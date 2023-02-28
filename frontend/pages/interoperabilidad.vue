<template>
  <PortalPagina titulo="Interoperabilidad">
    <AAlert
      message="Página en construcción"
      description="Esta página está en construcción. Pronto estará disponible."
      type="warning"
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
