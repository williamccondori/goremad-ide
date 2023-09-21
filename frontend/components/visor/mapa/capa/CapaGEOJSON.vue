<template>
  <div>
    <LGeoJson
      v-for="capaOperativa in capasOperativas"
      :key="capaOperativa.id"
      :geojson="capaOperativa.geometria"
      :options="{
        style: capaOperativa.estilo,
        onEachFeature: (feature, layer) =>
          onEachFeature(capaOperativa.estilo, feature, layer),
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
    ...mapState('visor', ['capasOperativas']),
  },
  methods: {
    onEachFeature(estilosPorDefecto, feature, layer) {
      layer.setStyle(estilosPorDefecto);
      layer.on({
        mouseover: this.resaltarPoligono,
        mouseout: (e) => this.reestablecerPoligono(e, estilosPorDefecto),
      });
    },
    resaltarPoligono(e) {
      const capa = e.target;
      capa.setStyle({
        color: '#00FFFF',
        fillColor: '#FFFFFF',
        fillOpacity: 0.5,
        lineJoin: 'bevel',
        opacity: 1,
        weight: 3,
      });
    },
    reestablecerPoligono(e, estilosPorDefecto) {
      const capa = e.target;
      capa.setStyle(estilosPorDefecto);
    },
  },
};
</script>
