<template>
  <LControl>
    <div class="utilidades-control">
      <AButton
        title="Marcadores"
        type="dashed"
        @click="abrirMarcadorCatalogoVentana()"
      >
        <i class="bx bx-pin" />
      </AButton>
      <AButton
        title="Compartir"
        type="dashed"
        @click="abrirCompartirVistaModal()"
      >
        <i class="bx bx-share-alt" />
      </AButton>
      <AButton
        title="Comparar capas activas"
        type="dashed"
        @click="abrirComparacionVentana()"
      >
        <i class="bx bx-bracket" />
      </AButton>
    </div>
  </LControl>
</template>

<script>
import { Button } from 'ant-design-vue';
import { mapActions } from 'vuex';
import { LControl } from 'vue2-leaflet';
export default {
  components: {
    AButton: Button,
    LControl,
  },
  methods: {
    ...mapActions('visor', [
      'abrirUbicacionVentana',
      'abrirCoordenadaVentana',
      'abrirDibujoVentana',
      'abrirMarcadorCatalogoVentana',
      'abrirCompartirVistaModal',
      'abrirComparacionVentana',
    ]),
  },
};
</script>

<style scoped>
.utilidades-control {
  padding: 0.25rem;
  background-color: rgba(255, 255, 255, 0.55);
}
</style>
