<template>
  <a-drawer
    width="25rem"
    placement="left"
    :visible="estaAbiertoUbicacionVentana"
    @close="cerrarUbicacionVentana()"
  >
    <span slot="title">
      <b>Búsqueda de ubicaciones</b>
    </span>
    <div class="app--contenedor-vertical">
      <a-form-model
        ref="referenciaFormulario"
        :model="formulario"
        @submit.prevent="buscar()"
      >
        <a-form-model-item
          label="Término de búsqueda"
          prop="query"
          :rules="[
            {
              required: true,
              message: 'Ingrese el término de búsqueda',
            },
          ]"
        >
          <a-input
            v-model="formulario.query"
            placeholder="Ingrese el término de búsqueda"
          />
        </a-form-model-item>
        <a-button html-type="submit" type="primary" icon="search" block>
          Buscar
        </a-button>
      </a-form-model>
      <a-divider />
      <div class="app--contenedor-horizontal-espaciado">
        <span>Todos los elementos:</span>
        <a-tag color="green" style="margin: 0">
          {{ resultados.length }}
        </a-tag>
      </div>
      <div class="app--contenedor-vertical-pequenio">
        <a-button
          v-for="resultado in resultados"
          :key="resultado.id"
          type="dashed"
          html-button="button"
          @click="ver(resultado)"
        >
          {{ resultado.nombre }}
        </a-button>
      </div>
      <div>
        <a-button
          block
          type="danger"
          icon="delete"
          html-type="button"
          :disabled="resultados.length === 0"
          @click="limpiar()"
        >
          Limpiar
        </a-button>
      </div>
    </div>
    <section />
  </a-drawer>
</template>

<script>
import { mapState, mapActions } from "vuex";

const formulario = {
  query: "",
};

export default {
  data() {
    return {
      formulario: { ...formulario },
      resultados: [],
    };
  },
  computed: {
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
