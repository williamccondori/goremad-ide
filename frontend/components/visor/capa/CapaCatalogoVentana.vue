<template>
  <a-drawer
    :width="esMovil ? '100%' : 400"
    :visible="estaAbiertoCapaVentana"
    @close="cerrarCapaVentana()"
  >
    <span slot="title" style="text-transform: uppercase">
      <b>Capas</b>
    </span>
    <a-tabs type="card">
      <a-tab-pane key="operables" tab="Capas">
        <a-tree
          checkable
          style="overflow-x: auto"
          :replace-fields="{
            key: 'id',
            title: 'label',
          }"
          :tree-data="capasEstructura"
          :default-checked-keys="capasActivas"
          :default-expanded-keys="capasActivas"
          :show-line="true"
          :selectable="false"
          :check-strictly="false"
          @check="seleccionarCapa"
        >
          <a-icon slot="switcherNode" type="folder" />
        </a-tree>
      </a-tab-pane>
      <a-tab-pane key="interoperables" tab="Capas interoperables">
        <a-alert
          message="Característica en construcción"
          description="Esta característica está en construcción. Pronto estará disponible."
          type="warning"
          show-icon
        />
        <!-- <a-tree
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
          :auto-expand-parent="true"
          @check="onCheck"
        /> -->
      </a-tab-pane>
    </a-tabs>
  </a-drawer>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  computed: {
    ...mapState(["esMovil"]),
    ...mapState("visor", [
      "estaAbiertoCapaVentana",
      "capasEstructura",
      "capas",
      "capasActivas",
      "capasInteroperablesEstructura",
      "capasInteroperablesActivas",
      "capasInteroperables",
    ]),
  },
  methods: {
    ...mapActions("visor", [
      "cerrarCapaVentana",
      "establecerCapasInteroperablesActivas",
      "establecerCapasActivas",
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
    seleccionarCapa(elementos) {
      const capasSeleccinadas = elementos.filter((elemento) => {
        return this.capas.find((capa) => capa.id === elemento);
      });
      this.establecerCapasActivas(capasSeleccinadas);
    },
  },
};
</script>
