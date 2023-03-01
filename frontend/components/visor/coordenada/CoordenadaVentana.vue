<template>
  <ADrawer
    placement="left"
    :width="esMovil ? '100%' : 400"
    :visible="estaAbiertoCoordenadaVentana"
    @close="cerrarCoordenadaVentana()"
  >
    <span slot="title" style="text-transform: uppercase">
      <b>Búsqueda de coordenadas</b>
    </span>
    <AFormModel
      ref="referenciaFormulario"
      :model="formulario"
      @submit.prevent="buscar()"
    >
      <AFormModelItem
        label="Sistema de coordenadas"
        prop="proyeccion"
        :rules="[
          {
            required: true,
            message: 'Seleccione el sistema de coordenadas',
          },
        ]"
      >
        <ASelect v-model="formulario.proyeccion" @change="cambiarProyeccion()">
          <ASelectOption value="latlong">GEOGRÁFICA</ASelectOption>
          <ASelectOption value="utm">UTM</ASelectOption>
        </ASelect>
      </AFormModelItem>
      <AFormModelItem
        label="Datum"
        prop="datum"
        :rules="[
          {
            required: formulario.proyeccion === 'utm',
            message: 'Seleccione el Datum',
          },
        ]"
      >
        <ASelect
          v-model="formulario.datum"
          :disabled="formulario.proyeccion !== 'utm'"
        >
          <ASelectOption
            v-for="datum in datums"
            :key="datum.codigo"
            :value="datum.codigo"
          >
            {{ datum.etiqueta }}
          </ASelectOption>
        </ASelect>
      </AFormModelItem>
      <AFormModelItem
        label="Zona UTM"
        prop="zona"
        :rules="[
          {
            required: formulario.proyeccion === 'utm',
            message: 'Seleccione la zona UTM',
          },
        ]"
      >
        <ASelect
          v-model="formulario.zona"
          :disabled="formulario.proyeccion !== 'utm'"
        >
          <ASelectOption value="17">17</ASelectOption>
          <ASelectOption value="18">18</ASelectOption>
          <ASelectOption value="19">19</ASelectOption>
        </ASelect>
      </AFormModelItem>
      <AFormModelItem
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
        <AInput
          v-model="formulario.x"
          placeholder="Ingrese el término de búsqueda"
        />
      </AFormModelItem>
      <AFormModelItem
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
        <AInput
          v-model="formulario.y"
          placeholder="Ingrese el término de búsqueda"
        />
      </AFormModelItem>
      <AButton html-type="submit" type="primary" icon="search" block>
        Buscar
      </AButton>
    </AFormModel>
  </ADrawer>
</template>

<script>
import { Drawer, FormModel, Input, Button, Select } from "ant-design-vue";
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
  components: {
    ADrawer: Drawer,
    AFormModel: FormModel,
    AFormModelItem: FormModel.Item,
    AInput: Input,
    AButton: Button,
    ASelect: Select,
    ASelectOption: Select.Option,
  },
  data() {
    return {
      formulario: { ...formulario },
      datums: datumsLatLong,
    };
  },
  computed: {
    ...mapState(["esMovil"]),
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
