from app.dominio.entidades.compartido.base_entidad import BaseEntidad


class CapaBaseEntidad(BaseEntidad):
    id: str = None
    nombre: str
    url: str
    atribucion: str
    esta_habilitado: bool
