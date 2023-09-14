<template>
  <LControl>
    <div class="herramientas-control">
      <a-button title="Capas" type="dashed" @click="abrirCapaCatalogoVentana()">
        <i class="bx bx-layer" />
      </a-button>
      <a-button
        title="Leyenda"
        type="dashed"
        @click="abrirCapaResumenVentana()"
      >
        <i class="bx bx-label" />
      </a-button>
      <a-button
        title="Capas base"
        type="dashed"
        @click="abrirCapaBaseCatalogoVentana()"
      >
        <i class="bx bx-map-alt" />
      </a-button>
      <a-button
        title="Interoperabilidad"
        type="dashed"
        @click="abrirWebMapServiceFormularioVentana()"
      >
        <i class="bx bx-globe" />
      </a-button>
      <a-button title="Subir información" type="dashed">
        <i class="bx bx-upload" />
      </a-button>
      <a-button title="Descargar información" type="dashed">
        <i class="bx bx-download" />
      </a-button>
      <a-button
        title="Imágenes satelitales"
        type="dashed"
        @click="abrirImagenSatelitalCatalogoVentana()"
      >
        <i class="bx bx-images" />
      </a-button>
      <a-button title="Portal" type="primary" @click="abrirPortalInformacion()">
        <i class="bx bx-book" />
      </a-button>
    </div>
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
      'abrirCapaCatalogoVentana',
      'abrirCapaResumenVentana',
      'abrirCapaBaseCatalogoVentana',
      'abrirWebMapServiceFormularioVentana',
      'abrirImagenSatelitalCatalogoVentana',
    ]),
    abrirPortalInformacion() {
      this.$router.push('/portal');
    },
  },
};
</script>

<style scoped>
.herramientas-control {
  padding: 0.25rem;
  background-color: rgba(255, 255, 255, 0.55);
}
</style>
