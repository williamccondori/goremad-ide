from pymongo import MongoClient

from app.settings import settings

cliente_mongo = MongoClient(settings.MONGODB_URL_BASE_DATOS)
base_datos = cliente_mongo[settings.MONGODB_NOMBRE_BASE_DATOS]

CapasBase = base_datos["capas_base"]
Configuraciones = base_datos["configuraciones"]
GruposCapas = base_datos["grupos_capas"]
ServiciosExternos = base_datos["servicios_externos"]
Usuarios = base_datos["usuarios"]
Publicaciones = base_datos["publicaciones"]
Programaciones = base_datos["programaciones"]
ImagenesSatelitales = base_datos["imagenes_satelitales"]
Catalogos = base_datos["catalogos"]
Temas = base_datos["temas"]
Grupos = base_datos["grupos"]
ObjetosGeograficos = base_datos["objetos_geograficos"]

print("Se ha iniciado la conexión con MongoDB en la clase: %s" % __name__)
print(
    "Se ha iniciado la conexión con MongoDB versión: %s"
    % cliente_mongo.server_info()["version"]
)
