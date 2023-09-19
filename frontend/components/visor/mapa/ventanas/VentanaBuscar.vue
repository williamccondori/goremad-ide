<template>
  <a-drawer
    :visible="estaAbiertoVentanaBuscar"
    :width="tamanioVentana"
    @close="cerrarVentana('Buscar')"
  >
    <span slot="title">
      <b>Buscar</b>
    </span>
    <a-space direction="vertical" style="width: 100%">
      <a-tabs default-active-key="buscarPorCriterio" type="card">
        <a-tab-pane key="buscarPorCriterio" tab="Buscar por criterio">
          Aquí se podrán buscar capas por criterio
        </a-tab-pane>
        <a-tab-pane key="buscarPorCoordenadas" tab="Buscar por coordenadas">
          Aquí de podrá descargar dibujos
        </a-tab-pane>
      </a-tabs>
    </a-space>
  </a-drawer>
</template>

<script>
import { mapState, mapActions } from 'vuex';
export default {
  data() {
    return {
      form: {
        tematica: undefined,
        capaGeografica: undefined,
        formato: undefined,
      },
      tematicas: [],
      formatos: [],
      gruposDiponibles: [],
    };
  },
  computed: {
    ...mapState(['tamanioVentana']),
    ...mapState('visor', ['estaAbiertoVentanaBuscar']),
  },
  methods: {
    ...mapActions('visor', ['cerrarVentana']),
  },
};
</script>
