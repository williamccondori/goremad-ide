from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.api.controllers.administrador.autenticacion_controller import autenticacion_controller
from app.api.controllers.administrador.capa_base_controller import capa_base_controller
from app.api.controllers.administrador.configuracion_controller import configuracion_controller
from app.api.controllers.administrador.grupo_capa_controller import grupo_capa_controller
from app.api.controllers.administrador.imagen_satelital_controller import imagen_satelital_controller
from app.api.controllers.administrador.resumen_controller import resumen_controller
from app.api.controllers.administrador.servicio_externo_controller import servicio_externo_controller
from app.api.controllers.administrador.usuario_controller import usuario_controller
from app.api.controllers.visor.coordenada_controller import coordenada_controller as coordenada_visor_controller
from app.api.controllers.visor.inicial_controller import inicial_controller as inicial_visor_controller
from app.api.controllers.visor.ubicacion_controller import ubicacion_controller as ubicacion_visor_controller
from app.api.controllers.visor.usuario_controller import usuario_controller as usuario_visor_controller
from app.api.controllers.visor.web_map_service_controller import \
    web_map_service_controller as web_map_service_visor_controller
from app.aplicacion.parseadores.base_modelo import BaseModelo
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.settings import settings

ALLOW_METHODS_AND_HEADERS = ["*"]

ORIGINS = settings.ORIGENES_PERMITIDOS.split(",")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=ALLOW_METHODS_AND_HEADERS,
    allow_headers=ALLOW_METHODS_AND_HEADERS,
)
app.include_router(autenticacion_controller, prefix="/api/v1/auth", tags=["Autenticacion"])
app.include_router(capa_base_controller, prefix="/api/v1/capas-base", tags=["Capas base"])
app.include_router(configuracion_controller, prefix="/api/v1/configuraciones", tags=["Configuraciones"])
app.include_router(grupo_capa_controller, prefix="/api/v1/grupos-capas", tags=["Grupos de capas"])
app.include_router(resumen_controller, prefix="/api/v1/resumenes", tags=["Resúmenes"])
app.include_router(servicio_externo_controller, prefix="/api/v1/servicios-externos", tags=["Servicios externos"])
app.include_router(usuario_controller, prefix="/api/v1/usuarios", tags=["Usuarios"]),
app.include_router(imagen_satelital_controller, prefix="/api/v1/imagenes-satelitales", tags=["Imagenes satelitales"])

app.include_router(inicial_visor_controller, prefix="/api/v1/visor/iniciales", tags=["Iniciales (Visor)"])
app.include_router(ubicacion_visor_controller, prefix="/api/v1/visor/ubicaciones", tags=["Ubicaciones (Visor)"])
app.include_router(usuario_visor_controller, prefix="/api/v1/visor/usuarios", tags=["Usuarios (Visor)"])
app.include_router(web_map_service_visor_controller, prefix="/api/v1/visor/web-map-services",
                   tags=["Web map services (Visor)"])
app.include_router(coordenada_visor_controller, prefix="/api/v1/visor/coordenadas", tags=["Coordenadas (Visor)"])


class ExcepcionResponse(BaseModelo):
    codigo: int
    mensaje: str


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, excepcion: RequestValidationError):
    errores = excepcion.errors()
    campos_invalidos: list[str] = []
    for error in errores:
        campo_invalido: str = error["loc"][1]
        campos_invalidos.append(campo_invalido.upper())
    error_response = ExcepcionResponse(
        codigo=status.HTTP_422_UNPROCESSABLE_ENTITY,
        mensaje=f"Los siguientes atributos son inválidos: {', '.join(campos_invalidos)}"
    )
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=error_response.dict())


@app.exception_handler(AplicacionException)
async def api_exception_handler(_: Request, excepcion: AplicacionException):
    error_response = ExcepcionResponse(
        codigo=excepcion.codigo,
        mensaje=excepcion.mensaje
    )
    return JSONResponse(status_code=excepcion.codigo, content=error_response.dict())
