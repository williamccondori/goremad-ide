class AplicacionException(Exception):
    def __init__(self, mensaje, codigo=400):
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self):
        return self.mensaje
