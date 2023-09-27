<template>
  <div style="height: 100%">
    <client-only>
      <LMap
        ref="referenciaMapa"
        :max-zoom="18"
        :min-zoom="3"
        :options="{ preferCanvas: true }"
        style="outline: none"
        @ready="inicializarMapa"
      >
        <!--Controles.-->

        <InformacionControl />
        <HerramientasControl />

        <InformacionPosicionControl />
        <LControlScale :max-width="200" position="bottomleft" />
        <LogoControl />
        <MiniMapaControl />
        <PantallaCompletaControl />
        <NavegadorControl />
        <UbicadorControl />
        <!--Capas.-->
        <CapaGEOJSON />
        <CapaBaseCapa />
        <CapaCapa />
        <!--Adicionales.-->
        <CapaDetallePopup />
        <ImpresionControl />
      </LMap>
    </client-only>
    <Ventanas />
    <CapaResumenVentana />
    <CompartirModal />
    <MarcadorCatalogoVentana />
    <CapaBaseCatalogoVentana />
    <ImagenSatelitalCatalogoVentana />
    <ComparacionVentana />
  </div>
</template>

<script>
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import { LMap, LControlScale } from 'vue2-leaflet';
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});
import { mapState, mapActions } from 'vuex';
// Controles.
import InformacionPosicionControl from '@/components/visor/mapa/control/InformacionPosicionControl.vue';
import MiniMapaControl from '@/components/visor/mapa/control/MiniMapaControl.vue';
import LogoControl from '@/components/visor/mapa/control/LogoControl.vue';
import NavegadorControl from '@/components/visor/mapa/control/NavegadorControl.vue';
import PantallaCompletaControl from '@/components/visor/mapa/control/PantallaCompletaControl.vue';
import UbicadorControl from '@/components/visor/mapa/control/UbicadorControl.vue';
// Capas.
import CapaBaseCapa from '@/components/visor/mapa/capa/CapaBaseCapa.vue';
import CapaCapa from '@/components/visor/mapa/capa/CapaCapa.vue';
// Adicionales.
import CapaDetallePopup from '@/components/visor/capa/CapaDetallePopup.vue';
// import CapasInteroperablesLayer from "@/components/visor/CapasInteroperablesLayer.vue";
// Ventanas.
import Ventanas from './Ventanas.vue';
import CapaResumenVentana from '@/components/visor/capa/CapaResumenVentana.vue';
import MarcadorCatalogoVentana from '@/components/visor/marcador/MarcadorCatalogoVentana.vue';
import CompartirModal from '@/components/visor/compartir/CompartirModal.vue';
import CapaBaseCatalogoVentana from '@/components/visor/capa-base/CapaBaseCatalogoVentana.vue';
import ImagenSatelitalCatalogoVentana from '@/components/visor/imagen-satelital/ImagenSatelitalCatalogoVentana.vue';
import ComparacionVentana from '@/components/visor/comparacion/ComparacionVentana.vue';
import CapaGEOJSON from './capa/CapaGEOJSON.vue';
import HerramientasControl from './control/HerramientasControl.vue';
import InformacionControl from './control/InformacionControl.vue';
import ImpresionControl from './control/ImpresionControl.vue';

export default {
  components: {
    LMap,
    LControlScale,
    InformacionPosicionControl,
    MiniMapaControl,
    LogoControl,
    NavegadorControl,
    PantallaCompletaControl,
    UbicadorControl,
    CapaBaseCapa,
    CapaCapa,
    CapaDetallePopup,
    Ventanas,
    CapaResumenVentana,
    MarcadorCatalogoVentana,
    CompartirModal,
    CapaBaseCatalogoVentana,
    ImagenSatelitalCatalogoVentana,
    ComparacionVentana,
    CapaGEOJSON,
    HerramientasControl,
    InformacionControl,
    ImpresionControl,
  },

  data() {
    return {
      mapa: undefined,
    };
  },
  computed: {
    ...mapState('visor', ['centro', 'zoom', 'bounds']),
  },
  watch: {
    centro(valor) {
      this.mapa.setView(valor, this.zoom);
    },
    zoom(valor) {
      this.mapa.setView(this.centro, valor);
    },
    bounds(valor) {
      if (valor) {
        this.mapa.fitBounds(valor);
      }
    },
  },
  methods: {
    ...mapActions('visor', ['establecerInformacionPosicion']),
    inicializarMapa(mapa) {
      this.mapa = mapa;
      this.mapa.setView(this.centro, this.zoom);
      this.mapa.on('moveend', this.onMoveEnd);
      this.mapa.on('zoomend', this.onZoomEnd);
      this.establecerInformacionPosicion({
        latitud: this.centro.lat,
        longitud: this.centro.lng,
        zoom: this.zoom,
      });
    },
    onMoveEnd() {
      if (this.mapa) {
        const centro = this.mapa.getCenter();
        this.establecerInformacionPosicion({
          latitud: centro.lat,
          longitud: centro.lng,
        });
      }
    },
    onZoomEnd() {
      if (this.mapa) {
        const zoom = this.mapa.getZoom();
        this.establecerInformacionPosicion({
          zoom,
        });
      }
    },
  },
};
</script>
