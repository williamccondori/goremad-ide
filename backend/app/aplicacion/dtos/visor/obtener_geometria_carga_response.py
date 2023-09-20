from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerGeometriaCargaResponse(BaseModelo):
    nombre: str
    extension: str
    cantidad_registros: int
    geojson: str
    tipo_geometria: str
