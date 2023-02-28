<template>
  <LControl>
    <div class="herramientas-control">
      <a-button-group size="large">
        <a-button type="dashed" title="Capas" @click="abrirCapaVentana()">
          <i class="bx bx-layer" />
        </a-button>
        <a-button type="dashed" title="Leyenda">
          <i class="bx bx-label" />
        </a-button>
        <a-button
          type="dashed"
          title="Capas base"
          @click="abrirCapaBaseVentana()"
        >
          <i class="bx bx-map-alt" />
        </a-button>
        <a-button
          type="dashed"
          title="Interoperabilidad"
          @click="abrirWebMapServiceFormularioVentana()"
        >
          <i class="bx bx-globe" />
        </a-button>
        <a-button type="dashed" title="Subir información">
          <i class="bx bx-upload" />
        </a-button>
        <a-button type="dashed" title="Descargar información">
          <i class="bx bx-download" />
        </a-button>
      </a-button-group>
    </div>
    <CapaBaseVentana />
    <WebMapServiceFormularioVentana />
  </LControl>
</template>

<script>
import { mapActions } from "vuex";
import { LControl } from "vue2-leaflet";
import CapaBaseVentana from "@/components/visor/CapaBaseVentana.vue";
// import WebMapServiceFormularioVentana from "@/components/visor/WebMapServiceFormularioVentana.vue";
export default {
  components: {
    LControl,
    CapaBaseVentana,
    // WebMapServiceFormularioVentana,
  },
  methods: {
    ...mapActions("visor", [
      "abrirCapaVentana",
      "abrirCapaBaseVentana",
      "abrirWebMapServiceFormularioVentana",
    ]),
  },
};
</script>

<style scoped>
.herramientas-control {
  padding: 0.25rem;
  background-color: rgba(255, 255, 255, 0.55);
}
</style>
