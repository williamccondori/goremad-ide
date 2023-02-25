<template>
  <a-table
    bordered
    row-key="id"
    :columns="columnas"
    :data-source="usuarios"
    size="middle"
  >
    <template #acciones="id">
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
          title: "Usuario",
          dataIndex: "username",
          key: "username",
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
      await this.obtenerUsuarios();
    } catch (error) {
      this.$manejarError(error);
    } finally {
      this.$finalizarCarga();
    }
  },
  computed: {
    ...mapState("administrador", ["usuarios"]),
  },
  methods: {
    ...mapActions("administrador", [
      "obtenerUsuarios",
      "abrirUsuarioFormularioActualizacionVentana",
    ]),
    async editar(usuarioId) {
      try {
        this.$iniciarCarga();
        const { data } = await this.$axios.get(`/usuarios/${usuarioId}/`);
        this.abrirUsuarioFormularioActualizacionVentana(data);
      } catch (error) {
        this.$manejarError(error);
      } finally {
        this.$finalizarCarga();
      }
    },
    async eliminar(usuarioId) {
      try {
        this.$iniciarCarga();
        await this.$axios.delete(`/usuarios/${usuarioId}/`);
        await this.obtenerUsuarios();
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
