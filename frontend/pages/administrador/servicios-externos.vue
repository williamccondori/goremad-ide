<template>
  <AdministracionPagina titulo="Servicios externos">
    <a-space direction="vertical" class="app--w-100">
      <a-button
        type="primary"
        icon="plus"
        @click="abrirServicioExternoFormularioVentana()"
      >
        Crear servicio externo
      </a-button>
      <ServicioExternoCatalogo />
    </a-space>
    <ServicioExternoFormularioVentana />
  </AdministracionPagina>
</template>

<script>
import { mapActions } from "vuex";
import AdministracionPagina from "@/components/administrador/compartido/AdministracionPagina.vue";
import ServicioExternoCatalogo from "@/components/administrador/servicio-externo/ServicioExternoCatalogo.vue";
import ServicioExternoFormularioVentana from "@/components/administrador/servicio-externo/ServicioExternoFormularioVentana.vue";
export default {
  components: {
    AdministracionPagina,
    ServicioExternoCatalogo,
    ServicioExternoFormularioVentana,
  },
  layout: "administrador",
  methods: {
    ...mapActions("administrador", ["abrirServicioExternoFormularioVentana"]),
  },
};
</script>
