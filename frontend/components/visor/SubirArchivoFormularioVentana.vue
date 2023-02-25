<template>
  <a-drawer
    width="25rem"
    :destroy-on-close="true"
    :visible="estaAbiertoSubirArchivoFormularioVentana"
    @close="cerrarSubirArchivoFormularioVentana()"
  >
    <span slot="title">
      <b>Cargar información</b>
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
    ...mapState("visor", ["estaAbiertoSubirArchivoFormularioVentana"]),
  },
  methods: {
    ...mapActions("visor", ["cerrarSubirArchivoFormularioVentana"]),
  },
};
</script>
