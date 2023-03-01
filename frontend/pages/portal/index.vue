<template>
  <PortalPagina>
    <AAlert
      message="¡Bienvenido a la Infraestructura de Datos Espaciales del Gobierno Regional de Madre de Dios!"
      description="En esta página podrás encontrar información geográfica de la región, así como también información de los servicios que ofrece el Gobierno Regional de Madre de Dios."
      type="success"
    />
    <AButton @click="irCatalogoMetadatos()"> Catálogo de Metadatos </AButton>
    <AButton @click="irSistemaCentrosPoblados()">
      Sistema de Categorización de Centros Poblados
    </AButton>
  </PortalPagina>
</template>

<script>
import { Alert, Button } from "ant-design-vue";
import PortalPagina from "@/components/portal/compartido/PortalPagina.vue";
export default {
  components: {
    AAlert: Alert,
    AButton: Button,
    PortalPagina,
  },
  auth: false,
  layout: "portal",
  methods: {
    irCatalogoMetadatos() {
      window.open(
        "https://metadatos.ide.regionmadrededios.gob.pe/geonetwork",
        "_blank"
      );
    },
    irSistemaCentrosPoblados() {
      window.open("https://centrospoblados.regionmadrededios.gob.pe", "_blank");
    },
  },
};
</script>
