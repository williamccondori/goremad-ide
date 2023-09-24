<template>
  <a-drawer
    :height="500"
    placement="bottom"
    :visible="estaAbiertoVentanaResultadoInformacionCapasOperables"
    @close="cerrarVentana('ResultadoInformacionCapasOperables')"
  >
    <span slot="title">
      <b>INFORMACIÓN DE LA CAPA: {{ registroObjetoGeografico?.nombre }}</b>
    </span>
    <a-space direction="vertical" style="width: 100%">
      <a-input
        v-model="cadenaBusqueda"
        placeholder="Buscar (a partir del tercer caracter)..."
      />
      <div>
        <a-table
          v-if="registroObjetoGeografico"
          bordered
          :columns="registroObjetoGeografico.columnas"
          :data-source="registrosFiltrados"
          row-key="id"
          size="small"
        />
      </div>
    </a-space>
  </a-drawer>
</template>

<script>
import { mapState, mapActions } from 'vuex';
export default {
  data() {
    return {
      cadenaBusqueda: '',
    };
  },
  computed: {
    ...mapState('visor', [
      'estaAbiertoVentanaResultadoInformacionCapasOperables',
      'registroObjetoGeografico',
    ]),
    registrosFiltrados() {
      if (!this.cadenaBusqueda || this.cadenaBusqueda.length <= 3) {
        return this.registroObjetoGeografico.registros;
      }
      const query = this.cadenaBusqueda.toLowerCase();
      return this.registroObjetoGeografico.registros.filter((row) =>
        Object.values(row).some((value) =>
          String(value).toLowerCase().includes(query)
        )
      );
    },
  },
  methods: {
    ...mapActions('visor', ['cerrarVentana']),
  },
};
</script>
