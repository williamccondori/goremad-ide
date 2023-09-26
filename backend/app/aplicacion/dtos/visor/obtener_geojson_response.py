from app.aplicacion.parseadores.base_modelo import BaseModelo

ORIGEN_POSTGRESQL = "POSTGRESQL"
ORIGEN_CARGA = "CARGA"

ESTILO_PREDETERMINADO = {
    "color": "#000000",
    "fillColor": "#333333",
    "fillOpacity": 0.5,
}


class ObtenerGeojsonResponse(BaseModelo):
    id: str
    origen: str
    nombre: str
    descripcion: str
    estilo: str
    geometria: str
    cuadro_delimitador: list[float]
    transparencia: float = 0
