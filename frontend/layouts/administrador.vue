<template>
  <div class="app--pagina">
    <a-spin :spinning="estaCargando">
      <div class="contenedor-principal">
        <AplicacionCabecera />
        <a-layout style="background: none">
          <AdministracionMenu v-if="$auth.loggedIn" />
          <a-layout-content style="padding: 1rem">
            <nuxt />
          </a-layout-content>
        </a-layout>
      </div>
    </a-spin>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import AplicacionCabecera from "@/components/compartido/AplicacionCabecera.vue";
import AdministracionMenu from "@/components/administrador/compartido/AdministracionMenu.vue";
export default {
  components: {
    AplicacionCabecera,
    AdministracionMenu,
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
  },
};
</script>

<style scoped>
.contenedor-principal {
  min-height: 100%;
  display: grid;
  grid-template-rows: var(--altura-cabecera) 1fr;
  background-size: 5px 5px;
  background-image: radial-gradient(
    hsla(215 28% 17% / 0.2) 0.5px,
    hsla(0 0% 95% / 1) 0.5px
  );
}
</style>
