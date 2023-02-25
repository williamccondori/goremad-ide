<template>
  <LControl position="bottomleft">
    <div class="utilidades-control">
      <a-button-group size="large">
        <a-button
          type="dashed"
          title="Búsqueda de ubicaciones"
          @click="abrirUbicacionVentana()"
        >
          <i class="bx bx-search" />
        </a-button>
        <a-button
          type="dashed"
          title="Búsqueda de coordenadas"
          @click="abrirCoordenadaVentana()"
        >
          <i class="bx bx-map-pin" />
        </a-button>
        <a-button type="dashed" title="Dibujos" @click="abrirDibujoVentana()">
          <i class="bx bx-palette" />
        </a-button>
        <a-button
          type="dashed"
          title="Marcadores"
          @click="abrirMarcadorVentana()"
        >
          <i class="bx bx-pin" />
        </a-button>
        <a-button
          type="dashed"
          title="Compartir"
          @click="abrirCompartirVistaModal()"
        >
          <i class="bx bx-share-alt" />
        </a-button>
      </a-button-group>
    </div>
    <UbicacionVentana />
    <CoordenadaVentana />
    <DibujoVentana />
    <MarcadorVentana />
    <CompartirModal />
  </LControl>
</template>

<script>
import { mapActions } from "vuex";
import { LControl } from "vue2-leaflet";
import UbicacionVentana from "@/components/visor/ubicacion/UbicacionVentana.vue";
import CoordenadaVentana from "@/components/visor/coordenada/CoordenadaVentana.vue";
import DibujoVentana from "@/components/visor/dibujo/DibujoVentana.vue";
import MarcadorVentana from "@/components/visor/marcador/MarcadorVentana.vue";
import CompartirModal from "@/components/visor/compartir/CompartirModal.vue";
export default {
  components: {
    LControl,
    UbicacionVentana,
    CoordenadaVentana,
    DibujoVentana,
    MarcadorVentana,
    CompartirModal,
  },
  methods: {
    ...mapActions("visor", [
      "abrirUbicacionVentana",
      "abrirCoordenadaVentana",
      "abrirDibujoVentana",
      "abrirMarcadorVentana",
      "abrirCompartirVistaModal",
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
