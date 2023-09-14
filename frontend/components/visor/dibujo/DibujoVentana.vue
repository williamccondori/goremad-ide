<template>
  <ADrawer
    placement="left"
    :visible="estaAbiertoDibujoVentana"
    :width="esMovil ? '100%' : 400"
    @close="cerrarDibujoVentana()"
  >
    <span slot="title" style="text-transform: uppercase">
      <b>Dibujos</b>
    </span>
    <AAlert
      description="Esta característica está en construcción. Pronto estará disponible."
      message="Característica en construcción"
      type="warning"
    />
  </ADrawer>
</template>

<script>
import { Drawer, Alert } from 'ant-design-vue';
import { mapState, mapActions } from 'vuex';
export default {
  components: {
    ADrawer: Drawer,
    AAlert: Alert,
  },
  computed: {
    ...mapState(['esMovil']),
    ...mapState('visor', ['estaAbiertoDibujoVentana']),
  },
  methods: {
    ...mapActions('visor', ['cerrarDibujoVentana']),
  },
};
</script>
