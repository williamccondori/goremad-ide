<template>
  <ADrawer
    :width="esMovil ? '100%' : 400"
    :visible="estaAbiertoComparacionVentana"
    @close="cerrarComparacionVentana()"
  >
    <span slot="title" style="text-transform: uppercase">
      <b>Comparar capas activas</b>
    </span>
    <AFormModel
      ref="referenciaFormulario"
      :model="formulario"
      @submit.prevent="comparar()"
    >
      <AFormModelItem
        label="Capa de la izquierda"
        prop="capaIzquierda"
        :rules="[
          {
            required: true,
            message: 'Seleccione la capa de la izquierda',
          },
        ]"
      >
        <ASelect
          v-model="formulario.capaIzquierda"
          placeholder="Seleccione  la capa de la izquierda"
        >
          <ASelectOption
            v-for="elemento in elementosActivos"
            :key="elemento.id"
            :value="elemento.id"
          >
            {{ elemento.titulo }}
          </ASelectOption>
        </ASelect>
      </AFormModelItem>
      <AFormModelItem
        label="Capa de la derecha"
        prop="capaDerecha"
        :rules="[
          {
            required: true,
            message: 'Seleccione la capa de la derecha',
          },
        ]"
      >
        <ASelect
          v-model="formulario.capaDerecha"
          placeholder="Seleccione  la capa de la derecha"
        >
          <ASelectOption
            v-for="elemento in elementosActivos"
            :key="elemento.id"
            :value="elemento.id"
          >
            {{ elemento.titulo }}
          </ASelectOption>
        </ASelect>
      </AFormModelItem>
      <div>
        <AButton html-type="submit" type="primary" icon="check" block>
          Comparar
        </AButton>
      </div>
    </AFormModel>
  </ADrawer>
</template>

<script>
import { Drawer, FormModel, Select, Button } from "ant-design-vue";
import { mapState, mapActions } from "vuex";

const formulario = {
  capaIzquierda: undefined,
  capaDerecha: undefined,
};

export default {
  components: {
    ADrawer: Drawer,
    AFormModel: FormModel,
    AFormModelItem: FormModel.Item,
    ASelect: Select,
    ASelectOption: Select.Option,
    AButton: Button,
  },
  data() {
    return {
      formulario: { ...formulario },
    };
  },
  computed: {
    ...mapState(["esMovil"]),
    ...mapState("visor", [
      "estaAbiertoComparacionVentana",
      "capas",
      "capasActivas",
    ]),
    elementosActivos() {
      return this.capas.filter((capa) => this.capasActivas.includes(capa.id));
    },
  },
  watch: {
    estaAbiertoComparacionVentana(valor) {
      if (!valor) {
        this.formulario = { ...formulario };
        this.$refs.referenciaFormulario?.resetFields();
      }
    },
  },
  methods: {
    ...mapActions("visor", ["cerrarComparacionVentana"]),
    comparar() {
      this.$refs.referenciaFormulario?.validate((valid) => {
        if (valid) {
          try {
            this.$iniciarCarga();
            if (this.formulario.capaIzquierda === this.formulario.capaDerecha) {
              this.$mostrarMensajeAdvertencia(
                "No puede comparar la misma capa en ambas posiciones"
              );
              return;
            }
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
