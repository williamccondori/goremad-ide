<template>
  <a-drawer
    width="25rem"
    placement="left"
    :visible="estaAbiertoDibujoVentana"
    @close="cerrarDibujoVentana()"
  >
    <span slot="title">
      <b>Dibujos</b>
    </span>
    <a-alert
      message="Característica en construcción"
      description="Esta característica está en construcción. Pronto estará disponible."
      type="warning"
      show-icon
    />
  </a-drawer>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  computed: {
    ...mapState("visor", ["estaAbiertoDibujoVentana"]),
  },
  methods: {
    ...mapActions("visor", ["cerrarDibujoVentana"]),
  },
};
</script>
