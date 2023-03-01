<template>
  <ADrawer
    :width="esMovil ? '100%' : 400"
    :visible="estaAbiertoCapaBaseCatalogoVentana"
    @close="cerrarCapaBaseCatalogoVentana()"
  >
    <span slot="title" style="text-transform: uppercase">
      <b>Capas base</b>
    </span>
    <div class="app--contenedor-vertical">
      <ARow type="flex" justify="space-between" align="middle">
        <span>Todos los elementos:</span>
        <ATag color="green">
          {{ capasBase.length }}
        </ATag>
      </ARow>
      <ARow :gutter="[16, 16]">
        <ACol v-for="capaBase in capasBase" :key="capaBase.id" :span="12">
          <CapaBasePrevisualizacion :capa-base="capaBase" />
        </ACol>
      </ARow>
    </div>
  </ADrawer>
</template>

<script>
import { Drawer, Tag, Row, Col } from "ant-design-vue";
import { mapState, mapActions } from "vuex";
import CapaBasePrevisualizacion from "~/components/visor/capa-base/CapaBasePrevisualizacion.vue";
export default {
  components: {
    ADrawer: Drawer,
    ATag: Tag,
    ARow: Row,
    ACol: Col,
    CapaBasePrevisualizacion,
  },
  computed: {
    ...mapState(["esMovil"]),
    ...mapState("visor", ["estaAbiertoCapaBaseCatalogoVentana", "capasBase"]),
  },
  methods: {
    ...mapActions("visor", ["cerrarCapaBaseCatalogoVentana"]),
  },
};
</script>

<style scoped>
.contenedor {
  gap: 0.5rem;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
}
</style>
