<template>
  <a-drawer
    :visible="estaAbiertoVentanaCapasInteroperables"
    :width="tamanioVentana"
    @close="cerrarVentana('CapasInteroperables')"
  >
    <span slot="title">
      <b>CAPAS INTEROPERABLES</b>
    </span>
    <a-space direction="vertical" style="width: 100%">
      <a-alert type="error">
        <span slot="message">
          <b>Funcionalidad en desarrollo</b>
        </span>
        <span slot="description">
          El comportamiento y la información mostrada por esta funcionalidad se
          encuentran en proceso de desarrollo/pruebas, por lo que pueden
          presentarse errores.
        </span>
      </a-alert>
    </a-space>
  </a-drawer>
</template>

<script>
import { mapState, mapActions } from 'vuex';
export default {
  computed: {
    ...mapState(['tamanioVentana']),
    ...mapState('visor', ['estaAbiertoVentanaCapasInteroperables']),
  },
  methods: {
    ...mapActions('visor', ['cerrarVentana']),
  },
};
</script>
