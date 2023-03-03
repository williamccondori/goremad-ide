<template>
  <AdministracionPagina titulo="Capas base">
    <ASpace direction="vertical" class="app--w-100">
      <AButton
        type="primary"
        icon="plus"
        @click="abrirCapaBaseFormularioVentana()"
      >
        Crear capa base
      </AButton>
      <CapaBaseCatalogo />
    </ASpace>
    <CapaBaseFormularioVentana />
  </AdministracionPagina>
</template>

<script>
import { Button, Space } from "ant-design-vue";
import { mapActions } from "vuex";
import AdministracionPagina from "@/components/administrador/compartido/AdministracionPagina.vue";
import CapaBaseCatalogo from "@/components/administrador/capa-base/CapaBaseCatalogo.vue";
import CapaBaseFormularioVentana from "@/components/administrador/capa-base/CapaBaseFormularioVentana.vue";
export default {
  components: {
    AButton: Button,
    ASpace: Space,
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
