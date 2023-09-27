<template>
  <LControl
    style="
      background-color: rgba(255, 255, 255, 0.55);
      border-radius: 0.25rem;
      padding: 0.25rem;
    "
  >
    <a-collapse expand-icon-position="right">
      <a-collapse-panel>
        <span slot="header">
          <b style="display: flex; align-items: center; gap: 0.25rem">
            📚 Información &nbsp;&nbsp;
          </b>
        </span>
        <a-tooltip placement="left" title="Capas">
          <a-button
            shape="circle"
            type="primary"
            @click="abrirVentana('CapasOperables')"
          >
            <i class="bx bx-layer" />
          </a-button>
        </a-tooltip>
        <a-tooltip placement="left" title="Capas interoperables">
          <a-button
            shape="circle"
            type="primary"
            @click="abrirVentana('CapasInteroperables')"
          >
            <i class="bx bx-globe" />
          </a-button>
        </a-tooltip>
        <a-tooltip placement="left" title="Información de las capas">
          <a-button
            shape="circle"
            type="primary"
            @click="abrirVentana('InformacionCapasOperables')"
          >
            <i class="bx bx-table" />
          </a-button>
        </a-tooltip>
        <a-tooltip placement="left" title="Buscar">
          <a-button
            shape="circle"
            type="primary"
            @click="abrirVentana('Buscar')"
          >
            <i class="bx bx-search" />
          </a-button>
        </a-tooltip>
        <a-tooltip placement="left" title="Subir información">
          <a-button
            shape="circle"
            type="primary"
            @click="abrirVentana('SubirInformacion')"
          >
            <i class="bx bx-upload" />
          </a-button>
        </a-tooltip>
        <a-tooltip placement="left" title="Descargar información">
          <a-button
            shape="circle"
            type="primary"
            @click="abrirVentana('DescargarInformacion')"
          >
            <i class="bx bx-download" />
          </a-button>
        </a-tooltip>
      </a-collapse-panel>
    </a-collapse>
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
