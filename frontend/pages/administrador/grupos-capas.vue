<template>
  <AdministracionPagina titulo="Grupo de capas">
    <GrupoCapaCatalogo />
  </AdministracionPagina>
</template>

<script>
import AdministracionPagina from "@/components/administrador/compartido/AdministracionPagina.vue";
import GrupoCapaCatalogo from "@/components/administrador/grupo-capa/GrupoCapaCatalogo.vue";
export default {
  components: {
    AdministracionPagina,
    GrupoCapaCatalogo,
  },
  layout: "administrador",
};
</script>
