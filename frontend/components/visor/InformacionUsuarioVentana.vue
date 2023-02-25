<template>
  <a-drawer
    width="25rem"
    :destroy-on-close="true"
    :visible="estaAbiertoInformacionUsuarioVentana"
    @close="cerrarInformacionUsuarioVentana()"
  >
    <span slot="title">
      <b>Información del usuario</b>
    </span>
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
    ...mapState("visor", ["estaAbiertoInformacionUsuarioVentana"]),
  },
  methods: {
    ...mapActions("visor", ["cerrarInformacionUsuarioVentana"]),
  },
};
</script>
