from app.aplicacion.parseadores.base_modelo import BaseModelo


class ObtenerInformacionObjetoGeograficoResponse(BaseModelo):
    id: str
    codigo: str
    nombre: str
    descripcion: str
    estilo: str
    geometria: str
