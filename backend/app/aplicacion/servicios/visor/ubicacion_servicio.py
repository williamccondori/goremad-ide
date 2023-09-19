import uuid

import requests

from app.aplicacion.dtos.visor.obtener_ubicacion_request import ObtenerUbicacionRequest
from app.aplicacion.dtos.visor.obtener_ubicacion_response import (
    ObtenerUbicacionResponse,
)
from app.settings import settings


class UbicacionServicio:
    @staticmethod
    def __obtener_url_busqueda(nombre_ubicacion: str) -> str:
        url_mapbox: str = f"https://api.mapbox.com/geocoding/v5/mapbox.places/${nombre_ubicacion}.json"
        url_mapbox += f"?access_token={settings.MAPBOX_TOKEN}&language=es"
        return url_mapbox

    async def obtener_todos(
        self, request: ObtenerUbicacionRequest
    ) -> list[ObtenerUbicacionResponse]:
        # Se obtienen los tipos de lugar de mapbox y se asigna un zoom correspondiente.
        tipo_lugar = {
            "country": 6,
            "place": 12,
            "locality": 14,
            "neighborhood": 16,
            "address": 18,
            "poi": 18,
        }
        # Se realiza la consulta a mapbox.
        respuesta = requests.get(self.__obtener_url_busqueda(request.query))
        if respuesta.status_code != 200:
            return []
        # Se obtienen las ubicaciones y se mapean al modelo de respuesta.
        respuesta_json = respuesta.json()
        ubicaciones: list[dict] = respuesta_json["features"]
        return [
            ObtenerUbicacionResponse(
                id=str(uuid.uuid4()),
                nombre=ubicacion.get("place_name"),
                centro=list(reversed(ubicacion.get("center", []))),
                zoom=tipo_lugar.get(ubicacion.get("place_type", ["place"])[0], 12),
            )
            for ubicacion in ubicaciones
        ]
