<template>
  <ATable
    bordered
    row-key="id"
    :columns="columnas"
    :data-source="capasBase"
    size="middle"
  >
    <template #acciones="id">
      <AButton type="dashed" size="small" @click="editar(id)">
        <AIcon type="edit" />
      </AButton>
      <APopconfirm
        title="¿Está seguro que desea eliminar este registro?"
        @confirm="eliminar(id)"
      >
        <AButton type="dashed" size="small">
          <AIcon type="delete" />
        </AButton>
      </APopconfirm>
    </template>
  </ATable>
</template>

<script>
import { Table, Button, Popconfirm, Icon } from "ant-design-vue";
import { mapState, mapActions } from "vuex";
export default {
  components: {
    ATable: Table,
    AButton: Button,
    APopconfirm: Popconfirm,
    AIcon: Icon,
  },
  data() {
    return {
      columnas: [
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
      await this.obtenerCapasBase();
    } catch (error) {
      this.$manejarError(error);
    } finally {
      this.$finalizarCarga();
    }
  },
  computed: {
    ...mapState("administrador", ["capasBase"]),
  },
  methods: {
    ...mapActions("administrador", [
      "obtenerCapasBase",
      "abrirCapaBaseFormularioActualizacionVentana",
    ]),
    async editar(capaBaseId) {
      try {
        this.$iniciarCarga();
        const { data } = await this.$axios.get(`/capas-base/${capaBaseId}/`);
        this.abrirCapaBaseFormularioActualizacionVentana(data);
      } catch (error) {
        this.$manejarError(error);
      } finally {
        this.$finalizarCarga();
      }
    },
    async eliminar(capaBaseId) {
      try {
        this.$iniciarCarga();
        await this.$axios.delete(`/capas-base/${capaBaseId}/`);
        await this.obtenerCapasBase();
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
