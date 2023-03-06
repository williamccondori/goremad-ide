<template>
  <LControl>
    <div class="utilidades-control">
      <AButton
        type="dashed"
        title="Búsqueda de ubicaciones"
        @click="abrirUbicacionVentana()"
      >
        <i class="bx bx-search" />
      </AButton>
      <AButton
        type="dashed"
        title="Búsqueda de coordenadas"
        @click="abrirCoordenadaVentana()"
      >
        <i class="bx bx-map-pin" />
      </AButton>
      <AButton type="dashed" title="Dibujos" @click="abrirDibujoVentana()">
        <i class="bx bx-palette" />
      </AButton>
      <AButton
        type="dashed"
        title="Marcadores"
        @click="abrirMarcadorCatalogoVentana()"
      >
        <i class="bx bx-pin" />
      </AButton>
      <AButton
        type="dashed"
        title="Compartir"
        @click="abrirCompartirVistaModal()"
      >
        <i class="bx bx-share-alt" />
      </AButton>
      <AButton
        type="dashed"
        title="Comparar capas activas"
        @click="abrirComparacionVentana()"
      >
        <i class="bx bx-bracket" />
      </AButton>
    </div>
  </LControl>
</template>

<script>
import { Button } from "ant-design-vue";
import { mapActions } from "vuex";
import { LControl } from "vue2-leaflet";
export default {
  components: {
    AButton: Button,
    LControl,
  },
  methods: {
    ...mapActions("visor", [
      "abrirUbicacionVentana",
      "abrirCoordenadaVentana",
      "abrirDibujoVentana",
      "abrirMarcadorCatalogoVentana",
      "abrirCompartirVistaModal",
      "abrirComparacionVentana",
    ]),
  },
};
</script>

<style scoped>
.utilidades-control {
  padding: 0.25rem;
  background-color: rgba(255, 255, 255, 0.55);
}
</style>
