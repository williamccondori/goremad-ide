<template>
  <LLayerGroup>
    <LTileLayer
      v-for="elemento in elementosActivos"
      :key="elemento.id"
      :attribution="elemento.atribucion"
      layer-type="base"
      :name="elemento.nombre"
      :url="elemento.url"
      :visible="true"
      :z-index="0"
    />
  </LLayerGroup>
</template>

<script>
import { mapState } from 'vuex';
import { LLayerGroup, LTileLayer } from 'vue2-leaflet';
export default {
  components: {
    LLayerGroup,
    LTileLayer,
  },
  computed: {
    ...mapState('visor', ['capaBaseActiva', 'capasBase']),
    elementosActivos() {
      return this.capasBase.filter(
        (elemento) => elemento.id === this.capaBaseActiva
      );
    },
  },
};
</script>
