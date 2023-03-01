<template>
  <PortalPagina titulo="Visor GEOGOREMAD">
    <NuxtLink to="/geogoremad">
      Ingresar al <b style="color: orange">GEOGOREMAD</b>
    </NuxtLink>
  </PortalPagina>
</template>

<script>
import PortalPagina from "@/components/portal/compartido/PortalPagina.vue";
export default {
  components: {
    PortalPagina,
  },
  auth: false,
  layout: "portal",
  methods: {},
};
</script>
