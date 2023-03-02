import asyncio
import threading

from fastapi import APIRouter, Depends

from app.aplicacion.servicios.administrador.imagen_satelital_servicio import ImagenSatelitalServicio
from app.aplicacion.servicios.administrador.programacion_servicio import ProgramacionServicio
from app.dominio.entidades import programacion_entidad
from app.infraestructura.oauth_2.autorizador import obtener_usuario_registrado
from app.infraestructura.oauth_2.modelos.usuario_registrado_modelo import UsuarioRegistradoModelo

imagen_satelital_controller = APIRouter()


class Ejecutor(threading.Thread):
    def __init__(self, programacion_id: str, imagen_satelital_servicio: ImagenSatelitalServicio):
        threading.Thread.__init__(self)
        self.programacion_id = programacion_id
        self.imagen_satelital_servicio = imagen_satelital_servicio

    def run(self):
        asyncio.run(self.imagen_satelital_servicio.descargar(self.programacion_id))


@imagen_satelital_controller.post("/descargas/", response_model=str)
async def descargar(
        programacion_servicio: ProgramacionServicio = Depends(ProgramacionServicio),
        imagen_satelital_servicio: ImagenSatelitalServicio = Depends(ImagenSatelitalServicio),
        usuario_registrado: UsuarioRegistradoModelo = Depends(obtener_usuario_registrado),
) -> str:
    programacion_id: str = await programacion_servicio.crear(
        programacion_entidad.PROGRAMACION_IMAGEN_SATELITAL,
        usuario_registrado.id,
    )
    ejecutor = Ejecutor(programacion_id, imagen_satelital_servicio)
    ejecutor.start()

    return programacion_id
