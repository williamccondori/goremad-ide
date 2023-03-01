<template>
  <ADrawer
    placement="left"
    :width="esMovil ? '100%' : 400"
    :visible="estaAbiertoMarcadorCatalogoVentana"
    @close="cerrarMarcadorCatalogoVentana()"
  >
    <span slot="title" style="text-transform: uppercase">
      <b>Marcadores</b>
    </span>
    <AButton
      type="primary"
      icon="plus"
      block
      @click="abrirMarcadorFormularioVentana()"
    >
      Agregar marcador
    </AButton>
    <ADivider />
    <ATable
      bordered
      row-key="id"
      :columns="columnas"
      :data-source="marcadores"
      size="middle"
    >
      <template #acciones="id">
        <AButton type="dashed" size="small" @click="ver(id)">
          <AIcon type="eye" />
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
    <MarcadorFormularioVentana />
  </ADrawer>
</template>

<script>
import {
  Drawer,
  Button,
  Icon,
  Divider,
  Table,
  Popconfirm,
} from "ant-design-vue";
import { mapState, mapActions } from "vuex";
import MarcadorFormularioVentana from "@/components/visor/marcador/MarcadorFormularioVentana.vue";
export default {
  components: {
    ADrawer: Drawer,
    AButton: Button,
    AIcon: Icon,
    ADivider: Divider,
    ATable: Table,
    APopconfirm: Popconfirm,
    MarcadorFormularioVentana,
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
  computed: {
    ...mapState(["esMovil"]),
    ...mapState("visor", ["estaAbiertoMarcadorCatalogoVentana", "marcadores"]),
  },
  methods: {
    ...mapActions("visor", [
      "cerrarMarcadorCatalogoVentana",
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
      this.cerrarMarcadorCatalogoVentana();
    },
  },
};
</script>
