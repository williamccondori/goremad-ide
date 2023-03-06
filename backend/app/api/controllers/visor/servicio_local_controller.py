from fastapi import APIRouter, Depends

from app.aplicacion.servicios.administrador.servicio_local_servicio import ServicioLocalServicio

servicio_local_controller = APIRouter()


@servicio_local_controller.get("/sincronizaciones/")
async def sincronizar_capas(
        servicio_local_servicio: ServicioLocalServicio = Depends(ServicioLocalServicio)
):
    return await servicio_local_servicio.sincronizar_capas()
