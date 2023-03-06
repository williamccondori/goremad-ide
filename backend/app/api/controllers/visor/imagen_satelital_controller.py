from fastapi import APIRouter, Depends

from app.aplicacion.dtos.visor.buscar_imagen_satelital_request import BuscarImagenSatelitalRequest
from app.aplicacion.dtos.visor.buscar_imagen_satelital_response import BuscarImagenSatelitalResponse
from app.aplicacion.dtos.visor.obtener_capas_imagen_satelital_request import ObtenerCapasImagenSatelitalRequest
from app.aplicacion.dtos.visor.obtener_capas_imagen_satelital_response import ObtenerCapasImagenSatelitalResponse
from app.aplicacion.servicios.visor.imagen_satelital_servicio import ImagenSatelitalServicio

imagen_satelital_controller = APIRouter()


@imagen_satelital_controller.get("/busquedas/", response_model=list[BuscarImagenSatelitalResponse])
async def buscar(
        request: BuscarImagenSatelitalRequest = Depends(),
        imagen_satelital_servicio: ImagenSatelitalServicio = Depends(ImagenSatelitalServicio)
) -> list[BuscarImagenSatelitalResponse]:
    return await imagen_satelital_servicio.buscar(request)


@imagen_satelital_controller.get("/capas/", response_model=ObtenerCapasImagenSatelitalResponse)
async def obtener_capas(
        request: ObtenerCapasImagenSatelitalRequest = Depends(),
        imagen_satelital_servicio: ImagenSatelitalServicio = Depends(ImagenSatelitalServicio)
) -> ObtenerCapasImagenSatelitalResponse:
    return await imagen_satelital_servicio.obtener_capas(request)
