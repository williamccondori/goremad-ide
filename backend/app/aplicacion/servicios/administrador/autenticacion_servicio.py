from datetime import timedelta, datetime
from typing import Optional

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt  # noqa
from starlette import status

from app.aplicacion.dtos.administrador.iniciar_sesion_response import (
    IniciarSesionResponse,
)
from app.aplicacion.servicios.administrador.usuario_servicio import encriptador
from app.dominio.entidades.compartido import base_entidad
from app.dominio.entidades.usuario_entidad import UsuarioEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.usuario_repositorio import IUsuarioRepositorio
from app.infraestructura.mongo_db.repositorios.usuario_repositorio import (
    UsuarioRepositorio,
)
from app.settings import settings


class AutenticacionServicio:
    def __init__(
        self, usuario_repositorio: IUsuarioRepositorio = Depends(UsuarioRepositorio)
    ):
        self._usuario_repositorio = usuario_repositorio

    @staticmethod
    def crear_token_acceso(
        data: dict, tiempo_expiracion_token: Optional[timedelta]
    ) -> str:
        para_codificar = data.copy()
        if tiempo_expiracion_token:
            expiracion = datetime.utcnow() + tiempo_expiracion_token
        else:
            expiracion = datetime.utcnow() + timedelta(minutes=30)
        para_codificar.update({"exp": expiracion})
        return jwt.encode(
            para_codificar, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM
        )

    @staticmethod
    def verificar_contrasenia(contrasenia_plana, contrasenia_encriptada) -> bool:
        return encriptador.verify(contrasenia_plana, contrasenia_encriptada)

    async def autenticar_usuario(self, usuario, password) -> UsuarioEntidad:
        usuario: UsuarioEntidad = await self._usuario_repositorio.obtener_por_filtros(
            {"estado": base_entidad.ESTADO_ACTIVO, "username": usuario}
        )
        if not usuario:
            raise AplicacionException(
                "El usuario ingresado es incorrecto", status.HTTP_401_UNAUTHORIZED
            )
        contrasenia_valida: bool = self.verificar_contrasenia(
            password, usuario.password
        )
        if not contrasenia_valida:
            raise AplicacionException(
                "La contraseña ingresada es incorrecta", status.HTTP_401_UNAUTHORIZED
            )
        if not usuario.esta_habilitado:
            raise AplicacionException(
                "El usuario no está habilitado para ingresar al sistema",
                status.HTTP_401_UNAUTHORIZED,
            )
        return usuario

    async def iniciar_sesion(
        self, request: OAuth2PasswordRequestForm
    ) -> IniciarSesionResponse:
        usuario: UsuarioEntidad = await self.autenticar_usuario(
            request.username, request.password
        )
        tiempo_expiracion_token: timedelta = timedelta(
            minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
        )
        token_acceso = self.crear_token_acceso(
            data={
                "sub": usuario.id,
                "username": usuario.username,
                "scopes": usuario.roles,
            },
            tiempo_expiracion_token=tiempo_expiracion_token,
        )
        return IniciarSesionResponse(access_token=token_acceso)
