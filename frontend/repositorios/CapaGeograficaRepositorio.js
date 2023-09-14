import axios from 'axios';

const WFS_URL = 'https://ide.regionmadrededios.gob.pe/geoserver/ows?';

const CAPAS_GEOGRAFICAS = {
  Con_ConcesionProForDifMad: {
    nombre: 'Con_ConcesionProForDifMad',
    titulo: 'Concesión para productos forestales diferentes a la madera',
    descripcion: '',
    tipoEstilo: 'poligono',
    estilos: {
      color: '#a80084',
      fillColor: '#FFFFFF',
      fillOpacity: 0,
      lineJoin: 'bevel',
      opacity: 1,
      weight: 2,
    },
  },
};

async function obtenerInformacionCapaGeografica(nombreCapaGeografica) {
  const params = {
    service: 'WFS',
    version: '1.0.0',
    request: 'GetFeature',
    typeName: `Servicio_OGC:${nombreCapaGeografica}`,
    outputFormat: 'application/json',
    srsName: 'EPSG:4326',
  };

  try {
    const { data } = await axios.get(WFS_URL, { params });

    const features = data?.features;

    if (features) {
      const registros = features.map((feature, index) => {
        return {
          id: index + 1,
          ...feature.properties,
        };
      });
      const columnas = Object.keys(registros[0]).map((key) => {
        return {
          title: key === 'id' ? 'ID' : key,
          dataIndex: key,
          key,
        };
      });
      const capaGeografica = CAPAS_GEOGRAFICAS[nombreCapaGeografica];
      if (capaGeografica) {
        return {
          registros,
          columnas,
          total: registros.length,
          ...capaGeografica,
        };
      }
    }
    return;
  } catch (error) {
    console.error(`Error al obtener los datos: ${error}`);
    throw error;
  }
}

async function obtenerGeometria(nombreCapaGeografica) {
  const params = {
    service: 'WFS',
    version: '1.0.0',
    request: 'GetFeature',
    typeName: `Servicio_OGC:${nombreCapaGeografica}`,
    outputFormat: 'application/json',
    srsName: 'EPSG:4326',
  };

  try {
    const { data } = await axios.get(WFS_URL, { params });
    if (data.features) {
      return {
        ...CAPAS_GEOGRAFICAS[nombreCapaGeografica],
        geojson: data,
      };
    }
  } catch (error) {
    console.error(`Error al obtener los datos: ${error}`);
    throw error;
  }
}

export { obtenerInformacionCapaGeografica, obtenerGeometria };
