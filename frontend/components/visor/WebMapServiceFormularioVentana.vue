<template>
  <a-drawer
    width="25rem"
    :destroy-on-close="true"
    :visible="estaAbiertoWebMapServiceFormularioVentana"
    @close="cerrarWebMapServiceFormularioVentana()"
  >
    <span slot="title">
      <b>Agregar Web Map Service</b>
    </span>
    <div class="app--contenedor-vertical">
      <a-form-model
        ref="referenciaFormulario"
        :model="formulario"
        @submit.prevent="buscar()"
      >
        <a-form-model-item
          label="URL del Web Map Service"
          prop="url"
          :rules="[
            {
              required: true,
              message: 'Ingrese el URL del Web Map Service',
            },
          ]"
        >
          <a-input
            v-model="formulario.url"
            placeholder="Ingrese el URL del Web Map Service"
          />
        </a-form-model-item>
        <a-button html-type="submit" type="primary" icon="search" block>
          Buscar
        </a-button>
      </a-form-model>
      <div v-if="servicioExterno" class="app--contenedor-vertical-pequenio">
        <InformacionServicioDescriptor :servicio-externo="servicioExterno" />
        <div class="app--contenedor-horizontal-espaciado">
          <h1>
            <b>Todos las capas:</b>
          </h1>
          <a-tag color="green" style="margin: 0">
            {{ servicioExterno.capas.length }}
          </a-tag>
        </div>
        <a-list
          item-layout="horizontal"
          :data-source="servicioExterno.capas"
          style="overflow: hidden"
        >
          <a-list-item slot="renderItem" slot-scope="elemento">
            <a-list-item-meta>
              <span slot="title" style="line-break: anywhere">
                {{ elemento.titulo }}
              </span>
              <span slot="description">
                <a-tag color="green"> Capa: {{ elemento.nombre }} </a-tag>
              </span>
              <a-avatar
                slot="avatar"
                icon="global"
                style="background-color: green"
              />
            </a-list-item-meta>
          </a-list-item>
        </a-list>
        <a-button
          block
          type="primary"
          icon="plus"
          html-type="button"
          @click="agregar()"
        >
          Agregar Web Map Service
        </a-button>
        <a-button
          block
          type="danger"
          icon="delete"
          html-type="button"
          @click="limpiar()"
        >
          Limpiar
        </a-button>
      </div>
    </div>
    <a-modal
      :footer="null"
      :visible="estaAbiertoWebMapServiceFormularioModal"
      @cancel="cerrarWebMapServiceFormularioModal()"
    >
      <span slot="title"> Agregar Web Map Service </span>
      <a-form-model
        ref="referenciaFormularioCreacion"
        :model="formularioCreacion"
        @submit.prevent="guardar()"
      >
        <a-form-model-item
          label="Nombre"
          prop="nombre"
          :rules="[
            {
              required: true,
              message: 'Ingrese el nombre del Web Map Service',
            },
          ]"
        >
          <a-input
            v-model="formularioCreacion.nombre"
            placeholder="Ingrese el nombre del Web Map Service"
            @change="
              () => {
                formularioCreacion.titulo = `${formularioCreacion.atribucion}:${formularioCreacion.nombre}`;
              }
            "
          />
        </a-form-model-item>
        <a-form-model-item
          label="Atribución"
          prop="atribucion"
          :rules="[
            {
              required: true,
              message: 'Ingrese la atribución del Web Map Service',
            },
          ]"
        >
          <a-input
            v-model="formularioCreacion.atribucion"
            placeholder="Ingrese la atribución del Web Map Service"
            @change="
              () => {
                formularioCreacion.titulo = `${formularioCreacion.atribucion}:${formularioCreacion.nombre}`;
              }
            "
          />
        </a-form-model-item>
        <a-form-model-item label="Nombre a mostrar" prop="titulo">
          <a-input v-model="formularioCreacion.titulo" disabled>
            <template slot="addonBefore">
              <a-icon type="global" />
            </template>
          </a-input>
        </a-form-model-item>
        <a-button html-type="submit" type="primary" block icon="save">
          Guardar
        </a-button>
      </a-form-model>
    </a-modal>
  </a-drawer>
</template>

<script>
import { mapState, mapActions } from "vuex";
import InformacionServicioDescriptor from "@/components/visor/InformacionServicioDescriptor.vue";

const formulario = {
  url: "",
};

const formularioCreacion = {
  nombre: "",
  atribucion: "",
  titulo: "",
};

export default {
  components: {
    InformacionServicioDescriptor,
  },
  data() {
    return {
      servicioExterno: undefined,
      formulario: { ...formulario },
      formularioCreacion: { ...formularioCreacion },
      estaAbiertoWebMapServiceFormularioModal: false,
    };
  },
  computed: {
    ...mapState("visor", ["estaAbiertoWebMapServiceFormularioVentana"]),
  },
  watch: {
    estaAbiertoWebMapServiceFormularioVentana(valor) {
      if (!valor) {
        this.limpiar();
      }
    },
  },
  methods: {
    ...mapActions("visor", [
      "cerrarWebMapServiceFormularioVentana",
      "agregarCapaInteroperabilidad",
    ]),
    buscar() {
      this.$refs.referenciaFormulario.validate(async (valid) => {
        if (valid) {
          try {
            this.$iniciarCarga();
            const { data } = await this.$axios.get("/visor/web-map-services/", {
              params: {
                url: this.formulario.url,
              },
            });
            this.servicioExterno = data;
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
      this.$refs.referenciaFormulario.resetFields();
      this.servicioExterno = undefined;
    },
    agregar() {
      this.estaAbiertoWebMapServiceFormularioModal = true;
    },
    guardar() {
      this.$refs.referenciaFormularioCreacion.validate((valid) => {
        if (valid) {
          try {
            this.$iniciarCarga();
            this.agregarCapaInteroperabilidad({
              ...this.formularioCreacion,
              url: this.servicioExterno.url,
              capas: this.servicioExterno.capas,
            });
            this.$mostrarMensajeCorrecto();
            this.cerrarWebMapServiceFormularioModal();
            this.cerrarWebMapServiceFormularioVentana();
          } catch (error) {
            this.$manejarError(error);
          } finally {
            this.$finalizarCarga();
          }
        }
      });
    },
    cerrarWebMapServiceFormularioModal() {
      this.limpiarFormularioCreacion();
      this.estaAbiertoWebMapServiceFormularioModal = false;
    },
    limpiarFormularioCreacion() {
      this.formularioCreacion = { ...formularioCreacion };
      this.$refs.referenciaFormularioCreacion.resetFields();
    },
  },
};
</script>
