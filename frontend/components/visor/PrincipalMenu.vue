<template>
  <div class="app--contenedor-vertical-pequenio menu">
    <CapaColapsable />
    <InteroperabilidadColapsable />
    <SubirArchivoColapsable />
    <DescargarArchivoColapsable />
    <h1 class="menu-titulo">Análisis de datos</h1>
    <InformacionColapsable />
  </div>
</template>

<script>
import CapaColapsable from "@/components/visor/CapaColapsable.vue";
import InteroperabilidadColapsable from "@/components/visor/InteroperabilidadColapsable.vue";
import SubirArchivoColapsable from "@/components/visor/SubirArchivoColapsable.vue";
import DescargarArchivoColapsable from "@/components/visor/DescargarArchivoColapsable.vue";
import InformacionColapsable from "@/components/visor/InformacionColapsable.vue";
export default {
  components: {
    CapaColapsable,
    InteroperabilidadColapsable,
    SubirArchivoColapsable,
    DescargarArchivoColapsable,
    InformacionColapsable,
  },
  props: {
    configuracionInicial: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.menu {
  width: 25rem;
  padding: 1rem;
  overflow-y: scroll;
}
.menu-titulo {
  color: green;
  margin-bottom: 0;
  font-weight: bold;
}
</style>
