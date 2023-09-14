<template>
  <div>
    <LGeoJson
      v-for="capaGEOJSON in capasGEOJSON"
      :key="capaGEOJSON.id"
      :geojson="capaGEOJSON.geojson"
      :options="{
        style: capaGEOJSON.estilos,
        onEachFeature: (feature, layer) =>
          onEachFeature(capaGEOJSON.estilos, feature, layer),
      }"
    />
  </div>
</template>

<script>
import { mapState } from 'vuex';
import { LGeoJson } from 'vue2-leaflet';

export default {
  components: {
    LGeoJson,
  },
  data() {
    return {
      layerOptions: {
        onEachFeature: this.onEachFeature,
      },
    };
  },
  computed: {
    ...mapState('visor', ['capasGEOJSON']),
  },
  methods: {
    onEachFeature(estilosPorDefecto, feature, layer) {
      // Aplicar estilos iniciales.
      layer.setStyle(estilosPorDefecto);

      // Configurar eventos del ratón.
      layer.on({
        mouseover: this.highlightFeature,
        mouseout: (e) => this.resetHighlight(e, estilosPorDefecto),
      });
    },
    highlightFeature(e) {
      const layer = e.target;

      layer.setStyle({
        color: '#00FFFF',
        fillColor: '#FFFFFF',
        fillOpacity: 0.5,
        lineJoin: 'bevel',
        opacity: 1,
        weight: 3,
      });
    },
    resetHighlight(e, estilosPorDefecto) {
      const layer = e.target;

      // Restablecer a los estilos por defecto
      layer.setStyle(estilosPorDefecto);
    },
  },
};
</script>
