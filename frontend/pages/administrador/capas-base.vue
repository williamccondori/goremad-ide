<template>
  <AdministracionPagina titulo="Capas base">
    <a-space direction="vertical" class="app--w-100">
      <a-button
        type="primary"
        icon="plus"
        @click="abrirCapaBaseFormularioVentana()"
      >
        Crear capa base
      </a-button>
      <CapaBaseCatalogo />
    </a-space>
    <CapaBaseFormularioVentana />
  </AdministracionPagina>
</template>

<script>
import { mapActions } from "vuex";
import AdministracionPagina from "@/components/administrador/compartido/AdministracionPagina.vue";
import CapaBaseCatalogo from "@/components/administrador/capa-base/CapaBaseCatalogo.vue";
import CapaBaseFormularioVentana from "@/components/administrador/capa-base/CapaBaseFormularioVentana.vue";
export default {
  components: {
    AdministracionPagina,
    CapaBaseCatalogo,
    CapaBaseFormularioVentana,
  },
  layout: "administrador",
  methods: {
    ...mapActions("administrador", ["abrirCapaBaseFormularioVentana"]),
  },
};
</script>
