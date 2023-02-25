<template>
  <a-form-model
    ref="referenciaFormulario"
    :model="formulario"
    @submit.prevent="guardar"
  >
    <a-row :gutter="16" type="flex" justify="center">
      <a-col :xs="24" :md="12" :xxl="6">
        <a-form-model-item
          prop="nombreEmpresa"
          label="Nombre de la empresa:"
          :rules="[
            {
              required: true,
              message: 'Ingrese el nombre de la empresa',
            },
          ]"
        >
          <a-input
            v-model="formulario.nombreEmpresa"
            placeholder="Ingrese el nombre de la empresa"
          />
        </a-form-model-item>
        <a-form-model-item
          prop="latitudInicial"
          label="Latitud inicial:"
          :rules="[
            {
              required: true,
              message: 'Ingrese la latitud inicial',
            },
          ]"
        >
          <a-input-number
            v-model="formulario.latitudInicial"
            class="app--w-100"
            :precision="6"
            :step="0.000001"
            :min="-180"
            :max="180"
          />
        </a-form-model-item>
        <a-form-model-item
          prop="longitudInicial"
          label="Longitud inicial:"
          :rules="[
            {
              required: true,
              message: 'Ingrese la longitud inicial',
            },
          ]"
        >
          <a-input-number
            v-model="formulario.longitudInicial"
            class="app--w-100"
            :precision="6"
            :step="0.000001"
            :min="-180"
            :max="180"
          />
        </a-form-model-item>
      </a-col>
      <a-col :xs="24" :md="12" :xxl="6">
        <a-form-model-item
          prop="zoomInicial"
          label="Zoom inicial:"
          :rules="[
            {
              required: true,
              message: 'Ingrese el zoom inicial',
            },
          ]"
        >
          <a-input-number
            v-model="formulario.zoomInicial"
            class="app--w-100"
            placeholder="Zoom inicial"
            :min="0"
            :max="18"
          />
        </a-form-model-item>
        <a-form-model-item prop="capaBaseInicialId" label="Capa base inicial:">
          <a-select
            v-model="formulario.capaBaseInicialId"
            :allow-clear="true"
            placeholder="Seleccione una capa base"
          >
            <a-select-option
              v-for="elemento in capasBase"
              :key="elemento.id"
              :value="elemento.id"
            >
              {{ elemento.nombre }}
            </a-select-option>
          </a-select>
        </a-form-model-item>
        <a-form-model-item
          prop="serviciosExternosActivosIds"
          label="Servicios externos activos:"
        >
          <a-select
            v-model="formulario.serviciosExternosActivos"
            mode="multiple"
            placeholder="Seleccione uno o más servicios externos"
          >
            <a-select-option
              v-for="elemento in serviciosExternos"
              :key="elemento.id"
              :value="elemento.id"
            >
              {{ elemento.nombre }}
            </a-select-option>
          </a-select>
        </a-form-model-item>
      </a-col>
    </a-row>
    <a-row type="flex" justify="center">
      <a-col :xs="24" :xxl="12">
        <div>
          <a-button block html-type="submit" type="primary" icon="save">
            Actualizar variables
          </a-button>
        </div>
      </a-col>
    </a-row>
  </a-form-model>
</template>

<script>
import { mapState, mapActions } from "vuex";

const formulario = {
  nombreEmpresa: "",
  latitudInicial: 0,
  longitudInicial: 0,
  zoomInicial: 0,
  capaBaseInicialId: undefined,
  serviciosExternosActivos: [],
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
      await this.obtenerCapasBase();
      await this.obtenerServiciosExternos(true);
      await this.actualizarFormulario();
    } catch (error) {
      this.$manejarError(error);
    } finally {
      this.$finalizarCarga();
    }
  },
  computed: {
    ...mapState(["esMovil"]),
    ...mapState("administrador", [
      "capasBase",
      "configuraciones",
      "serviciosExternos",
    ]),
  },
  methods: {
    ...mapActions("administrador", [
      "obtenerCapasBase",
      "obtenerConfiguraciones",
      "obtenerServiciosExternos",
    ]),
    async actualizarFormulario() {
      await this.obtenerConfiguraciones();
      // Si el valor es null o vacio se convierte a undefined para que el formulario no lo tome como un valor.
      const configuraciones = this.configuraciones.map((configuracion) => ({
        ...configuracion,
      }));
      configuraciones.forEach((configuracion) => {
        if (configuracion.valor === null || configuracion.valor === "") {
          configuracion.valor = undefined;
        }
      });
      const nombreEmpresa = configuraciones.find(
        (configuracion) => configuracion.nombre === "nombre_empresa"
      )?.valor;
      const latitudInicial = configuraciones.find(
        (configuracion) => configuracion.nombre === "latitud_inicial"
      )?.valor;
      const longitudInicial = configuraciones.find(
        (configuracion) => configuracion.nombre === "longitud_inicial"
      )?.valor;
      const zoomInicial = configuraciones.find(
        (configuracion) => configuracion.nombre === "zoom_inicial"
      )?.valor;
      const capaBaseInicialId = configuraciones.find(
        (configuracion) => configuracion.nombre === "capa_base_incial_id"
      )?.valor;
      this.formulario.nombreEmpresa = nombreEmpresa;
      this.formulario.latitudInicial = latitudInicial;
      this.formulario.longitudInicial = longitudInicial;
      this.formulario.zoomInicial = zoomInicial;
      this.formulario.capaBaseInicialId = capaBaseInicialId;
      // Los servicios externos manejan un tratamiento especial.
      const serviciosExternosActivos = this.configuraciones.find(
        (configuracion) => configuracion.nombre === "servicios_externos_activos"
      )?.valor;
      this.formulario.serviciosExternosActivos =
        serviciosExternosActivos?.split(",") ?? [];
    },
    guardar() {
      this.$refs.referenciaFormulario?.validate(async (valid) => {
        if (valid) {
          try {
            this.$iniciarCarga();
            // Se valida el contenido de las capas base.
            if (
              this.formulario.capaBaseInicialId === null ||
              this.formulario.capaBaseInicialId === ""
            ) {
              this.formulario.capaBaseInicialId = undefined;
            }
            // Se valida el contenido de los servicios externos.
            if (this.formulario.serviciosExternosActivos.length === 0) {
              this.formulario.serviciosExternosActivos = undefined;
            } else {
              this.formulario.serviciosExternosActivos =
                this.formulario.serviciosExternosActivos.join(",");
            }
            await this.$axios.put(`/configuraciones/`, { ...this.formulario });
            await this.actualizarFormulario();
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
