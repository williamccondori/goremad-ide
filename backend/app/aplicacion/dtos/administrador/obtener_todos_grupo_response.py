from app.aplicacion.dtos.administrador.obtener_por_id_grupo_response import \
    ObtenerPorIdGrupoResponse


class ObtenerTodosGrupoResponse(ObtenerPorIdGrupoResponse):
    tema_nombre: str
