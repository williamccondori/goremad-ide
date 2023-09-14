<template>
  <AdministracionPagina>
    <ASpace class="app--w-100" direction="vertical">
      <AAlert
        :closable="false"
        description="Módulo de administración de contenidos de la plataforma geoespacial GEOGOREMAD."
        message="¡Bienvenido al módulo de administración del GEOGOREMAD!"
        type="success"
      />
      <div v-if="resumen" class="contenedor">
        <ACard hoverable>
          <AStatistic
            title="Total de servicios locales"
            :value="resumen.totalServiciosLocales"
          />
        </ACard>
        <ACard hoverable>
          <AStatistic
            title="Total de capas base"
            :value="resumen.totalCapasBase"
          />
        </ACard>
        <ACard hoverable>
          <AStatistic
            title="Total de servicios externos"
            :value="resumen.totalServiciosExternos"
          />
        </ACard>
        <ACard hoverable>
          <AStatistic
            title="Total de usuarios"
            :value="resumen.totalUsuarios"
          />
        </ACard>
      </div>
    </ASpace>
  </AdministracionPagina>
</template>

<script>
import { Card, Statistic, Space, Alert } from 'ant-design-vue';
import { mapState, mapActions } from 'vuex';
import AdministracionPagina from '@/components/administrador/compartido/AdministracionPagina.vue';
export default {
  components: {
    ACard: Card,
    AStatistic: Statistic,
    ASpace: Space,
    AAlert: Alert,
    AdministracionPagina,
  },
  layout: 'administrador',
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
    ...mapState('administrador', ['resumen']),
  },
  methods: {
    ...mapActions('administrador', ['obtenerResumen']),
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
