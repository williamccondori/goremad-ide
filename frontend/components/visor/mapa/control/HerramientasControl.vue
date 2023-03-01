<template>
  <LControl>
    <div class="herramientas-control">
      <AButton type="dashed" title="Capas" @click="abrirCapaCatalogoVentana()">
        <i class="bx bx-layer" />
      </AButton>
      <AButton type="dashed" title="Leyenda" @click="abrirCapaResumenVentana()">
        <i class="bx bx-label" />
      </AButton>
      <AButton
        type="dashed"
        title="Capas base"
        @click="abrirCapaBaseCatalogoVentana()"
      >
        <i class="bx bx-map-alt" />
      </AButton>
      <AButton
        type="dashed"
        title="Interoperabilidad"
        @click="abrirWebMapServiceFormularioVentana()"
      >
        <i class="bx bx-globe" />
      </AButton>
      <AButton type="dashed" title="Subir información">
        <i class="bx bx-upload" />
      </AButton>
      <AButton type="dashed" title="Descargar información">
        <i class="bx bx-download" />
      </AButton>
      <AButton type="primary" title="Portal" @click="abrirPortalInformacion()">
        <i class="bx bx-book" />
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
      "abrirCapaCatalogoVentana",
      "abrirCapaResumenVentana",
      "abrirCapaBaseCatalogoVentana",
      "abrirWebMapServiceFormularioVentana",
    ]),
    abrirPortalInformacion() {
      this.$router.push("/portal");
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
