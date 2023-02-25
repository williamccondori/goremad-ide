<template>
  <BaseColapsable title="Interoperabilidad" icon="globe">
    <a-button
      html-type="button"
      type="dashed"
      block
      @click="abrirWebMapServiceFormularioVentana()"
    >
      Agregar Web Map Service
    </a-button>
    <a-divider />
    <a-tree
      checkable
      style="overflow-x: auto"
      :replace-fields="{
        key: 'id',
        title: 'label',
      }"
      :tree-data="capasInteroperablesEstructura"
      :default-checked-keys="capasInteroperablesActivas"
      :show-line="true"
      :selectable="false"
      :check-strictly="true"
      @check="onCheck"
    />
    <WebMapServiceFormularioVentana />
  </BaseColapsable>
</template>

<script>
import { mapState, mapActions } from "vuex";
import BaseColapsable from "@/components/visor/BaseColapsable.vue";
import WebMapServiceFormularioVentana from "./WebMapServiceFormularioVentana.vue";
export default {
  components: { BaseColapsable, WebMapServiceFormularioVentana },
  computed: {
    ...mapState("visor", [
      "capasInteroperablesEstructura",
      "capasInteroperablesActivas",
      "capasInteroperables",
    ]),
  },
  methods: {
    ...mapActions("visor", [
      "abrirWebMapServiceFormularioVentana",
      "establecerCapasInteroperablesActivas",
    ]),
    onCheck({ checked }) {
      const capasInteroperablesSeleccinadas = checked.filter((elemento) => {
        return this.capasInteroperables.find(
          (capaInteroperable) => capaInteroperable.id === elemento
        );
      });
      this.establecerCapasInteroperablesActivas(
        capasInteroperablesSeleccinadas
      );
    },
  },
};
</script>
