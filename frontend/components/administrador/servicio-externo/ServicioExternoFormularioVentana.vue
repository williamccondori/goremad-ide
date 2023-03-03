<template>
  <ADrawer
    :width="esMovil ? '100%' : 400"
    :mask-closable="false"
    :visible="estaAbiertoServicioExternoFormularioVentana"
    @close="cerrarServicioExternoFormularioVentana()"
  >
    <span slot="title" style="text-transform: uppercase">
      <b>{{ titulo }}</b>
    </span>
    <AFormModel
      ref="referenciaFormulario"
      :model="formulario"
      @submit.prevent="guardar()"
    >
      <AFormModelItem
        prop="url"
        label="URL:"
        :rules="[
          {
            required: true,
            message: 'Ingrese la URL del servicio externo',
          },
        ]"
      >
        <AInput
          v-model="formulario.url"
          placeholder="Ingrese la URL del servicio externo"
        />
      </AFormModelItem>
      <AFormModelItem
        prop="nombre"
        label="Nombre:"
        :rules="[
          {
            required: true,
            message: 'Ingrese el nombre del servicio externo',
          },
        ]"
      >
        <AInput
          v-model="formulario.nombre"
          placeholder="Ingrese el nombre del servicio externo"
        />
      </AFormModelItem>
      <AFormModelItem
        prop="atribucion"
        label="Atribución:"
        :rules="[
          {
            required: true,
            message: 'Ingrese la atribución del servicio externo',
          },
        ]"
      >
        <AInput
          v-model="formulario.atribucion"
          placeholder="Ingrese la atribución del servicio externo"
        />
      </AFormModelItem>
      <AFormModelItem prop="grupoCapaId" label="Grupo de capas:">
        <ASelect
          v-model="formulario.grupoCapaId"
          :allow-clear="true"
          placeholder="Seleccione un grupo de capas"
        >
          <ASelectOption
            v-for="elemento in gruposCapas"
            :key="elemento.id"
            :value="elemento.id"
          >
            {{ elemento.nombre }}
          </ASelectOption>
        </ASelect>
      </AFormModelItem>
      <AFormModelItem prop="estaHabilitado" label="¿Está habilitado?:">
        <ACheckbox v-model="formulario.estaHabilitado" />
      </AFormModelItem>
      <div>
        <AButton block html-type="submit" type="primary" icon="save">
          {{ titulo }}
        </AButton>
      </div>
    </AFormModel>
  </ADrawer>
</template>

<script>
import {
  Drawer,
  FormModel,
  Input,
  Select,
  Checkbox,
  Button,
} from "ant-design-vue";
import { mapState, mapActions } from "vuex";

const formulario = {
  url: "",
  nombre: "",
  atribucion: "",
  grupoCapaId: undefined,
  estaHabilitado: true,
};

export default {
  components: {
    ADrawer: Drawer,
    AFormModel: FormModel,
    AFormModelItem: FormModel.Item,
    AInput: Input,
    ASelect: Select,
    ASelectOption: Select.Option,
    ACheckbox: Checkbox,
    AButton: Button,
  },
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
