<template>
  <a-drawer
    :height="500"
    placement="bottom"
    :visible="estaAbiertoVentanaResultadoInformacionCapasOperables"
    @close="cerrarVentana('ResultadoInformacionCapasOperables')"
  >
    <span slot="title">
      <b>INFORMACIÓN DE LA CAPA: {{ informacionObjetoGeografico?.nombre }}</b>
    </span>
    <a-space direction="vertical" style="width: 100%">
      <a-input
        v-model="cadenaBusqueda"
        placeholder="Buscar (a partir del tercer caracter)..."
      />
      <div>
        <a-table
          v-if="informacionObjetoGeografico"
          bordered
          :columns="columasDisponibles"
          :data-source="registrosDisponibles"
          row-key="id"
          size="small"
        >
          <span
            v-for="columna in columasDisponibles"
            :key="`titulo-${columna.key}`"
            :slot="`titulo-${columna.key}`"
          >
            <a-tooltip
              placement="top"
              :title="informacionObjetoGeografico.alias[columna.key]"
            >
              <span>{{ columna.key.toUpperCase() }}</span>
            </a-tooltip>
          </span>
        </a-table>
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
      'informacionObjetoGeografico',
    ]),
    columasDisponibles() {
      if (!this.informacionObjetoGeografico) {
        return [];
      }
      return this.informacionObjetoGeografico.columnas.map((columna) => ({
        dataIndex: columna,
        key: columna,
        slots: {
          title: `titulo-${columna}`,
          customRender: columna.toUpperCase(),
        },
      }));
    },
    registrosDisponibles() {
      if (!this.cadenaBusqueda || this.cadenaBusqueda.length <= 3) {
        return this.informacionObjetoGeografico.registros;
      }
      const query = this.cadenaBusqueda.toLowerCase();
      return this.informacionObjetoGeografico.registros.filter((row) =>
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
