<template>
  <a-drawer
    width="25rem"
    :destroy-on-close="true"
    :visible="estaAbiertoCapaBaseVentana"
    @close="cerrarCapaBaseVentana()"
  >
    <span slot="title">
      <b>Capas base</b>
    </span>
    <div class="app--contenedor-vertical">
      <a-row type="flex" justify="space-between" align="middle">
        <span>Todos los elementos:</span>
        <a-tag color="green">
          {{ capasBase.length }}
        </a-tag>
      </a-row>
      <a-row :gutter="[16, 16]">
        <a-col v-for="capaBase in capasBase" :key="capaBase.id" :span="12">
          <CapaBaseTarjeta :capa-base="capaBase" />
        </a-col>
      </a-row>
    </div>
  </a-drawer>
</template>

<script>
import { mapState, mapActions } from "vuex";
import CapaBaseTarjeta from "@/components/visor/CapaBaseTarjeta.vue";
export default {
  components: {
    CapaBaseTarjeta,
  },
  computed: {
    ...mapState("visor", ["estaAbiertoCapaBaseVentana", "capasBase"]),
  },
  methods: {
    ...mapActions("visor", ["cerrarCapaBaseVentana"]),
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
