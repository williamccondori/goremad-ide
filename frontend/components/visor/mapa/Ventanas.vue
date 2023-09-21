<template>
  <fragment>
    <VentanaCapasOperables />
    <VentanaCapasInteroperables />
    <VentanaInformacionCapasOperables />
    <VentanaResultadoInformacionCapasOperables />
    <VentanaSubirInformacion />
    <VentanaDescargarInformacion />
    <VentanaBuscar />
  </fragment>
</template>
<script>
import VentanaCapasOperables from './ventanas/VentanaCapasOperables.vue';
import VentanaCapasInteroperables from './ventanas/VentanaCapasInteroperables.vue';
import VentanaInformacionCapasOperables from './ventanas/VentanaInformacionCapasOperables.vue';
import VentanaResultadoInformacionCapasOperables from './ventanas/VentanaResultadoInformacionCapasOperables.vue';
import VentanaSubirInformacion from './ventanas/VentanaSubirInformacion.vue';
import VentanaDescargarInformacion from './ventanas/VentanaDescargarInformacion.vue';
import VentanaBuscar from './ventanas/VentanaBuscar.vue';
export default {
  components: {
    VentanaCapasOperables,
    VentanaCapasInteroperables,
    VentanaInformacionCapasOperables,
    VentanaResultadoInformacionCapasOperables,
    VentanaSubirInformacion,
    VentanaDescargarInformacion,
    VentanaBuscar,
  },
};
</script>
