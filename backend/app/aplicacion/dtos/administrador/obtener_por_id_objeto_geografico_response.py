from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerPorIdObjetoGeograficoResponse(BaseModelo):
    id: str = None
    codigo: str
    nombre: str
    nombre_geoserver: str
    descripcion: Optional[str]
    estilo: Optional[str]
    esta_habilitado: bool
    grupo_id: str
