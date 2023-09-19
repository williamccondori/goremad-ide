from typing import Optional

from app.dominio.entidades.compartido.base_entidad import BaseEntidad


class ColumnaObjetoGeograficoEntidad(BaseEntidad):
    id: str = None
    nombre: str
    tipo: str
    longitud: int
    mascara: str
    objeto_geografico_id: str
    esta_habilitado: bool
