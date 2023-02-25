class ImagenSatelitalServicio:
    pass


"""
warnings.simplefilter(action='ignore', category=FutureWarning)

satellite_image_router = APIRouter()

STATUS_ERROR = "ERROR"
STATUS_SUCCESS = "SUCCESS"
STATUS_IN_PROGRESS = "IN_PROGRESS"


class DownloadSatelliteImageSchema(BaseModel):
    date: datetime


class DownloadSatelliteImageProcessModel(BaseModel):
    start_date: datetime
    status: str
    error: str = None

    # Audit fields.
    is_active: bool = True
    created_at: datetime = datetime.now()
    updated_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None

    class Config:
        orm_mode = True


def start_download_satellite_images():
    process_in_progress = DownloadSatelliteImageProcessCollection.find_one({
        'status': STATUS_IN_PROGRESS,
    })
    if not process_in_progress:
        download_satellite_images_process = DownloadSatelliteImageProcessModel(
            start_date=datetime.now(),
            status=STATUS_IN_PROGRESS,
            is_active=True,
        )
        result = DownloadSatelliteImageProcessCollection.insert_one(download_satellite_images_process.dict())

        try:
            api = SentinelAPI('williamccondori', 'Computo.123', 'https://scihub.copernicus.eu/dhus')
            geojson_path = os.path.join(settings.MEDIA_FOLDER, 'polygon.geojson')
            footprint = geojson_to_wkt(read_geojson(geojson_path))

            # Se busca y se descargan las imagenes que no hayan sido descargadas previamente.

            start_day = datetime.now() - timedelta(days=5)
            end_day = datetime.now()

            products = api.query(footprint,
                                 date=(start_day, end_day),
                                 platformname='Sentinel-2',
                                 cloudcoverpercentage=(0, 10),
                                 processinglevel='Level-1C',
                                 area_relation='Intersects')

            satellite_images = SatelliteImageCollection.find({
                'uuid': {
                    '$in': list(products.keys()),
                },
            })

            for satellite_image in satellite_images:
                products.pop(satellite_image['uuid'])

            print('Se encontraron %s imágenes' % len(products))

            api.download_all(list(products.keys()), directory_path=settings.MEDIA_FOLDER)

            for product in products.values():
                print('Se descargó la imagen %s' % product['title'])

                carpeta_salida = os.path.join(settings.MEDIA_FOLDER, product['title'])
                if os.path.exists(carpeta_salida):
                    shutil.rmtree(carpeta_salida)
                os.makedirs(carpeta_salida)
                archivo_comprimido = os.path.join(settings.MEDIA_FOLDER, product['title'] + '.zip')

                # Abrir el archivo comprimido y extraer los *.jp2.
                with zipfile.ZipFile(archivo_comprimido, 'r') as zip_ref:
                    [zip_ref.extract(file, carpeta_salida) for file in zip_ref.namelist() if file.endswith(".jp2")]

                # Mover todos los *.jp2 a la carpeta de salida.
                for file in os.walk(carpeta_salida):
                    for file_name in file[2]:
                        if str(file_name).endswith(".jp2"):
                            os.rename(os.path.join(file[0], file_name), os.path.join(carpeta_salida, file_name))

                bands = []
                for file_name in os.listdir(carpeta_salida):
                    file_name_path = os.path.join(carpeta_salida, file_name)
                    if str(file_name).startswith("T"):
                        if str(file_name).endswith("B02.jp2"):
                            bands.append(rasterio.open(file_name_path))
                        if str(file_name).endswith("B03.jp2"):
                            bands.append(rasterio.open(file_name_path))
                        if str(file_name).endswith("B04.jp2"):
                            bands.append(rasterio.open(file_name_path))
                        if str(file_name).endswith("B08.jp2"):
                            bands.append(rasterio.open(file_name_path))

                # Se obtiene los datos de la primera banda para la creación de la imagen.
                profile = bands[0].meta
                profile.update(
                    driver='GTiff',
                    dtype=rasterio.float32
                )

                # RECORTE DE LA IMAGEN.

                gdf = gpd.read_file(geojson_path)
                gdf = gdf.to_crs(crs=bands[0].crs.data)
                geometry = gdf[['geometry']].values.flatten()

                for i in range(len(bands)):
                    image, out_transform = mask(bands[i], geometry, crop=True)
                    bands[i] = image[0].astype(rasterio.float32)

                    # Se actualiza el perfil de la imagen.
                    profile.update({
                        "height": image.shape[1],
                        "width": image.shape[2],
                        "transform": out_transform
                    })

                print('Se recortó la imagen %s' % product['title'])

                output_path = os.path.join(carpeta_salida, product['title'])

                # RGB.

                profile.update(count=3)
                with rasterio.open(output_path + '_RGB.tif', 'w', **profile) as dst:
                    dst.write(bands[0], 1)
                    dst.write(bands[1], 2)
                    dst.write(bands[2], 3)

                # NDVI.

                profile.update(count=1)
                ndvi = (bands[3] - bands[2]) / (bands[3] + bands[2])
                with rasterio.open(output_path + '_NDVI.tif', 'w', **profile) as dst:
                    dst.write(ndvi, 1)

                # NDWI.

                profile.update(count=1)
                ndwi = (bands[1] - bands[3]) / (bands[1] + bands[3])
                with rasterio.open(output_path + '_NDWI.tif', 'w', **profile) as dst:
                    dst.write(ndwi, 1)

                print('Se procesó la imagen %s' % product['title'])

                # Eliminar los archivos diferentes a *.tif.
                for file in os.listdir(carpeta_salida):
                    if not str(file).endswith(".tif"):
                        path = os.path.join(carpeta_salida, file)
                        if os.path.isfile(path):
                            os.remove(path)
                        else:
                            shutil.rmtree(path)

            # Editar el estado del proceso a completado.
            DownloadSatelliteImageProcessCollection.update_one({
                '_id': result.inserted_id,
            }, {
                '$set': {
                    'status': STATUS_SUCCESS,
                    'is_active': False,
                },
            })
        except Exception as exception:
            print(exception)
            # Editar el estado del proceso si se encontró un error.
            DownloadSatelliteImageProcessCollection.update_one({
                '_id': result.inserted_id,
            }, {
                '$set': {
                    'status': STATUS_ERROR,
                    'error': str(exception),
                    'is_active': False,
                },
            })
    else:
        print("A download satellite images process is already in progress.")


@satellite_image_router.post("/", response_model=DownloadSatelliteImageSchema)
async def download_satellite_images():

    thead = threading.Thread(target=start_download_satellite_images)
    thead.start()

    return DownloadSatelliteImageSchema(
        date=datetime.now()
    )
    """
