from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerPorIdObjetoGeograficoResponse(BaseModelo):
    id: str = None
    codigo: str
    nombre: str
    nombre_base_datos: str
    nombre_tabla: str
    nombre_esquema: str
    descripcion: Optional[str]
    estilo: Optional[str]
    esta_habilitado: bool
    grupo_id: str
