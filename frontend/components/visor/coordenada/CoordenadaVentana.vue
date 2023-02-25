<template>
  <a-drawer
    width="25rem"
    placement="left"
    :visible="estaAbiertoCoordenadaVentana"
    @close="cerrarCoordenadaVentana()"
  >
    <span slot="title">
      <b>Búsqueda de coordenadas</b>
    </span>

    <a-form-model
      ref="referenciaFormulario"
      :model="formulario"
      @submit.prevent="buscar()"
    >
      <a-form-model-item
        label="Sistema de coordenadas"
        prop="proyeccion"
        :rules="[
          {
            required: true,
            message: 'Seleccione el sistema de coordenadas',
          },
        ]"
      >
        <a-select v-model="formulario.proyeccion" @change="cambiarProyeccion()">
          <a-select-option value="latlong">GEOGRÁFICA</a-select-option>
          <a-select-option value="utm">UTM</a-select-option>
        </a-select>
      </a-form-model-item>
      <a-form-model-item
        label="Datum"
        prop="datum"
        :rules="[
          {
            required: formulario.proyeccion === 'utm',
            message: 'Seleccione el Datum',
          },
        ]"
      >
        <a-select
          v-model="formulario.datum"
          :disabled="formulario.proyeccion !== 'utm'"
        >
          <a-select-option
            v-for="datum in datums"
            :key="datum.codigo"
            :value="datum.codigo"
          >
            {{ datum.etiqueta }}
          </a-select-option>
        </a-select>
      </a-form-model-item>
      <a-form-model-item
        label="Zona UTM"
        prop="zona"
        :rules="[
          {
            required: formulario.proyeccion === 'utm',
            message: 'Seleccione la zona UTM',
          },
        ]"
      >
        <a-select
          v-model="formulario.zona"
          :disabled="formulario.proyeccion !== 'utm'"
        >
          <a-select-option value="17">17</a-select-option>
          <a-select-option value="18">18</a-select-option>
          <a-select-option value="19">19</a-select-option>
        </a-select>
      </a-form-model-item>
      <a-form-model-item
        :label="formulario.proyeccion === 'utm' ? 'X' : 'Longitud'"
        prop="x"
        :rules="[
          {
            required: true,
            message: `Ingrese el valor para: ${
              formulario.proyeccion === 'utm' ? 'X' : 'Longitud'
            }`,
          },
        ]"
      >
        <a-input
          v-model="formulario.x"
          placeholder="Ingrese el término de búsqueda"
        />
      </a-form-model-item>
      <a-form-model-item
        :label="formulario.proyeccion === 'utm' ? 'Y' : 'Latitud'"
        prop="y"
        :rules="[
          {
            required: true,
            message: `Ingrese el valor para: ${
              formulario.proyeccion === 'utm' ? 'Y' : 'Latitud'
            }`,
          },
        ]"
      >
        <a-input
          v-model="formulario.y"
          placeholder="Ingrese el término de búsqueda"
        />
      </a-form-model-item>
      <a-button html-type="submit" type="primary" icon="search" block>
        Buscar
      </a-button>
    </a-form-model>
  </a-drawer>
</template>

<script>
import { mapState, mapActions } from "vuex";

const formulario = {
  proyeccion: "latlong",
  datum: "WGS84",
  zona: 17,
  x: 0,
  y: 0,
};

const datumsLatLong = [{ codigo: "WGS84", etiqueta: "WGS84" }];
const datumsUtm = [{ codigo: "PSAD56", etiqueta: "PSAD56" }];

export default {
  data() {
    return {
      formulario: { ...formulario },
      datums: datumsLatLong,
    };
  },
  computed: {
    ...mapState("visor", ["estaAbiertoCoordenadaVentana"]),
  },
  watch: {
    estaAbiertoCoordenadaVentana(valor) {
      if (!valor) {
        this.limpiar();
      }
    },
  },
  methods: {
    ...mapActions("visor", [
      "cerrarCoordenadaVentana",
      "establecerCentro",
      "establecerZoom",
    ]),
    buscar() {
      this.$refs.referenciaFormulario?.validate(async (valid) => {
        if (valid) {
          try {
            this.$iniciarCarga();
            const { data } = await this.$axios.get("/visor/coordenadas/", {
              params: this.formulario,
            });
            this.establecerCentro([data.latitud, data.longitud]);
            this.establecerZoom(15);
            this.cerrarCoordenadaVentana();
          } catch (error) {
            this.$manejarError(error);
          } finally {
            this.$finalizarCarga();
          }
        }
      });
    },
    limpiar() {
      this.formulario = { ...formulario };
      this.$refs.referenciaFormulario?.resetFields();
    },
    cambiarProyeccion() {
      const { proyeccion } = this.formulario;
      if (proyeccion === "utm") {
        this.datums = datumsUtm;
        this.formulario.datum = "PSAD56";
      } else {
        this.datums = datumsLatLong;
        this.formulario.datum = "WGS84";
      }
    },
  },
};
</script>
