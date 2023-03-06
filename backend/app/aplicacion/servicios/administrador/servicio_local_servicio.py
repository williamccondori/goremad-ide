from geo.Geoserver import Geoserver  # noqa

from app.settings import settings


class ServicioLocalServicio:
    async def sincronizar_capas(self):
        geoserver = Geoserver(settings.GEOSERVER_URL, username=settings.GEOSERVER_USER,
                              password=settings.GEOSERVER_PASSWORD)
        return []
