<template>
  <ADrawer
    :visible="estaAbiertoCapaCatalogoVentana"
    :width="esMovil ? '100%' : 400"
    @close="cerrarCapaCatalogoVentana()"
  >
    <span slot="title" style="text-transform: uppercase">
      <b>Capas</b>
    </span>
    <ATabs type="card">
      <ATabPane key="operables" tab="Capas">
        <ATree
          :check-strictly="false"
          checkable
          :default-checked-keys="capasActivas"
          :default-expanded-keys="capasActivas"
          :replace-fields="{
            key: 'id',
            title: 'label',
          }"
          :selectable="false"
          :show-line="true"
          style="overflow-x: auto"
          :tree-data="capasEstructura"
          @check="seleccionarCapa"
        />
      </ATabPane>
      <ATabPane key="interoperables" tab="Capas interoperables">
        <AAlert
          description="Esta característica está en construcción. Pronto estará disponible."
          message="Característica en construcción"
          type="warning"
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
      </ATabPane>
    </ATabs>
  </ADrawer>
</template>

<script>
import { Drawer, Tabs, Alert, Tree } from 'ant-design-vue';
import { mapState, mapActions } from 'vuex';
export default {
  components: {
    ADrawer: Drawer,
    ATabs: Tabs,
    ATabPane: Tabs.TabPane,
    AAlert: Alert,
    ATree: Tree,
  },
  computed: {
    ...mapState(['esMovil']),
    ...mapState('visor', [
      'estaAbiertoCapaCatalogoVentana',
      'capasEstructura',
      'capas',
      'capasActivas',
      'capasInteroperablesEstructura',
      'capasInteroperablesActivas',
      'capasInteroperables',
    ]),
  },
  methods: {
    ...mapActions('visor', [
      'cerrarCapaCatalogoVentana',
      'establecerCapasInteroperablesActivas',
      'establecerCapasActivas',
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
