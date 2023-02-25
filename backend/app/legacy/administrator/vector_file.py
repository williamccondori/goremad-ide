import geopandas
import pandas as pd
from bson import ObjectId
from fastapi import APIRouter, Form, Depends, File, UploadFile
from pandas import DataFrame
from pandas.errors import ParserError
from sqlalchemy import create_engine

from database import VectorFileCollection
from exceptions import APIException, ApplicationException
from app.legacy.helpers import postgres
from parser import CustomBaseModel, CustomBaseSchema

SCHEMA = "GEOGOREMAD"


class VectorFileModel(CustomBaseModel):
    name: str
    description: str


class VectorFileResponse(CustomBaseSchema):
    id: str
    name: str
    description: str


class SaveVectorFileRequest:
    def __init__(self,
                 name: str = Form(),
                 description: str = Form(),
                 file: UploadFile = File(...)):
        self.name = name
        self.description = description
        self.file = file


vector_file_router = APIRouter()


@vector_file_router.get("/", response_model=list[VectorFileResponse])
async def get_all_vector_files() -> list[VectorFileResponse]:
    try:
        vector_files = VectorFileCollection.find({
            "is_active": True
        })

        vector_layer_response = [
            VectorFileResponse(
                id=str(vector_file["_id"]),
                name=vector_file["name"],
                description=vector_file["description"]
            ) for vector_file in vector_files
        ]

        return vector_layer_response
    except Exception as e:
        raise APIException(e)


@vector_file_router.get("/{vector_file_id}", response_model=VectorFileResponse)
async def get_vector_file_by_id(vector_file_id: str) -> VectorFileResponse:
    try:
        vector_file = VectorFileCollection.find_one({
            "is_active": True,
            "_id": ObjectId(vector_file_id)
        })

        if not vector_file:
            raise ApplicationException("Vector file not found", 404)

        vector_layer_response = VectorFileResponse(
            id=str(vector_file["_id"]),
            name=vector_file["name"],
            description=vector_file["description"]
        )

        return vector_layer_response
    except Exception as e:
        raise APIException(e)


@vector_file_router.post("/", response_model=VectorFileResponse, status_code=201)
async def create_vector_file(request: SaveVectorFileRequest = Depends()) -> VectorFileResponse:
    try:
        # Validate request.
        if not request.name.isalpha():
            raise ApplicationException("Invalid name, only alpha characters are allowed", 400)

        vector_file = VectorFileCollection.find_one({
            "is_active": True,
            "name": request.name
        })

        if vector_file:
            raise ApplicationException("Vector file already exists", 400)

        geospatial_file: UploadFile = request.file
        gdf: DataFrame = geopandas.read_file(geospatial_file.file)

        # Improve the date columns.

        for column in gdf.columns[gdf.dtypes == 'object']:
            try:
                if gdf[column].dropna().size > 0:
                    gdf[column] = pd.to_datetime(gdf[column])
            except (ParserError, ValueError):
                pass

        # Standardize coordinates system.

        gdf.set_crs(epsg=32719, inplace=True)

        # Standardize geometry column name.

        geom_column: str = gdf.geometry.name
        gdf.rename(columns={geom_column: 'geom'}, inplace=True)
        gdf.set_geometry('geom', inplace=True)

        # Save to production database.

        engine = create_engine(postgres.get_production_general_database_url())

        gdf.to_postgis(
            con=engine,
            schema=SCHEMA,
            name=request.name,
            index=False, if_exists='replace')

        with engine.connect() as conn:
            with conn.begin():
                conn.execute(
                    f"COMMENT ON TABLE \"{SCHEMA}\".\"{request.name}\" "
                    f"IS 'Represents the vector file {request.description}';")
        engine.dispose()

        # Save to GeoGOREMAD database.

        vector_file: VectorFileModel = VectorFileModel(
            name=request.name,
            description=request.description,
            created_by="admin"
        )

        result = VectorFileCollection.insert_one(vector_file.dict())

        vector_file_created = VectorFileCollection.find_one({
            '_id': result.inserted_id,
        })

        if not vector_file_created:
            raise ApplicationException("Vector file not created", 404)

        vector_file_response = {
            "id": str(vector_file_created['_id']),
            "name": vector_file_created['name'],
            "description": vector_file_created['description'],
            "created_by": vector_file_created['created_by']
        }

        return VectorFileResponse(**vector_file_response)
    except Exception as e:
        raise APIException(e)


@vector_file_router.delete("/{vector_file_id}", response_model=str)
async def delete_vector_file(vector_file_id: str) -> str:
    try:
        vector_file = VectorFileCollection.find_one({
            "is_active": True,
            "_id": ObjectId(vector_file_id)
        })

        if not vector_file:
            raise ApplicationException("Vector file not found", 404)

        engine = create_engine(postgres.get_production_general_database_url())
        with engine.connect() as conn:
            with conn.begin():
                conn.execute(
                    f"DROP TABLE IF EXISTS \"{SCHEMA}\".\"{vector_file['name']}\" CASCADE;")
        engine.dispose()

        VectorFileCollection.update_one({
            "_id": ObjectId(vector_file_id)
        }, {
            "$set": {
                "is_active": False
            }
        })

        return vector_file_id
    except Exception as e:
        raise APIException(e)
