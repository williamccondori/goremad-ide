<template>
  <div>
    <VentanaCapasOperables />
    <VentanaCapasInteroperables />
    <VentanaInformacionCapasOperables />
    <VentanaResultadoInformacionCapasOperables />
  </div>
</template>
<script>
import VentanaCapasOperables from './ventanas/VentanaCapasOperables.vue';
import VentanaCapasInteroperables from './ventanas/VentanaCapasInteroperables.vue';
import VentanaInformacionCapasOperables from './ventanas/VentanaInformacionCapasOperables.vue';
import VentanaResultadoInformacionCapasOperables from './ventanas/VentanaResultadoInformacionCapasOperables.vue';
export default {
  components: {
    VentanaCapasOperables,
    VentanaCapasInteroperables,
    VentanaInformacionCapasOperables,
    VentanaResultadoInformacionCapasOperables,
  },
};
</script>
