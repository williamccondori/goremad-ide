<template>
  <AdministracionPagina>
    <a-space direction="vertical" class="app--w-100">
      <a-alert
        type="success"
        message="¡Bienvenido al módulo de administración del GEOGOREMAD!"
        description="Módulo de administración de contenidos de la plataforma geoespacial GEOGOREMAD."
        :closable="false"
      />
      <div v-if="resumen" class="contenedor">
        <a-card hoverable>
          <a-statistic
            :value="resumen.totalServiciosLocales"
            title="Total de servicios locales"
          />
        </a-card>
        <a-card hoverable>
          <a-statistic
            :value="resumen.totalCapasBase"
            title="Total de capas base"
          />
        </a-card>
        <a-card hoverable>
          <a-statistic
            :value="resumen.totalServiciosExternos"
            title="Total de servicios externos"
          />
        </a-card>
        <a-card hoverable>
          <a-statistic
            :value="resumen.totalUsuarios"
            title="Total de usuarios"
          />
        </a-card>
      </div>
    </a-space>
  </AdministracionPagina>
</template>

<script>
import { mapState, mapActions } from "vuex";
import AdministracionPagina from "@/components/administrador/compartido/AdministracionPagina.vue";
export default {
  components: {
    AdministracionPagina,
  },
  layout: "administrador",
  async fetch() {
    try {
      this.$iniciarCarga();
      await this.obtenerResumen();
    } catch (error) {
      this.$manejarError(error);
    } finally {
      this.$finalizarCarga();
    }
  },
  computed: {
    ...mapState("administrador", ["resumen"]),
  },
  methods: {
    ...mapActions("administrador", ["obtenerResumen"]),
  },
};
</script>

<style scoped>
.contenedor {
  gap: 1rem;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
}
</style>
