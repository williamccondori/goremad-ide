<template>
  <a-drawer
    :visible="estaAbiertoVentanaCapasInteroperables"
    :width="tamanioVentana"
    @close="cerrarVentana('CapasInteroperables')"
  >
    <span slot="title">
      <b>Capas interoperables</b>
    </span>
    <a-space direction="vertical" style="width: 100%">
      <a-tabs default-active-key="capasExternas" type="card">
        <a-tab-pane key="capasExternas" tab="Capas externas">
          <a-tree
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
        </a-tab-pane>
      </a-tabs>
    </a-space>
  </a-drawer>
</template>

<script>
import { mapState, mapActions } from 'vuex';
export default {
  computed: {
    ...mapState(['tamanioVentana']),
    ...mapState('visor', [
      'estaAbiertoVentanaCapasInteroperables',
      'capas',
      'capasEstructura',
      'capasActivas',
      'capasInteroperablesEstructura',
      'capasInteroperablesActivas',
      'capasInteroperables',
    ]),
  },
  methods: {
    ...mapActions('visor', [
      'cerrarVentana',
      'establecerCapasInteroperablesActivas',
      'establecerCapasWmsActivas',
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
      this.establecerCapasWmsActivas(capasSeleccinadas);
    },
  },
};
</script>
