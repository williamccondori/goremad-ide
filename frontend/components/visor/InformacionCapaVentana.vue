<template>
  <a-drawer
    width="25rem"
    placement="bottom"
    :title="null"
    :destroy-on-close="true"
    :visible="estaAbiertoInformacionCapaVentana"
    @close="cerrarInformacionCapaVentana()"
  >
    <br />
    <a-alert type="warning" show-icon>
      <span slot="message">Advertencia</span>
      <span slot="description"> Caracaterística en desarrollo </span>
    </a-alert>
  </a-drawer>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  computed: {
    ...mapState("visor", ["estaAbiertoInformacionCapaVentana"]),
  },
  methods: {
    ...mapActions("visor", ["cerrarInformacionCapaVentana"]),
  },
};
</script>
