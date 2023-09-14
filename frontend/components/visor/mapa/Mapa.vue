<template>
  <div style="height: 100vh">
    <client-only>
      <LMap
        ref="referenciaMapa"
        :max-zoom="18"
        :min-zoom="3"
        :options="{ preferCanvas: true }"
        @ready="inicializarMapa"
      >
        <!--Controles.-->
        <HerramientasControl />
        <InformacionControl />
        <UtilidadesControl />
        <InformacionPosicionControl />
        <LControlScale :max-width="200" position="bottomleft" />
        <LogoControl />
        <MiniMapaControl />
        <PantallaCompletaControl />
        <NavegadorControl />
        <UbicadorControl />
        <DibujoControl />
        <!--Capas.-->
        <CapaGEOJSON />
        <CapaBaseCapa />
        <CapaCapa />
        <ComparacionCapa />
        <!--Adicionales.-->
        <CapaDetallePopup />
      </LMap>
    </client-only>
    <Ventanas />
    <CapaCatalogoVentana />
    <CapaResumenVentana />
    <UbicacionVentana />
    <CoordenadaVentana />
    <DibujoVentana />
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
import HerramientasControl from '@/components/visor/mapa/control/HerramientasControl.vue';
import InformacionPosicionControl from '@/components/visor/mapa/control/InformacionPosicionControl.vue';
import MiniMapaControl from '@/components/visor/mapa/control/MiniMapaControl.vue';
import LogoControl from '@/components/visor/mapa/control/LogoControl.vue';
import NavegadorControl from '@/components/visor/mapa/control/NavegadorControl.vue';
import PantallaCompletaControl from '@/components/visor/mapa/control/PantallaCompletaControl.vue';
import UbicadorControl from '@/components/visor/mapa/control/UbicadorControl.vue';
import UtilidadesControl from '@/components/visor/mapa/control/UtilidadesControl.vue';
import DibujoControl from '@/components/visor/mapa-control/DibujoControl.vue';
// Capas.
import CapaBaseCapa from '@/components/visor/mapa/capa/CapaBaseCapa.vue';
import CapaCapa from '@/components/visor/mapa/capa/CapaCapa.vue';
import ComparacionCapa from '@/components/visor/mapa/capa/ComparacionCapa.vue';
// Adicionales.
import CapaDetallePopup from '@/components/visor/capa/CapaDetallePopup.vue';
// import CapasInteroperablesLayer from "@/components/visor/CapasInteroperablesLayer.vue";
// Ventanas.
import Ventanas from './Ventanas.vue';
import CapaResumenVentana from '@/components/visor/capa/CapaResumenVentana.vue';
import CapaCatalogoVentana from '@/components/visor/capa/CapaCatalogoVentana.vue';
import UbicacionVentana from '@/components/visor/ubicacion/UbicacionVentana.vue';
import CoordenadaVentana from '@/components/visor/coordenada/CoordenadaVentana.vue';
import DibujoVentana from '@/components/visor/dibujo/DibujoVentana.vue';
import MarcadorCatalogoVentana from '@/components/visor/marcador/MarcadorCatalogoVentana.vue';
import CompartirModal from '@/components/visor/compartir/CompartirModal.vue';
import CapaBaseCatalogoVentana from '@/components/visor/capa-base/CapaBaseCatalogoVentana.vue';
import ImagenSatelitalCatalogoVentana from '@/components/visor/imagen-satelital/ImagenSatelitalCatalogoVentana.vue';
import ComparacionVentana from '@/components/visor/comparacion/ComparacionVentana.vue';
import CapaGEOJSON from './capa/CapaGEOJSON.vue';
import InformacionControl from './control/InformacionControl.vue';

export default {
  components: {
    LMap,
    LControlScale,
    // Controles.
    HerramientasControl,
    InformacionPosicionControl,
    MiniMapaControl,
    LogoControl,
    NavegadorControl,
    PantallaCompletaControl,
    UbicadorControl,
    UtilidadesControl,
    DibujoControl,
    // Capas.
    CapaBaseCapa,
    CapaCapa,
    ComparacionCapa,
    // Adicionales
    CapaDetallePopup,
    // CapasInteroperablesLayer,
    // Ventanas.
    Ventanas,
    CapaResumenVentana,
    CapaCatalogoVentana,
    UbicacionVentana,
    CoordenadaVentana,
    DibujoVentana,
    MarcadorCatalogoVentana,
    CompartirModal,
    CapaBaseCatalogoVentana,
    ImagenSatelitalCatalogoVentana,
    ComparacionVentana,
    CapaGEOJSON,
    InformacionControl,
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
