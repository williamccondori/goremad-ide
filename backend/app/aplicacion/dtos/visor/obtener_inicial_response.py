from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class CapaBaseResponse(BaseModelo):
    id: str
    nombre: str
    url: str
    atribucion: str


class ServicioExternoResponse(BaseModelo):
    id: str
    servicio_id: str
    servicio_titulo: str
    nombre: str
    titulo: str
    url: str
    url_leyenda: str
    atribucion: str
    cuadro_delimitador: list[float]
    grupo_capa_id: Optional[str]
    transparencia: int


class EstructuraCapaResponse(BaseModelo):
    id: str
    label: str
    children: list["EstructuraCapaResponse"] = []
    es_grupo: bool = True


class ObtenerInicialResponse(BaseModelo):
    estructura: list[EstructuraCapaResponse] = []
    capas_base: list[CapaBaseResponse] = []
    servicios_externos: list[ServicioExternoResponse] = []
    capas_activas: list[str] = []
    capa_base_incial_id: str
    latitud_inicial: float
    longitud_inicial: float
    zoom_inicial: int
