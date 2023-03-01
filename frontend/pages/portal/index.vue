<template>
  <PortalPagina>
    <AAlert
      message="¡Bienvenido a la Infraestructura de Datos Espaciales del Gobierno Regional de Madre de Dios!"
      description="En esta página podrás encontrar información geográfica de la región, así como también información de los servicios que ofrece el Gobierno Regional de Madre de Dios."
      type="success"
    />
  </PortalPagina>
</template>

<script>
import { Alert } from "ant-design-vue";
import PortalPagina from "@/components/portal/compartido/PortalPagina.vue";
export default {
  components: {
    AAlert: Alert,
    PortalPagina,
  },
  auth: false,
  layout: "portal",
  methods: {},
};
</script>
