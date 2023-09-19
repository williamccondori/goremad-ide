from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from bson import ObjectId
from typing import List
from .models import Tema, TemaCreate, TemaUpdate


client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
temas_collection = db["temas"]


tema_controller = APIRouter()


# Create
@tema_controller.post("/", response_model=Tema)
async def create_tema(tema: TemaCreate):
    tema_dict = tema.dict()
    tema_dict["_id"] = ObjectId()
    temas_collection.insert_one(tema_dict)
    return tema


# Read all
@tema_controller.get("/", response_model=List[Tema])
async def read_temas():
    temas = []
    for tema in temas_collection.find():
        temas.append(Tema(**tema))
    return temas


# Read one
@tema_controller.get("/{tema_id}", response_model=Tema)
async def read_tema(tema_id: str):
    tema = temas_collection.find_one({"_id": ObjectId(tema_id)})
    if not tema:
        raise HTTPException(status_code=404, detail="Tema not found")
    return Tema(**tema)


# Update
@tema_controller.put("/{tema_id}", response_model=Tema)
async def update_tema(tema_id: str, tema: TemaUpdate):
    temas_collection.update_one({"_id": ObjectId(tema_id)}, {"$set": tema.dict()})
    updated_tema = temas_collection.find_one({"_id": ObjectId(tema_id)})
    if not updated_tema:
        raise HTTPException(status_code=404, detail="Tema not found")
    return Tema(**updated_tema)


# Delete
@tema_controller.delete("/{tema_id}")
async def delete_tema(tema_id: str):
    result = temas_collection.delete_one({"_id": ObjectId(tema_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Tema not found")
    return {"message": "Tema deleted successfully"}
