from fastapi import APIRouter

base_dato_controller = APIRouter()

"""RESERVED_SCHEMAS = ['information_schema', 'pg_catalog', 'pg_toast', 'public', 'cron', 'topology']


class GetAllSchemasResponse(CustomBaseSchema):
    id: str
    name: str


class GetAllTablesResponse(CustomBaseSchema):
    id: str
    name: str
    schema_name: str


@database_router.get("/schemas/", response_model=list[GetAllSchemasResponse])
async def get_all_schemas(database_type: str) -> list[GetAllSchemasResponse]:
    try:
        schemas = postgres.obtener_esquemas(database_type)

        get_all_schemas_response = [
            GetAllSchemasResponse(id=schema['schema_name'], name=schema['schema_name'])
            for schema in schemas
        ]

        return get_all_schemas_response
    except Exception as e:
        raise APIException(e)


@database_router.get("/schemas/{schema_name}/tables/", response_model=list[GetAllTablesResponse])
async def get_all_tables(database_type: str, schema_name: str) -> list[GetAllTablesResponse]:
    try:
        tables = postgres.obtener_tablas(database_type, schema_name)

        get_all_tables_response = [
            GetAllTablesResponse(id=table['table_name'], name=table['table_name'], schema_name=table['table_schema'])
            for table in tables
        ]

        return get_all_tables_response
    except Exception as e:
        raise APIException(e)
        """
