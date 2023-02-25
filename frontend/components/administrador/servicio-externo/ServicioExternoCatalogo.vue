<template>
  <a-table
    bordered
    row-key="id"
    :columns="columnas"
    :data-source="serviciosExternos"
    size="middle"
  >
    <template slot="acciones" slot-scope="id">
      <a-button type="dashed" size="small" @click="editar(id)">
        <a-icon type="edit" />
      </a-button>
      <a-popconfirm
        title="¿Está seguro que desea eliminar este registro?"
        @confirm="eliminar(id)"
      >
        <a-button type="dashed" size="small">
          <a-icon type="delete" />
        </a-button>
      </a-popconfirm>
    </template>
  </a-table>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  data() {
    return {
      columnas: [
        {
          title: "Atribucion",
          dataIndex: "atribucion",
          key: "atribucion",
        },
        {
          title: "Nombre",
          dataIndex: "nombre",
          key: "nombre",
        },
        {
          title: "Acciones",
          dataIndex: "id",
          key: "id",
          scopedSlots: {
            customRender: "acciones",
          },
        },
      ],
    };
  },
  async fetch() {
    try {
      this.$iniciarCarga();
      await this.obtenerServiciosExternos();
    } catch (error) {
      this.$manejarError(error);
    } finally {
      this.$finalizarCarga();
    }
  },
  computed: {
    ...mapState("administrador", ["serviciosExternos"]),
  },
  methods: {
    ...mapActions("administrador", [
      "obtenerServiciosExternos",
      "abrirServicioExternoFormularioActualizacionVentana",
    ]),
    async editar(servicioExternoId) {
      try {
        this.$iniciarCarga();
        const { data } = await this.$axios.get(
          `/servicios-externos/${servicioExternoId}/`
        );
        this.abrirServicioExternoFormularioActualizacionVentana(data);
      } catch (error) {
        this.$manejarError(error);
      } finally {
        this.$finalizarCarga();
      }
    },
    async eliminar(servicioExternoId) {
      try {
        this.$iniciarCarga();
        await this.$axios.delete(`/servicios-externos/${servicioExternoId}/`);
        await this.obtenerServiciosExternos();
        this.$mostrarMensajeCorrecto();
      } catch (error) {
        this.$manejarError(error);
      } finally {
        this.$finalizarCarga();
      }
    },
  },
};
</script>
