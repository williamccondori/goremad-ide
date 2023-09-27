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
            🧰 Herramientas
          </b>
        </span>
        <a-tooltip placement="left" title="Mapas base">
          <a-button
            shape="circle"
            type="primary"
            @click="abrirCapaBaseCatalogoVentana()"
          >
            <div style="display: flex; align-items: center; gap: 0.25rem">
              <i class="bx bx-map-alt" />
            </div>
          </a-button>
        </a-tooltip>
        <a-tooltip placement="left" title="Marcadores">
          <a-button
            shape="circle"
            type="primary"
            @click="abrirMarcadorCatalogoVentana()"
          >
            <div style="display: flex; align-items: center; gap: 0.25rem">
              <i class="bx bx-pin" />
            </div>
          </a-button>
        </a-tooltip>
        <a-tooltip placement="left" title="Leyenda">
          <a-button
            shape="circle"
            title="Leyenda"
            type="primary"
            @click="abrirCapaResumenVentana()"
          >
            <i class="bx bx-label" />
          </a-button>
        </a-tooltip>
        <a-tooltip placement="left" title="Gráficos">
          <a-button
            shape="circle"
            type="primary"
            @click="abrirVentana('Graficos')"
          >
            <i class="bx bx-chart" />
          </a-button>
        </a-tooltip>
        <a-tooltip placement="left" title="Compartir">
          <a-button
            shape="circle"
            type="primary"
            @click="abrirCompartirVistaModal()"
          >
            <i class="bx bx-share-alt" />
          </a-button>
        </a-tooltip>
        <a-tooltip placement="left" title="Imágenes satelitales">
          <a-button
            shape="circle"
            type="primary"
            @click="abrirImagenSatelitalCatalogoVentana()"
          >
            <i class="bx bx-images" />
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
    ...mapActions('visor', [
      'abrirVentana',
      'abrirCompartirVistaModal',
      'abrirCapaCatalogoVentana',
      'abrirCapaResumenVentana',
      'abrirCapaBaseCatalogoVentana',
      'abrirMarcadorCatalogoVentana',
      'abrirWebMapServiceFormularioVentana',
      'abrirImagenSatelitalCatalogoVentana',
    ]),
  },
};
</script>
