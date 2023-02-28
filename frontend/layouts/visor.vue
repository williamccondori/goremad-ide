<template>
  <div v-if="configuracionAplicada" class="app--pagina">
    <ASpin :spinning="estaCargando">
      <div class="contenedor-principal">
        <AplicacionCabecera />
        <nuxt />
      </div>
    </ASpin>
  </div>
  <div v-else class="app--pagina">
    <PaginaCarga />
  </div>
</template>

<script>
import { Spin } from "ant-design-vue";
import { mapState, mapActions } from "vuex";
import AplicacionCabecera from "@/components/compartido/AplicacionCabecera.vue";
import PaginaCarga from "@/components/visor/compartido/PaginaCarga.vue";
export default {
  components: { ASpin: Spin, AplicacionCabecera, PaginaCarga },
  data() {
    return {
      configuracionAplicada: false,
    };
  },
  async fetch() {
    try {
      const { data } = await this.$axios.get("/visor/iniciales/");
      const configuracionInicial = data;
      if (configuracionInicial) {
        this.configuracionAplicada = true;
        // Se establece la posicion inicial de la vista del mapa.
        this.establecerCentro([
          configuracionInicial.latitudInicial,
          configuracionInicial.longitudInicial,
        ]);
        this.establecerZoom(configuracionInicial.zoomInicial);
        // Se establece la informacion de las capas base.
        this.establecerCapasBase(configuracionInicial.capasBase);
        this.establecerCapaBaseActiva(configuracionInicial.capaBaseIncialId);
        // Se establece la informacion de las capas.
        this.establacerCapas(configuracionInicial.serviciosExternos);
        this.establecerCapasActivas(configuracionInicial.capasActivas);
        // Se establce la estructura de arbol de las capas.
        this.establecerCapasEstructura(configuracionInicial.estructura);
      }
    } catch (error) {
      this.$manejarError(error);
    }
  },
  computed: {
    ...mapState(["estaCargando"]),
  },
  mounted() {
    window.addEventListener("resize", () => {
      this.establecerEsMovil(window.innerWidth < 720);
    });
  },
  methods: {
    ...mapActions(["establecerEsMovil"]),
    ...mapActions("visor", [
      "establecerCentro",
      "establecerZoom",
      "establecerCapasBase",
      "establecerCapaBaseActiva",
      "establacerCapas",
      "establecerCapasActivas",
      "establecerCapasEstructura",
    ]),
  },
};
</script>

<style scoped>
.contenedor-principal {
  height: 100%;
  display: grid;
  grid-template-rows: var(--altura-cabecera) 1fr;
}
</style>
