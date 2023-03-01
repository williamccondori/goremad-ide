<template>
  <ADrawer
    placement="left"
    :width="esMovil ? '100%' : 400"
    :visible="estaAbiertoUbicacionVentana"
    @close="cerrarUbicacionVentana()"
  >
    <span slot="title" style="text-transform: uppercase">
      <b>Búsqueda de ubicaciones</b>
    </span>
    <div class="app--contenedor-vertical">
      <AFormModel
        ref="referenciaFormulario"
        :model="formulario"
        @submit.prevent="buscar()"
      >
        <AFormModelItem
          label="Término de búsqueda"
          prop="query"
          :rules="[
            {
              required: true,
              message: 'Ingrese el término de búsqueda',
            },
          ]"
        >
          <AInput
            v-model="formulario.query"
            placeholder="Ingrese el término de búsqueda"
          />
        </AFormModelItem>
        <AButton html-type="submit" type="primary" icon="search" block>
          Buscar
        </AButton>
      </AFormModel>
      <ADivider />
      <div class="app--contenedor-horizontal-espaciado">
        <span>Todos los elementos:</span>
        <ATag color="green" style="margin: 0">
          {{ resultados.length }}
        </ATag>
      </div>
      <div class="app--contenedor-vertical-pequenio">
        <AButton
          v-for="resultado in resultados"
          :key="resultado.id"
          type="dashed"
          html-button="button"
          @click="ver(resultado)"
        >
          {{ resultado.nombre }}
        </AButton>
      </div>
      <div>
        <AButton
          block
          type="danger"
          icon="delete"
          html-type="button"
          :disabled="resultados.length === 0"
          @click="limpiar()"
        >
          Limpiar
        </AButton>
      </div>
    </div>
    <section />
  </ADrawer>
</template>

<script>
import { Drawer, FormModel, Input, Button, Divider, Tag } from "ant-design-vue";
import { mapState, mapActions } from "vuex";

const formulario = {
  query: "",
};

export default {
  components: {
    ADrawer: Drawer,
    AFormModel: FormModel,
    AFormModelItem: FormModel.Item,
    AInput: Input,
    AButton: Button,
    ADivider: Divider,
    ATag: Tag,
  },
  data() {
    return {
      formulario: { ...formulario },
      resultados: [],
    };
  },
  computed: {
    ...mapState(["esMovil"]),
    ...mapState("visor", ["estaAbiertoUbicacionVentana"]),
  },
  watch: {
    estaAbiertoUbicacionVentana(valor) {
      if (!valor) {
        this.limpiar();
      }
    },
  },
  methods: {
    ...mapActions("visor", [
      "cerrarUbicacionVentana",
      "establecerCentro",
      "establecerZoom",
    ]),
    buscar() {
      this.$refs.referenciaFormulario?.validate(async (valid) => {
        if (valid) {
          try {
            this.$iniciarCarga();
            const { data } = await this.$axios.get("/visor/ubicaciones/", {
              params: {
                query: this.formulario.query,
              },
            });
            this.resultados = data;
          } catch (error) {
            this.$manejarError(error);
          } finally {
            this.$finalizarCarga();
          }
        }
      });
    },
    ver(resultado) {
      this.establecerCentro(resultado.centro);
      this.establecerZoom(resultado.zoom);
    },
    limpiar() {
      this.formulario = { ...formulario };
      this.$refs.referenciaFormulario?.resetFields();
      this.resultados = [];
    },
  },
};
</script>
