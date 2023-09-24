<template>
  <div>
    <VentanaCapasOperables />
    <VentanaCapasInteroperables />
    <VentanaInformacionCapasOperables />
    <VentanaResultadoInformacionCapasOperables />
    <VentanaSubirInformacion />
    <VentanaDescargarInformacion />
    <VentanaBuscar />
    <VentanaInformacionCapaWfs />
  </div>
</template>
<script>
import VentanaCapasOperables from './ventanas/VentanaCapasOperables.vue';
import VentanaCapasInteroperables from './ventanas/VentanaCapasInteroperables.vue';
import VentanaInformacionCapasOperables from './ventanas/VentanaInformacionCapasOperables.vue';
import VentanaResultadoInformacionCapasOperables from './ventanas/VentanaResultadoInformacionCapasOperables.vue';
import VentanaSubirInformacion from './ventanas/VentanaSubirInformacion.vue';
import VentanaDescargarInformacion from './ventanas/VentanaDescargarInformacion.vue';
import VentanaBuscar from './ventanas/VentanaBuscar.vue';
import VentanaInformacionCapaWfs from './ventanas/VentanaInformacionCapaWfs.vue';
export default {
  components: {
    VentanaCapasOperables,
    VentanaCapasInteroperables,
    VentanaInformacionCapasOperables,
    VentanaResultadoInformacionCapasOperables,
    VentanaSubirInformacion,
    VentanaDescargarInformacion,
    VentanaBuscar,
    VentanaInformacionCapaWfs,
  },
};
</script>
