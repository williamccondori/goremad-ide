import json

from owslib.wms import WebMapService

from app.legacy.compartido.consultar_detalles_servicio_request import ConsultarDetallesServicioRequest
from app.legacy.compartido.consultar_detalles_servicio_response import ConsultarDetallesServicioResponse
from app.legacy.compartido.consultar_servicio_request import ConsultarServicioRequest
from app.legacy.compartido.consultar_servicio_response import ConsultarServicioResponse


class ServicioServicio:
    @staticmethod
    def obtener_cuadro_delimitador(cuadro_delimitador: str) -> tuple[float, ...]:
        cuadro_delimitador = cuadro_delimitador.split(',')
        return tuple(float(i) for i in cuadro_delimitador)

    async def consultar(self, request: ConsultarServicioRequest) -> ConsultarServicioResponse:
        pass
    """
    base_url = url.split('?')[0]
        base_url_wms = f'{base_url}?service=wms&version=1.1.1'
        try:
            wms = WebMapService(base_url, version='1.1.1')
        except requests.exceptions.HTTPError as error:
            raise Exception(f'Error: {error}')
        layers = []
        for layer in wms.contents:
            layer_data = wms[layer]
            layer_url = f'{base_url_wms}&layer={layer}'
            layers.append(
                ExternalLayerItemSchema(id=str(uuid.uuid4()),
                                        title=layer_data.title,
                                        url=base_url,
                                        name=layer,
                                        version=wms.version,
                                        legend_url=f'{layer_url}&request=GetLegendGraphic&format=image/png',
                                        information_url=f'{layer_url}&request=GetFeatureInfo',
                                        opacity=1,
                                        attribution='',
                                        bounding_box=layer_data.boundingBoxWGS84,
                                        )
            )
        service = wms.identification
        return ExternalLayerCapabilitiesSchema(
            id=str(uuid.uuid4()),
            url=wms.url,
            title=service.title,
            abstract=service.abstract,
            version=wms.version,
            keywords=list(map((lambda x: x), service.keywords)),
            operations=list(map((lambda x: x.name), wms.operations)),
            layers=layers
        )
        
        class ExternalLayerItemSchema(BaseModel):
    id: str
    title: str
    url: str
    name: str
    version: str
    legend_url: str
    information_url: str
    opacity: float
    attribution: str
    bounding_box: list[float]


class ExternalLayerCapabilitiesSchema(BaseModel):
    id: str
    url: str
    title: str
    abstract: str
    version: str
    keywords: list[str]
    operations: list[str]
    layers: list[ExternalLayerItemSchema]

        """

    async def consultar_detalles(self,
                                 request: ConsultarDetallesServicioRequest) -> ConsultarDetallesServicioResponse:
        cuadro_delimitador: tuple[float, ...] = self.obtener_cuadro_delimitador(request.cuadro_delimitador)
        capas: list[str] = request.capas.split(',')

        servicio_wms = WebMapService(request.url)

        detalles_capa = servicio_wms.getfeatureinfo(
            srs='EPSG:4326',
            xy=(request.x, request.y),
            size=(request.ancho, request.alto),
            info_format="application/json",
            bbox=cuadro_delimitador,
            layers=capas,
            query_layers=capas
        )

        return json.loads(detalles_capa.read())


"""
group_layer_collection = GroupLayerCollection.find_one({
            "is_active": True,
            "_id": ObjectId(group_layer_id)
        })

        if not group_layer_collection:
            raise ApplicationException("Group layer not found", 404)

        GroupLayerCollection.update_one({
            "_id": ObjectId(group_layer_id)
        }, {
            "$set": {
                "name": request.name,
                "group_layer_id": request.group_layer_id,
                "updated_by": "admin"
            }
        })

        group_layer_updated = GroupLayerCollection.find_one({
            "_id": ObjectId(group_layer_id)
        })

        if not group_layer_updated:
            raise ApplicationException("Group layer not found", 404)

        return map_group_layer_response(group_layer_updated)
        
        
        
         group_layer_parent = GroupLayerCollection.find_one({
            "is_active": True,
            "_id": ObjectId(request.group_layer_id)
        })

        if not group_layer_parent:
            raise ApplicationException("Group layer parent not found", 404)

        grupo_capa: GrupoCapaEntidad = GrupoCapaEntidad(
            nombre=request.name,
            grupo_capa_id=group_layer_parent["_id"],
            created_by="admin",
        )
        resultado: InsertOneResult = GroupLayerCollection.insert_one(grupo_capa.dict())
        grupo_capa_creado = GroupLayerCollection.find_one({'_id': resultado.inserted_id})
        if not grupo_capa_creado:
            raise ApplicationException("No se ha creado el registro para el grupo de capa",
                                       status.HTTP_406_NOT_ACCEPTABLE)
        return str(resultado.inserted_id)
"""