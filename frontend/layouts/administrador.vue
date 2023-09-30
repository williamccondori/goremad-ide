<template>
  <div class="app--pagina">
    <ASpin :spinning="estaCargando">
      <div class="contenedor-principal">
        <Cabecera />
        <ALayout style="background: none">
          <AdministracionMenu v-if="$auth.loggedIn" />
          <ALayoutContent style="padding: 1rem">
            <nuxt />
          </ALayoutContent>
        </ALayout>
      </div>
    </ASpin>
  </div>
</template>

<script>
import { Spin, Layout } from 'ant-design-vue';
import { mapState, mapActions } from 'vuex';
import Cabecera from '@/components/compartido/Cabecera.vue';
import AdministracionMenu from '@/components/administrador/compartido/AdministracionMenu.vue';
export default {
  components: {
    ASpin: Spin,
    ALayout: Layout,
    ALayoutContent: Layout.Content,
    Cabecera,
    AdministracionMenu,
  },
  computed: {
    ...mapState(['estaCargando']),
  },
  mounted() {
    window.addEventListener('resize', () => {
      this.establecerEsMovil(window.innerWidth < 720);
    });
  },
  methods: {
    ...mapActions(['establecerEsMovil']),
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
