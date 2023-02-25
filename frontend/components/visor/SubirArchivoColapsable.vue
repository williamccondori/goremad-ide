<template>
  <BaseColapsable title="Carga de información" icon="upload">
    <a-button
      html-type="button"
      type="dashed"
      block
      @click="abrirSubirArchivoFormularioVentana()"
    >
      Cargar información
    </a-button>
    <a-divider />
    <a-button
      html-type="button"
      type="dashed"
      block
      @click="abrirSubirArchivoVentana()"
    >
      Información cargada
    </a-button>
    <SubirArchivoFormularioVentana />
    <SubirArchivoVentana />
  </BaseColapsable>
</template>

<script>
import { mapActions } from "vuex";
import BaseColapsable from "@/components/visor/BaseColapsable.vue";
import SubirArchivoFormularioVentana from "@/components/visor/SubirArchivoFormularioVentana.vue";
import SubirArchivoVentana from "@/components/visor/SubirArchivoVentana.vue";
export default {
  components: {
    BaseColapsable,
    SubirArchivoFormularioVentana,
    SubirArchivoVentana,
  },
  methods: {
    ...mapActions("visor", [
      "abrirSubirArchivoFormularioVentana",
      "abrirSubirArchivoVentana",
    ]),
  },
};
</script>
