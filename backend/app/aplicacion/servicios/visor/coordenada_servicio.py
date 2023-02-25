import pyproj

from app.aplicacion.dtos.visor.obtener_coordenada_request import ObtenerCoordenadaRequest
from app.aplicacion.dtos.visor.obtener_coordenada_response import ObtenerCoordenadaResponse
from app.dominio.excepciones.aplicacion_exception import AplicacionException


class CoordenadaServicio:
    @staticmethod
    def validar_parametros(request: ObtenerCoordenadaRequest) -> None:
        if request.proyeccion == "utm":
            if request.zona is None or request.zona == 0:
                raise AplicacionException("La proyección UTM requiere la zona.")
            if not (0 < request.x < 1000000 and 0 < request.y < 10000000):
                raise AplicacionException("Las coordenadas no están dentro de los límites.")
        else:
            if not (-180 < request.x < 180 and -85 < request.y < 85):
                raise AplicacionException("Las coordenadas no están dentro de los límites.")

    async def obtener_coordenadas(self, request: ObtenerCoordenadaRequest) -> ObtenerCoordenadaResponse:
        self.validar_parametros(request)
        # Define el sistema de coordenadas de origen.
        if request.proyeccion == "utm":
            proyeccion_entrada = pyproj.Proj(
                proj=request.proyeccion,
                datum=request.datum,
                zone=request.zona
            )
        else:
            proyeccion_entrada = pyproj.Proj(
                proj=request.proyeccion,
                datum=request.datum
            )
        print(proyeccion_entrada)
        # Define el sistema de coordenadas de destino (EPSG:4326).
        proyeccion_salida = pyproj.Proj(proj="latlong", datum="WGS84")
        entrada_crs = pyproj.CRS.from_proj4(proyeccion_entrada.srs)
        salida_crs = pyproj.CRS.from_proj4(proyeccion_salida.srs)
        # Transforma las coordenadas.
        transformer = pyproj.Transformer.from_crs(entrada_crs, salida_crs)
        longitud, latitud = transformer.transform(request.x, request.y)
        return ObtenerCoordenadaResponse(
            longitud=longitud,
            latitud=latitud
        )
