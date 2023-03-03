<template>
  <AdministracionPagina>
    <ASpace direction="vertical" class="app--w-100">
      <AAlert
        type="success"
        message="¡Bienvenido al módulo de administración del GEOGOREMAD!"
        description="Módulo de administración de contenidos de la plataforma geoespacial GEOGOREMAD."
        :closable="false"
      />
      <div v-if="resumen" class="contenedor">
        <ACard hoverable>
          <AStatistic
            :value="resumen.totalServiciosLocales"
            title="Total de servicios locales"
          />
        </ACard>
        <ACard hoverable>
          <AStatistic
            :value="resumen.totalCapasBase"
            title="Total de capas base"
          />
        </ACard>
        <ACard hoverable>
          <AStatistic
            :value="resumen.totalServiciosExternos"
            title="Total de servicios externos"
          />
        </ACard>
        <ACard hoverable>
          <AStatistic
            :value="resumen.totalUsuarios"
            title="Total de usuarios"
          />
        </ACard>
      </div>
    </ASpace>
  </AdministracionPagina>
</template>

<script>
import { Card, Statistic, Space, Alert } from "ant-design-vue";
import { mapState, mapActions } from "vuex";
import AdministracionPagina from "@/components/administrador/compartido/AdministracionPagina.vue";
export default {
  components: {
    ACard: Card,
    AStatistic: Statistic,
    ASpace: Space,
    AAlert: Alert,
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
