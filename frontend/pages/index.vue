<template>
  <div style="height: 100%">
    <Mapa />
    <BienvenidaModal />
  </div>
</template>

<script>
import Mapa from '@/components/visor/mapa/Mapa.vue';
import BienvenidaModal from '@/components/visor/bienvenida/BienvenidaModal.vue';
export default {
  components: {
    Mapa,
    BienvenidaModal,
  },
  auth: false,
  layout: 'visor',
};
</script>
