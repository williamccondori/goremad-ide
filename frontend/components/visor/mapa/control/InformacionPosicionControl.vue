<template>
  <LControl position="bottomright">
    <div v-if="informacionPosicion">
      <a-tag color="green" class="informacion-posicion">
        <i class="bx bxs-map" />
        {{ informacionPosicion.latitud }},
        {{ informacionPosicion.longitud }}
      </a-tag>
      <a-tag color="green" class="informacion-posicion">
        <i class="bx bx-search" />
        {{ informacionPosicion.zoom }}
      </a-tag>
    </div>
  </LControl>
</template>

<script>
import { mapState } from "vuex";
import { LControl } from "vue2-leaflet";
export default {
  components: {
    LControl,
  },
  computed: {
    ...mapState("visor", ["informacionPosicion"]),
  },
};
</script>

<style scoped>
.informacion-posicion {
  border-radius: 0;
}
</style>
