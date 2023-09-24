from datetime import datetime

from app.dominio.entidades.compartido.base_entidad import BaseEntidad


class ObjetoGeograficoGeometriaEntidad(BaseEntidad):
    id: str = None
    objeto_geografico_id: str
    geometria: str
    fecha_ultima_actualizacion: datetime
