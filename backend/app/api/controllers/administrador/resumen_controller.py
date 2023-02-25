from fastapi import APIRouter, Depends

from app.aplicacion.dtos.administrador.obtener_totales_resumen_response import ObtenerTotalesResumenResponse
from app.aplicacion.servicios.administrador.resumen_servicio import ResumenServicio
from app.infraestructura.oauth_2.autorizador import obtener_usuario_registrado
from app.infraestructura.oauth_2.modelos.usuario_registrado_modelo import UsuarioRegistradoModelo

resumen_controller = APIRouter()


@resumen_controller.get("/", response_model=ObtenerTotalesResumenResponse)
async def obtener_totales(
        resumen_servicio: ResumenServicio = Depends(ResumenServicio),
        _: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado)) -> ObtenerTotalesResumenResponse:
    return await resumen_servicio.obtener_totales()
