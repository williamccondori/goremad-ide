<template>
  <ADrawer
    placement="left"
    :width="esMovil ? '100%' : 400"
    :visible="estaAbiertoMarcadorFormularioVentana"
    @close="cerrarMarcadorFormularioVentana()"
  >
    <span slot="title" style="text-transform: uppercase">
      <b>Agregar marcador</b>
    </span>
    <AFormModel
      ref="referenciaFormulario"
      :model="formulario"
      @submit.prevent="guardar()"
    >
      <AFormModelItem
        prop="nombre"
        label="Nombre:"
        :rules="[
          {
            required: true,
            message: 'Ingrese el nombre del marcador',
          },
        ]"
      >
        <AInput
          v-model="formulario.nombre"
          placeholder="Ingrese el nombre del marcador"
        />
      </AFormModelItem>
      <AFormModelItem
        prop="zoom"
        label="Zoom:"
        :rules="[
          {
            required: true,
            message: 'Ingrese el zoom del mapa',
          },
        ]"
      >
        <AInput
          v-model="formulario.zoom"
          placeholder="Ingrese el zoom del mapa"
          disabled
        />
      </AFormModelItem>
      <ARow :gutter="16">
        <ACol :span="12">
          <AFormModelItem
            prop="latitud"
            label="Latitud:"
            :rules="[
              {
                required: true,
                message: 'Ingrese la latitud del mapa',
              },
            ]"
          >
            <AInput v-model="formulario.latitud" disabled />
          </AFormModelItem>
        </ACol>
        <ACol :span="12">
          <AFormModelItem
            prop="longitud"
            label="Longitud:"
            :rules="[
              {
                required: true,
                message: 'Ingrese la longitud del mapa',
              },
            ]"
          >
            <AInput v-model="formulario.longitud" disabled />
          </AFormModelItem>
        </ACol>
      </ARow>
      <AButton html-type="submit" type="primary" icon="save" block>
        Guardar
      </AButton>
    </AFormModel>
  </ADrawer>
</template>

<script>
import { Drawer, FormModel, Input, Button, Row, Col } from "ant-design-vue";
import { mapState, mapActions } from "vuex";

const formulario = {
  nombre: "",
  zoom: 0,
  latitud: 0,
  longitud: 0,
};

export default {
  components: {
    ADrawer: Drawer,
    AFormModel: FormModel,
    AFormModelItem: FormModel.Item,
    AInput: Input,
    AButton: Button,
    ARow: Row,
    ACol: Col,
  },
  data() {
    return {
      formulario: { ...formulario },
    };
  },
  computed: {
    ...mapState(["esMovil"]),
    ...mapState("visor", [
      "estaAbiertoMarcadorFormularioVentana",
      "informacionPosicion",
    ]),
  },
  watch: {
    estaAbiertoMarcadorFormularioVentana(valor) {
      if (!valor) {
        this.limpiar();
      } else {
        if (this.informacionPosicion) {
          this.formulario.zoom = this.informacionPosicion.zoom;
          this.formulario.latitud = this.informacionPosicion.latitud;
          this.formulario.longitud = this.informacionPosicion.longitud;
        }
      }
    },
  },
  methods: {
    ...mapActions("visor", [
      "cerrarMarcadorFormularioVentana",
      "agregarMarcador",
    ]),
    guardar() {
      this.$refs.referenciaFormulario?.validate((valid) => {
        if (valid) {
          this.agregarMarcador({ ...this.formulario });
          this.$mostrarMensajeCorrecto();
          this.cerrarMarcadorFormularioVentana();
        }
      });
    },
    limpiar() {
      this.formulario = { ...formulario };
      this.$refs.referenciaFormulario?.resetFields();
    },
  },
};
</script>
