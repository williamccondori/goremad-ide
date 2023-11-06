from typing import Optional

from app.dominio.entidades.compartido.base_entidad import BaseEntidad

TIPO_PUBLICACION_NOTICIA = "noticia"
TIPO_PUBLICACION_PUBLICACION = "publicacion"
TIPO_PUBLICACION_DOCUMENTO = "documento"


class PublicacionEntidad(BaseEntidad):
    id: str = None
    tipo: str
    titulo: str
    resumen: str
    contenido: Optional[str]
    imagen: Optional[str]
    esta_habilitado: bool
