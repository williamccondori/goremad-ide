from pymongo import MongoClient

from app.settings import settings

cliente_mongo = MongoClient(settings.MONGODB_URL_BASE_DATOS)
base_datos = cliente_mongo[settings.MONGODB_NOMBRE_BASE_DATOS]

CapasBase = base_datos['capas_base']
Configuraciones = base_datos['configuraciones']
GruposCapas = base_datos['grupos_capas']
ServiciosExternos = base_datos['servicios_externos']
Usuarios = base_datos['usuarios']
Publicaciones = base_datos['publicaciones']

print("Se ha iniciado la conexión con MongoDB en la clase: %s" % __name__)
print("Se ha iniciado la conexión con MongoDB versión: %s" % cliente_mongo.server_info()['version'])
