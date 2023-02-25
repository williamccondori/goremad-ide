<template>
  <PortalPagina titulo="Visor GEOGOREMAD">
    <a-button type="primary" @click="() => $router.push('/geogoremad')">
      Ingresar al <b style="margin-left: 0.5rem">GEOGOREMAD</b>
    </a-button>
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
