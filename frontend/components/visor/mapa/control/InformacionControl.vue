<template>
  <LControl position="topleft">
    <a-button
      title="Capas"
      type="dashed"
      @click="abrirVentana('CapasOperables')"
    >
      <i class="bx bx-layer" />
    </a-button>
    <a-button
      title="Capas interoperables"
      type="dashed"
      @click="abrirVentana('CapasInteroperables')"
    >
      <i class="bx bx-globe" />
    </a-button>
    <a-button
      title="Información de las capas"
      type="dashed"
      @click="abrirVentana('InformacionCapasOperables')"
    >
      <i class="bx bx-table" />
    </a-button>
  </LControl>
</template>

<script>
import { mapActions } from 'vuex';
import { LControl } from 'vue2-leaflet';
export default {
  components: {
    LControl,
  },
  methods: {
    ...mapActions('visor', ['abrirVentana']),
  },
};
</script>
