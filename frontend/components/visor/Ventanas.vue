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

    <CapaResumenVentana />
    <CompartirModal />
    <MarcadorCatalogoVentana />
    <CapaBaseCatalogoVentana />
    <ImagenSatelitalCatalogoVentana />
    <ComparacionVentana />
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
import CompartirModal from './compartir/CompartirModal.vue';
import MarcadorCatalogoVentana from './marcador/MarcadorCatalogoVentana.vue';
import CapaBaseCatalogoVentana from './capa-base/CapaBaseCatalogoVentana.vue';
import ImagenSatelitalCatalogoVentana from './imagen-satelital/ImagenSatelitalCatalogoVentana.vue';
import ComparacionVentana from './comparacion/ComparacionVentana.vue';
import CapaResumenVentana from './capa/CapaResumenVentana.vue';
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
    CompartirModal,
    MarcadorCatalogoVentana,
    CapaBaseCatalogoVentana,
    ImagenSatelitalCatalogoVentana,
    ComparacionVentana,
    CapaResumenVentana,
  },
};
</script>
