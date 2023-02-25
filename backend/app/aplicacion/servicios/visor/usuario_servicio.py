from app.aplicacion.dtos.visor.obtener_todos_servicio_externo_usuario_response import \
    ObtenerTodosServicioExternoUsuarioResponse


class UsuarioServicio:
    async def obtener_servicios_externos(self, usuario_id: str) -> list[ObtenerTodosServicioExternoUsuarioResponse]:
        return []
