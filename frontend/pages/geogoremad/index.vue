<template>
  <div class="pagina-principal">
    <Mapa />
    <BienvenidaModal />
  </div>
</template>

<script>
import Mapa from "@/components/visor/mapa/Mapa.vue";
import BienvenidaModal from "@/components/visor/bienvenida/BienvenidaModal.vue";
export default {
  components: {
    Mapa,
    BienvenidaModal,
  },
  auth: false,
  layout: "visor",
};
</script>

<style scoped>
.pagina-principal {
  height: 100%;
}
</style>
