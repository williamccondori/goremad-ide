from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerGeometriaObjetoGeograficoResponse(BaseModelo):
    id: str
    codigo: str
    nombre: str
    descripcion: str
    estilo: str
    geometria: str
