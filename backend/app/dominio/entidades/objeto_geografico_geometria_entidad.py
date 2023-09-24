from datetime import datetime

from app.dominio.entidades.compartido.base_entidad import BaseEntidad


class ObjetoGeograficoInformacionEntidad(BaseEntidad):
    id: str = None
    objeto_geografico_id: str
    codigo: str
    nombre: str
    descripcion: str
    estilo: str
    geometria: str
    fecha_ultima_actualizacion: datetime
