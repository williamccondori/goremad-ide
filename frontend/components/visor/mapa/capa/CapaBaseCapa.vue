<template>
  <div>
    <LTileLayer
      v-for="elemento in elementosActivos"
      :key="elemento.id"
      :attribution="elemento.atribucion"
      :name="elemento.nombre"
      :url="elemento.url"
      :visible="true"
      :z-index="0"
      layer-type="base"
    />
  </div>
</template>

<script>
import { mapState } from "vuex";
import { LTileLayer } from "vue2-leaflet";
export default {
  components: {
    LTileLayer,
  },
  computed: {
    ...mapState("visor", ["capaBaseActiva", "capasBase"]),
    elementosActivos() {
      return this.capasBase.filter(
        (elemento) => elemento.id === this.capaBaseActiva
      );
    },
  },
};
</script>
