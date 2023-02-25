<template>
  <div class="pagina-principal">
    <a-card shadow="never" :style="{ width: esMovil ? '100%' : '400px' }">
      <div style="text-align: center">
        <img src="/logo.png" alt="logo" width="150" />
      </div>
      <a-divider />
      <InicioSesionFormulario />
    </a-card>
  </div>
</template>

<script>
import { mapState } from "vuex";
import InicioSesionFormulario from "@/components/administrador/inicio-sesion/InicioSesionFormulario.vue";
export default {
  components: { InicioSesionFormulario },
  layout: "administrador",
  computed: {
    ...mapState(["esMovil"]),
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
