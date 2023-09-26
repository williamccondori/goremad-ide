from typing import Optional

from app.aplicacion.parseadores.base_modelo import BaseModelo


class CrearObjetoGeograficoRequest(BaseModelo):
    codigo: str
    nombre: str
    nombre_base_datos: str
    nombre_esquema: str
    nombre_tabla: str
    descripcion: Optional[str]
    estilo: Optional[str]
    grupo_id: str
    esta_habilitado: bool
