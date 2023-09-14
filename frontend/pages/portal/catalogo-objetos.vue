<template>
  <PortalPagina titulo="Catálogo de objetos">
    <AAlert
      description="Esta página está en construcción. Pronto estará disponible."
      message="Página en construcción"
      type="warning"
    />
  </PortalPagina>
</template>

<script>
import { Alert } from 'ant-design-vue';
import PortalPagina from '@/components/portal/compartido/PortalPagina.vue';
export default {
  components: {
    AAlert: Alert,
    PortalPagina,
  },
  auth: false,
  layout: 'portal',
  methods: {},
};
</script>
