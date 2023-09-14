<template>
  <a-drawer
    :height="500"
    placement="bottom"
    :visible="estaAbiertoVentanaResultadoInformacionCapasOperables"
    @close="cerrarVentana('ResultadoInformacionCapasOperables')"
  >
    <span slot="title">
      <b>INFORMACIÓN DE LA CAPA: {{ informacionCapaOperativa?.titulo }}</b>
    </span>
    <a-space direction="vertical" style="width: 100%">
      <a-input v-model="cadenaBusqueda" placeholder="Buscar..." />
      <div>
        <a-table
          v-if="informacionCapaOperativa"
          bordered
          :columns="informacionCapaOperativa.columnas"
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
      'informacionCapaOperativa',
    ]),
    registrosFiltrados() {
      if (!this.cadenaBusqueda) {
        return this.informacionCapaOperativa.registros;
      }
      const query = this.cadenaBusqueda.toLowerCase();
      return this.informacionCapaOperativa.registros.filter((row) =>
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
