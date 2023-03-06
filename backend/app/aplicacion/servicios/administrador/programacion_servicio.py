from datetime import datetime
from typing import Optional

from fastapi import Depends

from app.aplicacion.dtos.administrador.obtener_actual_programacion_reponse import ObtenerActualProgramacionResponse
from app.aplicacion.dtos.administrador.obtener_actual_programacion_request import ObtenerActualProgramacionRequest
from app.aplicacion.dtos.administrador.obtener_todo_programacion_response import ObtenerTodoProgramacionResponse
from app.dominio.entidades import programacion_entidad
from app.dominio.entidades.compartido import base_entidad
from app.dominio.entidades.programacion_entidad import ProgramacionEntidad
from app.dominio.entidades.usuario_entidad import UsuarioEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.programacion_repositorio import IProgramacionRepositorio
from app.dominio.repositorios.usuario_repositorio import IUsuarioRepositorio
from app.infraestructura.mongo_db.repositorios.programacion_repositorio import ProgramacionRepositorio
from app.infraestructura.mongo_db.repositorios.usuario_repositorio import UsuarioRepositorio


class ProgramacionServicio:
    def __init__(self,
                 programacion_repositorio: IProgramacionRepositorio = Depends(ProgramacionRepositorio),
                 usuario_repositorio: IUsuarioRepositorio = Depends(UsuarioRepositorio)
                 ):
        self._programacion_repositorio = programacion_repositorio
        self._usuario_repositorio = usuario_repositorio

    async def obtener_nombre_usuario(self, usuario_id: str) -> str:
        usuario: UsuarioEntidad = await self._usuario_repositorio.obtener_por_id(usuario_id)
        return usuario.username

    async def crear(self, tipo: str, usuario_auditoria_id: str) -> str:
        # Se verifica que no se este ejecutando una descarga
        existe_descarga: bool = await self._programacion_repositorio.verificar_existencia_por_filtros({
            "estado": base_entidad.ESTADO_ACTIVO,
            "tipo": programacion_entidad.PROGRAMACION_IMAGEN_SATELITAL,
            "estado_ejecucion": programacion_entidad.ESTADO_PENDIENTE
        })
        if existe_descarga:
            raise AplicacionException("Ya existe una descarga en proceso")
        fecha_actual: datetime = datetime.now()
        programacion: ProgramacionEntidad = ProgramacionEntidad(
            tipo=tipo,
            fecha_inicio=fecha_actual,
            estado_ejecucion=programacion_entidad.ESTADO_PENDIENTE,
            usuario=usuario_auditoria_id
        )
        programacion.registrar_creacion(usuario_auditoria_id)
        return await self._programacion_repositorio.crear(programacion)

    async def obtener_todos(self) -> list[ObtenerTodoProgramacionResponse]:
        programaciones: list[ProgramacionEntidad] = await self._programacion_repositorio.obtener_todos({
            "estado": base_entidad.ESTADO_ACTIVO
        })
        programaciones.sort(key=lambda x: x.fecha_inicio, reverse=True)
        return [ObtenerTodoProgramacionResponse(
            id=programacion.id,
            tipo=programacion.tipo,
            fecha_inicio=programacion.fecha_inicio.strftime("%d/%m/%Y %H:%M:%S"),
            fecha_fin=programacion.fecha_fin.strftime("%d/%m/%Y %H:%M:%S") if programacion.fecha_fin else None,
            estado_ejecucion=programacion.estado_ejecucion,
            observaciones=programacion.observaciones,
            usuario=await self.obtener_nombre_usuario(programacion.usuario)
        ) for programacion in programaciones]

    async def obtener_actual(self, request: ObtenerActualProgramacionRequest) \
            -> Optional[ObtenerActualProgramacionResponse]:
        tipo: str = request.tipo
        # Validacion de los tipos disponibles.
        if tipo not in [programacion_entidad.PROGRAMACION_IMAGEN_SATELITAL]:
            raise AplicacionException("Tipo de programación no disponible")
        programaciones: list[ProgramacionEntidad] = await self._programacion_repositorio.obtener_todos({
            "estado": base_entidad.ESTADO_ACTIVO,
            "tipo": tipo,
        })
        if len(programaciones) == 0:
            return None
        # Se ordena por fecha de inicio de forma descendente.
        programaciones.sort(key=lambda x: x.fecha_inicio, reverse=True)
        programacion: ProgramacionEntidad = programaciones[0]
        fecha_fin: Optional[str] = None
        if programacion.fecha_fin:
            fecha_fin = programacion.fecha_fin.strftime("%d/%m/%Y %H:%M:%S")
        return ObtenerActualProgramacionResponse(
            id=programacion.id,
            tipo=programacion.tipo,
            fecha_inicio=programacion.fecha_inicio.strftime("%d/%m/%Y %H:%M:%S"),
            fecha_fin=fecha_fin,
            estado_ejecucion=programacion.estado_ejecucion,
            observaciones=programacion.observaciones,
            usuario=await self.obtener_nombre_usuario(programacion.usuario)
        )
