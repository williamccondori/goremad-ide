<template>
  <div class="pagina-principal">
    <ACard shadow="never" :style="{ width: esMovil ? '100%' : '400px' }">
      <div style="text-align: center">
        <img alt="logo" src="/logo.png" width="150" />
      </div>
      <ADivider />
      <InicioSesionFormulario />
    </ACard>
  </div>
</template>

<script>
import { Card, Divider } from 'ant-design-vue';
import { mapState } from 'vuex';
import InicioSesionFormulario from '@/components/administrador/inicio-sesion/InicioSesionFormulario.vue';
export default {
  components: { ACard: Card, ADivider: Divider, InicioSesionFormulario },
  layout: 'administrador',
  computed: {
    ...mapState(['esMovil']),
  },
};
</script>

<style scoped>
.pagina-principal {
  height: 100%;
  display: grid;
  place-items: center;
}
</style>
