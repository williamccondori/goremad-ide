from app.aplicacion.dtos.visor.capa_response import CapaResponse
from app.aplicacion.parseadores.base_modelo import BaseModelo


class CapaBaseResponse(BaseModelo):
    id: str
    nombre: str
    url: str
    atribucion: str


class EstructuraCapaResponse(BaseModelo):
    id: str
    label: str
    children: list["EstructuraCapaResponse"] = []
    es_grupo: bool = True


class ObtenerInicialResponse(BaseModelo):
    estructura: list[EstructuraCapaResponse] = []
    capas_base: list[CapaBaseResponse] = []
    servicios_externos: list[CapaResponse] = []
    capas_activas: list[str] = []
    capa_base_incial_id: str
    latitud_inicial: float
    longitud_inicial: float
    zoom_inicial: int
