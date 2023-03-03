import uuid

from fastapi import APIRouter
from geo.Geoserver import Geoserver  # noqa

from exceptions import APIException, ApplicationException
from parser import CustomBaseSchema
from settings import settings

WMS_STORE = 'WMS'
WFS_STORE = 'WFS'

WMS_SCHEMA = 'WMS'
WFS_SCHEMA = 'WFS'

geoserver_router = APIRouter()

class CreateWorkspaceSchema(CustomBaseSchema):
    name: str


def get_workspace_by_name(geoserver_instance, workspace_name):
    result = geoserver_instance.get_workspace(workspace_name)
    if type(result) is str:
        raise ApplicationException("Error getting workspace")
    if not result['workspace']:
        raise ApplicationException("Workspace not found")

    workspace = result["workspace"]
    return {
        "id": workspace["name"],
        "name": workspace["name"],
        "isolated": workspace["isolated"],
        "date_created": workspace["dateCreated"]
    }


@geoserver_router.get("/workspaces/", response_model=list[dict])
async def get_all_workspaces() -> list[dict]:
    try:
        geoserver = Geoserver(settings.GEOSERVER_URL, username=settings.GEOSERVER_USER,
                              password=settings.GEOSERVER_PASSWORD)

        result = geoserver.get_workspaces()
        if type(result) is str:
            raise ApplicationException("Error getting workspaces")

        return list(map(lambda x: {
            "id": x["name"],
            "name": x["name"]
        }, result["workspaces"]["workspace"] if result["workspaces"] else []))
    except Exception as e:
        raise APIException(e)


@geoserver_router.get("/workspaces/{workspace_name}/", response_model=dict)
async def get_workspace_by_name(workspace_name: str) -> dict:
    try:
        geoserver = Geoserver(settings.GEOSERVER_URL, username=settings.GEOSERVER_USER,
                              password=settings.GEOSERVER_PASSWORD)

        return get_workspace_by_name(geoserver, workspace_name)
    except Exception as e:
        raise APIException(e)


@geoserver_router.post("/workspaces/", response_model=dict)
async def create_workspace(request: CreateWorkspaceSchema) -> dict:
    try:
        geoserver = Geoserver(settings.GEOSERVER_URL, username=settings.GEOSERVER_USER,
                              password=settings.GEOSERVER_PASSWORD)

        result = geoserver.get_workspace(request.name)
        if type(result) is str:
            raise ApplicationException("Error getting workspace")
        if result and result["workspace"]:
            raise ApplicationException("Workspace already exists")

        geoserver.create_workspace(request.name)
        geoserver.create_featurestore(WFS_STORE, workspace=request.name, host=settings.SERVER_LOCAL_HOST,
                                      port=settings.DISTRIBUTION_DATABASE_PORT, db=settings.DISTRIBUTION_DATABASE_NAME,
                                      schema=WFS_SCHEMA, pg_user=settings.DISTRIBUTION_DATABASE_USER,
                                      pg_password=settings.DISTRIBUTION_DATABASE_PASSWORD, expose_primary_keys="true")

        return get_workspace_by_name(geoserver, request.name)
    except Exception as e:
        raise APIException(e)


@geoserver_router.delete("/workspaces/{workspace_name}/", response_model=dict)
async def delete_workspace(workspace_name: str) -> dict:
    try:
        geoserver = Geoserver(settings.GEOSERVER_URL, username=settings.GEOSERVER_USER,
                              password=settings.GEOSERVER_PASSWORD)

        result = geoserver.get_workspace(workspace_name)
        if type(result) is str:
            raise ApplicationException("Error getting workspace")
        if not result["workspace"]:
            raise ApplicationException("Workspace not found")

        result = geoserver.delete_workspace(workspace_name)
        if not result:
            raise ApplicationException("Error deleting workspace")

        return {
            "name": workspace_name,
        }
    except Exception as e:
        raise APIException(e)


# ==============================================================================
# Layers
# ==============================================================================

@geoserver_router.get("/layers/", response_model=list[dict])
async def get_all_layers(workspace: str) -> list[dict]:
    try:
        geoserver = Geoserver(settings.GEOSERVER_URL, username=settings.GEOSERVER_USER,
                              password=settings.GEOSERVER_PASSWORD)

        result = geoserver.get_layers(workspace)
        if type(result) is str:
            raise ApplicationException("Error getting layers")

        return list(map(lambda x: {
            "id": str(uuid.uuid4()),
            "name": x["name"]
        }, result["layers"]["layer"] if result["layers"] else []))
    except Exception as e:
        raise APIException(e)


@geoserver_router.get("/layers/{layer_name}/", response_model=dict)
async def get_layer_by_name(layer_name: str) -> dict:
    try:
        geoserver = Geoserver(settings.GEOSERVER_URL, username=settings.GEOSERVER_USER,
                              password=settings.GEOSERVER_PASSWORD)

        result = geoserver.get_layer(layer_name)
        if type(result) is str:
            raise ApplicationException("Error getting layer")
        if not result["layer"]:
            raise ApplicationException("Layer not found")

        layer = result["layer"]
        return {
            "id": str(uuid.uuid4()),
            "name": layer["name"],
            "type": layer["type"],
            "resource": layer["resource"]["name"] if layer["resource"] else "N/A",
            "date_created": layer["dateCreated"]
        }
    except Exception as e:
        raise APIException(e)
