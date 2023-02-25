from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerEstructuraGrupoCapaResponse(BaseModelo):
    id: str
    label: str
    children: list["ObtenerEstructuraGrupoCapaResponse"] = []
