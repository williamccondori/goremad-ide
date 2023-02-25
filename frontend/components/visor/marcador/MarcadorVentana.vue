<template>
  <a-drawer
    width="25rem"
    placement="left"
    :visible="estaAbiertoMarcadorVentana"
    @close="cerrarMarcadorVentana()"
  >
    <span slot="title">
      <b>Marcadores</b>
    </span>
    <a-button
      type="primary"
      icon="plus"
      block
      @click="abrirMarcadorFormularioVentana()"
    >
      Agregar marcador
    </a-button>
    <a-divider />
    <DataTable
      :data="marcadores"
      :columns="{
        nombre: 'Nombre',
        actions: 'Acciones',
      }"
      :show-edit="false"
      @onDelete="eliminar"
    >
      <template #actions="{ id }">
        <a-button type="dashed" size="small" @click="ver(id)">
          <a-icon type="eye" />
        </a-button>
      </template>
    </DataTable>
    <MarcadorFormularioVentana />
  </a-drawer>
</template>

<script>
import { mapState, mapActions } from "vuex";
import DataTable from "@/components/compartido/DataTable.vue";
import MarcadorFormularioVentana from "@/components/visor/marcador/MarcadorFormularioVentana.vue";
export default {
  components: {
    DataTable,
    MarcadorFormularioVentana,
  },
  computed: {
    ...mapState("visor", ["estaAbiertoMarcadorVentana", "marcadores"]),
  },
  methods: {
    ...mapActions("visor", [
      "cerrarMarcadorVentana",
      "eliminarMarcador",
      "establecerCentro",
      "establecerZoom",
      "abrirMarcadorFormularioVentana",
    ]),
    eliminar(marcadorId) {
      this.eliminarMarcador(marcadorId);
      this.$mostrarMensajeCorrecto();
    },
    ver(marcadorId) {
      const marcador = this.marcadores.find((m) => m.id === marcadorId);
      this.establecerCentro([marcador.latitud, marcador.longitud]);
      this.establecerZoom(marcador.zoom);
      this.cerrarMarcadorVentana();
    },
  },
};
</script>
