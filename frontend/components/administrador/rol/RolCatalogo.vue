<template>
  <ATable
    bordered
    row-key="id"
    :columns="columnas"
    :data-source="usuarios"
    size="middle"
  >
    <template #roles="roles">
      <ASpace>
        <ATag v-for="rol in roles" :key="rol" :color="obtenerColor(rol)">
          {{ rol }}
        </ATag>
      </ASpace>
    </template>
    <template slot="acciones" slot-scope="id, row">
      <AButton
        v-if="!row.roles.includes('superusuario')"
        type="dashed"
        size="small"
        @click="editar(id)"
      >
        <AIcon type="edit" />
      </AButton>
    </template>
  </ATable>
</template>

<script>
import { Table, Button, Icon, Tag, Space } from "ant-design-vue";
import { mapState, mapActions } from "vuex";
export default {
  components: {
    ATable: Table,
    AButton: Button,
    AIcon: Icon,
    ATag: Tag,
    ASpace: Space,
  },
  data() {
    return {
      columnas: [
        {
          title: "Usuario",
          dataIndex: "username",
          key: "username",
        },
        {
          title: "Roles",
          dataIndex: "roles",
          key: "roles",
          scopedSlots: {
            customRender: "roles",
          },
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
      "abrirRolFormularioActualizacionVentana",
    ]),
    obtenerColor(rol) {
      switch (rol) {
        case "superusuario":
          return "red";
        case "administrador":
          return "orange";
        default:
          return "green";
      }
    },
    async editar(capaBaseId) {
      try {
        this.$iniciarCarga();
        const { data } = await this.$axios.get(`/usuarios/${capaBaseId}/`);
        this.abrirRolFormularioActualizacionVentana(data);
      } catch (error) {
        this.$manejarError(error);
      } finally {
        this.$finalizarCarga();
      }
    },
  },
};
</script>
