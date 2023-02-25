<template>
  <BaseColapsable title="Capas" icon="layer" :collapse="false">
    <div class="app--contenedor-vertical">
      <a-input-search placeholder="Buscar..." @change="buscar" />
      <a-tree
        checkable
        :tree-data="capasEstructura"
        :replace-fields="{
          key: 'id',
          title: 'label',
        }"
        :selectable="false"
        :check-strictly="true"
      />
      <a-button
        block
        html-type="button"
        type="danger"
        icon="delete"
        :disabled="capasActivas.length === 0"
        @click="limpiarCapasActivas()"
      >
        Limpiar capas activas
      </a-button>
    </div>
  </BaseColapsable>
</template>

<script>
import { mapState, mapActions } from "vuex";
import BaseColapsable from "@/components/visor/BaseColapsable.vue";

export default {
  components: { BaseColapsable },
  data() {
    return {
      query: "",
    };
  },
  computed: {
    ...mapState("visor", ["capasEstructura", "capasActivas"]),
  },
  watch: {
    capasActivas(valor) {
      //this.$refs.referenciaEstructura?.setCheckedKeys(valor);
    },
  },
  methods: {
    ...mapActions("visor", ["cerrarCapaDrawer", "establecerCapasActivas"]),
    buscar(e) {
      const valor = e.target.value;
    },
    onCheck(capa) {},
    toggleCapasActivas(capaId) {},
    limpiarCapasActivas() {
      this.establecerCapasActivas([]);
    },
  },
};
</script>
