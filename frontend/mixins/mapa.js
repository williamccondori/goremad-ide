export default {
  methods: {
    /**
     * Obtiene los parametros de consulta para el servicio de busqueda de direcciones.
     * @param {Object} mapa - Objeto del mapa.
     * @param {Object} latitudLongitud - Objeto con las coordenadas de latitud y longitud.
     * @returns {Object} - Objeto con los parametros de consulta.
     */
    $obtenerParametrosConsulta(mapa, latitudLongitud) {
      // Se obtienen la información del mapa.
      const zoomActual = mapa.getZoom();
      const tamanioMapa = mapa.getSize();
      const cuadroDelimitador = mapa.getBounds();
      const puntoConsulta = mapa.latLngToContainerPoint(
        latitudLongitud,
        zoomActual
      );
      // Se obtienen los parámetros de consulta.
      return {
        width: tamanioMapa.x,
        height: tamanioMapa.y,
        x: Math.round(puntoConsulta.x),
        y: Math.round(puntoConsulta.y),
        boundingBox: cuadroDelimitador.toBBoxString(),
        url: this.url,
        layers: undefined,
      };
    },
  },
};
