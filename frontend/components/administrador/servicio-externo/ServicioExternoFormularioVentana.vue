<template>
  <a-drawer
    :width="esMovil ? '100%' : 400"
    :mask-closable="false"
    :visible="estaAbiertoServicioExternoFormularioVentana"
    @close="cerrarServicioExternoFormularioVentana()"
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
        prop="url"
        label="URL:"
        :rules="[
          {
            required: true,
            message: 'Ingrese la URL del servicio externo',
          },
        ]"
      >
        <a-input
          v-model="formulario.url"
          placeholder="Ingrese la URL del servicio externo"
        />
      </a-form-model-item>
      <a-form-model-item
        prop="nombre"
        label="Nombre:"
        :rules="[
          {
            required: true,
            message: 'Ingrese el nombre del servicio externo',
          },
        ]"
      >
        <a-input
          v-model="formulario.nombre"
          placeholder="Ingrese el nombre del servicio externo"
        />
      </a-form-model-item>
      <a-form-model-item
        prop="atribucion"
        label="Atribución:"
        :rules="[
          {
            required: true,
            message: 'Ingrese la atribución del servicio externo',
          },
        ]"
      >
        <a-input
          v-model="formulario.atribucion"
          placeholder="Ingrese la atribución del servicio externo"
        />
      </a-form-model-item>
      <a-form-model-item prop="grupoCapaId" label="Grupo de capas:">
        <a-select
          v-model="formulario.grupoCapaId"
          :allow-clear="true"
          placeholder="Seleccione un grupo de capas"
        >
          <a-select-option
            v-for="elemento in gruposCapas"
            :key="elemento.id"
            :value="elemento.id"
          >
            {{ elemento.nombre }}
          </a-select-option>
        </a-select>
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
  </a-drawer>
</template>

<script>
import { mapState, mapActions } from "vuex";

const formulario = {
  url: "",
  nombre: "",
  atribucion: "",
  grupoCapaId: undefined,
  estaHabilitado: true,
};

export default {
  data() {
    return {
      formulario: { ...formulario },
    };
  },
  async fetch() {
    try {
      this.$iniciarCarga();
      await this.obtenerGruposCapas();
    } catch (error) {
      this.$manejarError(error);
    } finally {
      this.$finalizarCarga();
    }
  },
  computed: {
    ...mapState(["esMovil"]),
    ...mapState("administrador", [
      "estaAbiertoServicioExternoFormularioVentana",
      "gruposCapas",
      "servicioExterno",
    ]),
    esEdicion() {
      return this.servicioExterno !== undefined;
    },
    titulo() {
      return this.esEdicion
        ? "Actualizar servicio externo"
        : "Crear servicio externo";
    },
  },
  watch: {
    estaAbiertoServicioExternoFormularioVentana(value) {
      if (!value) {
        this.formulario = { ...formulario };
        this.$refs.referenciaFormulario?.resetFields();
      } else {
        if (this.esEdicion && this.servicioExterno) {
          // Si el valor es null o vacio se convierte a undefined para que el formulario no lo tome como un valor.
          const servicioExterno = { ...this.servicioExterno };
          Object.keys(servicioExterno).forEach((key) => {
            if (servicioExterno[key] === null || servicioExterno[key] === "") {
              servicioExterno[key] = undefined;
            }
          });
          this.formulario.nombre = servicioExterno.nombre;
          this.formulario.url = servicioExterno.url;
          this.formulario.atribucion = servicioExterno.atribucion;
          this.formulario.grupoCapaId = servicioExterno.grupoCapaId;
          this.formulario.estaHabilitado = servicioExterno.estaHabilitado;
        }
      }
    },
  },
  methods: {
    ...mapActions("administrador", [
      "cerrarServicioExternoFormularioVentana",
      "obtenerGruposCapas",
      "obtenerServiciosExternos",
    ]),
    guardar() {
      this.$refs.referenciaFormulario?.validate(async (valid) => {
        if (valid) {
          try {
            this.$iniciarCarga();
            // Se valida el contenido del grupo de capas.
            if (
              this.formulario.grupoCapaId === null ||
              this.formulario.grupoCapaId === ""
            ) {
              this.formulario.grupoCapaId = undefined;
            }
            if (this.esEdicion) {
              await this.$axios.put(
                `/servicios-externos/${this.servicioExterno.id}/`,
                {
                  ...this.formulario,
                }
              );
            } else {
              await this.$axios.post("/servicios-externos/", {
                ...this.formulario,
              });
            }
            await this.obtenerServiciosExternos();
            this.cerrarServicioExternoFormularioVentana();
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
