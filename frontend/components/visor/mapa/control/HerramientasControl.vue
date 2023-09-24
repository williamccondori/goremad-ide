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
      title="Mapas base"
      type="primary"
      @click="abrirCapaBaseCatalogoVentana()"
    >
      <i class="bx bx-map-alt" />
    </a-button>
    <a-button
      shape="circle"
      title="Leyenda"
      type="primary"
      @click="abrirCapaResumenVentana()"
    >
      <i class="bx bx-label" />
    </a-button>
    <a-button
      shape="circle"
      title="Compartir"
      type="primary"
      @click="abrirCompartirVistaModal()"
    >
      <i class="bx bx-share-alt" />
    </a-button>
    <a-button
      shape="circle"
      title="Imágenes satelitales"
      type="primary"
      @click="abrirImagenSatelitalCatalogoVentana()"
    >
      <i class="bx bx-images" />
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
    ...mapActions('visor', [
      'abrirCompartirVistaModal',
      'abrirCapaCatalogoVentana',
      'abrirCapaResumenVentana',
      'abrirCapaBaseCatalogoVentana',
      'abrirWebMapServiceFormularioVentana',
      'abrirImagenSatelitalCatalogoVentana',
    ]),
  },
};
</script>
