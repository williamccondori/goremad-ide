<template>
  <PortalPagina>
    <a-alert
      message="¡Bienvenido a la Infraestructura de Datos Espaciales del Gobierno Regional de Madre de Dios!"
      description="En esta página podrás encontrar información geográfica de la región, así como también información de los servicios que ofrece el Gobierno Regional de Madre de Dios."
      type="success"
      show-icon
    />
  </PortalPagina>
</template>

<script>
import PortalPagina from "@/components/portal/compartido/PortalPagina.vue";
export default {
  components: {
    PortalPagina,
  },
  auth: false,
  methods: {},
};
</script>
