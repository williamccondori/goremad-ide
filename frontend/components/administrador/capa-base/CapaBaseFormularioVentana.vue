<template>
  <ADrawer
    :width="esMovil ? '100%' : 400"
    :mask-closable="false"
    :visible="estaAbiertoCapaBaseFormularioVentana"
    @close="cerrarCapaBaseFormularioVentana()"
  >
    <span slot="title" style="text-transform: uppercase">
      <b>{{ titulo }}</b>
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
            message: 'Ingrese el nombre de la capa base',
          },
        ]"
      >
        <a-input
          v-model="formulario.nombre"
          placeholder="Ingrese el nombre de la capa base"
        />
      </a-form-model-item>
      <a-form-model-item
        prop="url"
        label="URL:"
        :rules="[
          {
            required: true,
            message: 'Ingrese la URL de la capa base',
          },
        ]"
      >
        <a-input
          v-model="formulario.url"
          placeholder="Ingrese la URL de la capa base"
        />
      </a-form-model-item>
      <a-form-model-item
        prop="atribucion"
        label="Atribución:"
        :rules="[
          {
            required: true,
            message: 'Ingrese la atribución de la capa base',
          },
        ]"
      >
        <a-input
          v-model="formulario.atribucion"
          placeholder="Ingrese la atribución de la capa base"
        />
      </a-form-model-item>
      <a-form-model-item prop="estaHabilitado" label="¿Está habilitado?:">
        <a-checkbox v-model="formulario.estaHabilitado" />
      </a-form-model-item>
      <div>
        <a-button block html-type="submit" type="primary" icon="save">
          {{ titulo }}
        </a-button>
      </div>
    </a-form-model>
  </ADrawer>
</template>

<script>
import { Drawer } from "ant-design-vue";
import { mapState, mapActions } from "vuex";

const formulario = {
  nombre: "",
  url: "",
  atribucion: "",
  estaHabilitado: true,
};

export default {
  components: {
    ADrawer: Drawer,
  },
  data() {
    return {
      formulario: { ...formulario },
    };
  },
  computed: {
    ...mapState(["esMovil"]),
    ...mapState("administrador", [
      "estaAbiertoCapaBaseFormularioVentana",
      "capaBase",
    ]),
    esEdicion() {
      return this.capaBase !== undefined;
    },
    titulo() {
      return this.esEdicion ? "Actualizar capa base" : "Crear capa base";
    },
  },
  watch: {
    estaAbiertoCapaBaseFormularioVentana(value) {
      if (!value) {
        this.formulario = { ...formulario };
        this.$refs.referenciaFormulario?.resetFields();
      } else {
        if (this.esEdicion && this.capaBase) {
          this.formulario.nombre = this.capaBase.nombre;
          this.formulario.url = this.capaBase.url;
          this.formulario.atribucion = this.capaBase.atribucion;
          this.formulario.estaHabilitado = this.capaBase.estaHabilitado;
        }
      }
    },
  },
  methods: {
    ...mapActions("administrador", [
      "cerrarCapaBaseFormularioVentana",
      "obtenerCapasBase",
    ]),
    guardar() {
      this.$refs.referenciaFormulario?.validate(async (valid) => {
        if (valid) {
          try {
            this.$iniciarCarga();
            if (this.esEdicion) {
              await this.$axios.put(`/capas-base/${this.capaBase.id}/`, {
                ...this.formulario,
              });
            } else {
              await this.$axios.post("/capas-base/", { ...this.formulario });
            }
            await this.obtenerCapasBase();
            this.cerrarCapaBaseFormularioVentana();
            this.$mostrarMensajeCorrecto();
          } catch (error) {
            this.$manejarError(error);
          } finally {
            this.$finalizarCarga();
          }
        }
      });
    },
  },
};
</script>
