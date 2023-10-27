export default {
    methods: {
        $obtenerParametrosConsulta(mapa, latitudLongitud) {
            const zoomActual = mapa.getZoom();
            const tamanioMapa = mapa.getSize();
            const cuadroDelimitador = mapa.getBounds();
            const puntoConsulta = mapa.latLngToContainerPoint(
                latitudLongitud,
                zoomActual
            );
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
