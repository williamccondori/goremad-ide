from fastapi import APIRouter, Depends, UploadFile, File

from app.aplicacion.dtos.visor.obtener_geometria_carga_response import ObtenerGeometriaCargaResponse
from app.aplicacion.servicios.visor.carga_servicio import CargaServicio

carga_controller = APIRouter()


@carga_controller.post("/geometrias/")
async def transformar_a_geojson(
        archivo: UploadFile = File(...),
        carga_servicio: CargaServicio = Depends()
) -> ObtenerGeometriaCargaResponse:
    return await carga_servicio.obtener_geometria(archivo)
