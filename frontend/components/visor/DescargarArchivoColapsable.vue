<template>
  <BaseColapsable title="Descarga de información" icon="globe">
    <a-button
      html-type="button"
      type="dashed"
      block
      @click="abrirDescargarArchivoVentana()"
    >
      Descargar información
    </a-button>
    <DescargarArchivoVentana />
  </BaseColapsable>
</template>

<script>
import { mapActions } from "vuex";
import BaseColapsable from "@/components/visor/BaseColapsable.vue";
import DescargarArchivoVentana from "@/components/visor/DescargarArchivoVentana.vue";
export default {
  components: { BaseColapsable, DescargarArchivoVentana },
  methods: {
    ...mapActions("visor", ["abrirDescargarArchivoVentana"]),
  },
};
</script>
