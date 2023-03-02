from datetime import datetime

from fastapi import Depends

from app.dominio.entidades import programacion_entidad
from app.dominio.entidades.compartido import base_entidad
from app.dominio.entidades.programacion_entidad import ProgramacionEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.programacion_repositorio import IProgramacionRepositorio
from app.infraestructura.mongo_db.repositorios.programacion_repositorio import ProgramacionRepositorio


class ProgramacionServicio:
    def __init__(self,
                 programacion_repositorio: IProgramacionRepositorio = Depends(ProgramacionRepositorio)
                 ):
        self._programacion_repositorio = programacion_repositorio

    async def crear(self, tipo: str, usuario_auditoria_id: str) -> str:
        # Se verifica que no se este ejecutando una descarga
        existe_descarga = await self._programacion_repositorio.verificar_existencia_por_filtros({
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
