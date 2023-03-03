<template>
  <ATable
    bordered
    row-key="id"
    :columns="columnas"
    :data-source="imagenesSatelitales"
    size="middle"
  >
    <template #acciones="id">
      <AButton type="dashed" size="small" @click="ver(id)">
        <AIcon type="eye" />
      </AButton>
      <APopconfirm
        title="¿Está seguro que desea eliminar este registro, no se eliminará de GEOSERVER?"
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
          title: "Fecha",
          dataIndex: "fecha",
          key: "fecha",
        },
        {
          title: "Identificador",
          dataIndex: "identificador",
          key: "identificador",
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
      await this.obtenerImagenesSatelitales();
    } catch (error) {
      this.$manejarError(error);
    } finally {
      this.$finalizarCarga();
    }
  },
  computed: {
    ...mapState("administrador", ["imagenesSatelitales"]),
  },
  methods: {
    ...mapActions("administrador", [
      "obtenerImagenesSatelitales",
      "abrirImagenSatelitalResumenVentana",
    ]),
    async ver(imagenSatelitalId) {
      try {
        this.$iniciarCarga();
        const { data } = await this.$axios.get(
          `/imagenes-satelitales/${imagenSatelitalId}/`
        );
        this.abrirImagenSatelitalResumenVentana(data);
      } catch (error) {
        this.$manejarError(error);
      } finally {
        this.$finalizarCarga();
      }
    },
    async eliminar(imagenSatelitalId) {
      try {
        this.$iniciarCarga();
        await this.$axios.delete(`/imagenes-satelitales/${imagenSatelitalId}/`);
        await this.obtenerImagenesSatelitales();
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
