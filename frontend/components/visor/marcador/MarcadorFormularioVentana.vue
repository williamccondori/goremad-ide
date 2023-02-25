<template>
  <a-drawer
    width="25rem"
    placement="left"
    :visible="estaAbiertoMarcadorFormularioVentana"
    @close="cerrarMarcadorFormularioVentana()"
  >
    <span slot="title">
      <b>Agregar marcador</b>
    </span>
    <a-form-model
      ref="referenciaFormulario"
      :model="formulario"
      @submit.prevent="guardar()"
    >
      <a-form-model-item
        prop="nombre"
        label="Nombre:"
        :rules="[
          {
            required: true,
            message: 'Ingrese el nombre del marcador',
          },
        ]"
      >
        <a-input
          v-model="formulario.nombre"
          placeholder="Ingrese el nombre del marcador"
        />
      </a-form-model-item>
      <a-form-model-item
        prop="zoom"
        label="Zoom:"
        :rules="[
          {
            required: true,
            message: 'Ingrese el zoom del mapa',
          },
        ]"
      >
        <a-input
          v-model="formulario.zoom"
          placeholder="Ingrese el zoom del mapa"
          disabled
        />
      </a-form-model-item>
      <a-row :gutter="16">
        <a-col :span="12">
          <a-form-model-item
            prop="latitud"
            label="Latitud:"
            :rules="[
              {
                required: true,
                message: 'Ingrese la latitud del mapa',
              },
            ]"
          >
            <a-input v-model="formulario.latitud" disabled />
          </a-form-model-item>
        </a-col>
        <a-col :span="12">
          <a-form-model-item
            prop="longitud"
            label="Longitud:"
            :rules="[
              {
                required: true,
                message: 'Ingrese la longitud del mapa',
              },
            ]"
          >
            <a-input v-model="formulario.longitud" disabled />
          </a-form-model-item>
        </a-col>
      </a-row>
      <a-button html-type="submit" type="primary" icon="save" block>
        Guardar
      </a-button>
    </a-form-model>
  </a-drawer>
</template>

<script>
import { mapState, mapActions } from "vuex";

const formulario = {
  nombre: "",
  zoom: 0,
  latitud: 0,
  longitud: 0,
};

export default {
  data() {
    return {
      formulario: { ...formulario },
    };
  },
  computed: {
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
