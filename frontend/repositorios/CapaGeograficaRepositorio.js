import axios from 'axios';

const WFS_URL = 'https://ide.regionmadrededios.gob.pe/geoserver/ows?';

const CAPAS_GEOGRAFICAS = {
  Act_AutorizacionDes: {
    nombre: 'Act_AutorizacionDes',
    titulo: 'Autorización de desbosque',
    descripcion:
      'El desbosque consiste en el retiro de la cobertura forestal mediante cualquier método que conlleve la pérdida del estado natural del recurso forestal. El desbosque se realiza en áreas comprendidas en cualquier categoría del patrimonio forestal de la Nación, para el desarrollo de actividades productivas que no tengan como fines su manejo forestal sostenible, tales como: la instalación de infraestructura, la apertura de vías de comunicación, incluyendo caminos de acceso a áreas de producción forestal, la producción o transporte de energía, así como operaciones energéticas, hidrocarburíferas y mineras. El desbosque es un acto administrativo que no constituye título habilitante. (Área de Conservación Privada). Las ANP son parte del ordenamiento forestal, sin perjuicio de ello, su establecimiento y gestión se rige por sus propias normas.',
    tipoEstilo: 'poligono',
    estilos: {},
  },
  Act_AutorizacionCamUsoActTieFinAgrPrePri: {
    nombre: 'Act_AutorizacionCamUsoActTieFinAgrPrePri',
    titulo:
      'Autorización de cambio de uso actual de las tierras a fines agropecuarios en predios privadoss',
    descripcion:
      'Todo proyecto productivo con fines agropecuarios en predios privados que impliquen el retiro de cobertura forestal, requiere una autorización de cambio de uso actual de la tierra previa, para el retiro de la cobertura forestal. Es un acto administrativo que no constituye título habilitante.',
    tipoEstilo: 'poligono',
    estilos: {},
  },
  Con_ConcesionProForDifMad: {
    nombre: 'Con_ConcesionProForDifMad',
    titulo: 'Concesión para productos forestales diferentes a la madera',
    descripcion:
      'Las concesiones para el aprovechamiento de otros productos del bosque son a exclusividad y están orientadas a especies de flora y fauna, tales como: castaña, aguaje, palmito, lianas, resinas, gomas, plantas medicinales, ornamentales; crianzas de animales silvestres en ambiente natural y otros. Las otorga la autoridad competente en atención a la ubicación y características de los recursos a ser aprovechados, de acuerdo a las condiciones que establece el reglamento. Es un acto administrativo que constituye título habilitante.',
    tipoEstilo: 'poligono',
    estilos: {
      fillColor: '#ffffff',
      color: '#a80084',
      weight: 1,
      fillOpacity: 0,
      opacity: 1,
      lineJoin: 'bevel',
    },
  },
  Con_ConcesionForFinMad: {
    nombre: 'Con_ConcesionForFinMad',
    titulo: 'Concesión forestal con fines maderables',
    descripcion:
      'Son las concesiones en unidades de aprovechamiento de 5,000 hasta 40,000 ha, por el plazo hasta de 40 años renovables, a favor de medianos y pequeños empresarios (en forma individual u organizados en sociedades u otras modalidades empresariales). Es un acto administrativo que constituye título habilitante.',
    tipoEstilo: 'poligono',
    estilos: {
      fillColor: '#ffffff',
      color: '#737300',
      weight: 1,
      fillOpacity: 0,
      opacity: 1,
      lineJoin: 'bevel',
    },
  },
  Con_ConcesionForRef: {
    nombre: 'Con_ConcesionForRef',
    titulo: 'Concesión para forestación y/o reforestación',
    descripcion:
      'Son concesiones cuyo objetivo es realizar actividades de forestación y/o reforestación. Son concesiones consideradas como actividades de interés público y prioridad nacional, especialmente en tierras forestales sin cubierta boscosa y en tierras de protección o eriazas. Es un acto administrativo que constituye título habilitante. Fueron otorgadas en el marco de la derogada Ley Nº27308.',
    tipoEstilo: 'poligono',
    estilos: {
      fillColor: '#ffffff',
      color: '#8400a8',
      weight: 1,
      fillOpacity: 0,
      opacity: 1,
      lineJoin: 'bevel',
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
    typeName: nombreCapaGeografica,
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
