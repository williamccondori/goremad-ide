<template>
  <LControl
    style="
      background-color: rgba(255, 255, 255, 0.55);
      border-radius: 1rem;
      padding: 0.25rem;
    "
  >
    <a-button
      shape="circle"
      title="Capas"
      type="primary"
      @click="abrirVentana('CapasOperables')"
    >
      <i class="bx bx-layer" />
    </a-button>
    <a-button
      shape="circle"
      title="Capas interoperables"
      type="primary"
      @click="abrirVentana('CapasInteroperables')"
    >
      <i class="bx bx-globe" />
    </a-button>
    <a-button
      shape="circle"
      title="Información de las capas"
      type="primary"
      @click="abrirVentana('InformacionCapasOperables')"
    >
      <i class="bx bx-table" />
    </a-button>
    <a-button
      shape="circle"
      title="Buscar"
      type="primary"
      @click="abrirVentana('Buscar')"
    >
      <i class="bx bx-map" />
    </a-button>
    <a-button
      shape="circle"
      title="Descargar información"
      type="primary"
      @click="abrirVentana('DescargarInformacion')"
    >
      <i class="bx bx-download" />
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
