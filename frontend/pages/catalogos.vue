<template>
  <PortalPagina titulo="Catálogos">
    <a-alert
      message="Página en construcción"
      description="Esta página está en construcción. Pronto estará disponible."
      type="warning"
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
