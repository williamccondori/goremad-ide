<template>
  <div style="height: 100%">
    <client-only>
      <LMap
        :max-zoom="18"
        :min-zoom="3"
        :options="{ preferCanvas: true }"
        style="outline: none"
        @ready="inicializarMapa"
      >
        <ControlInformacion />
        <ControlHerramientas />
        <ControlImpresion />
        <InformacionPosicionControl />
        <LControlScale :max-width="200" position="bottomleft" />
        <ControlLogo />
        <MiniMapaControl />
        <PantallaCompletaControl />
        <NavegadorControl />
        <UbicadorControl />
        <CapaMapaBase />
        <CapaGeojson />
        <CapaCapa />
        <CapaDetallePopup />
      </LMap>
    </client-only>
    <Ventanas />
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
/* ================================================================================================================ */
import ControlInformacion from './controles/ControlInformacion.vue';
import ControlHerramientas from './controles/ControlHerramientas.vue';
import ControlImpresion from './controles/ControlImpresion.vue';
import ControlLogo from './controles/ControlLogo.vue';
/* ================================================================================================================ */
import Ventanas from './Ventanas.vue';
/* ================================================================================================================ */
import InformacionPosicionControl from '@/components/visor/mapa/control/InformacionPosicionControl.vue';
import MiniMapaControl from '@/components/visor/mapa/control/MiniMapaControl.vue';
import NavegadorControl from '@/components/visor/mapa/control/NavegadorControl.vue';
import PantallaCompletaControl from '@/components/visor/mapa/control/PantallaCompletaControl.vue';
import UbicadorControl from '@/components/visor/mapa/control/UbicadorControl.vue';
import CapaMapaBase from './capas/CapaMapaBase.vue';
import CapaGeojson from './capas/CapaGeojson.vue';
import CapaCapa from '@/components/visor/mapa/capa/CapaCapa.vue';
import CapaDetallePopup from '@/components/visor/capa/CapaDetallePopup.vue';
export default {
  components: {
    LMap,
    LControlScale,
    InformacionPosicionControl,
    MiniMapaControl,
    ControlLogo,
    NavegadorControl,
    PantallaCompletaControl,
    UbicadorControl,
    CapaMapaBase,
    CapaCapa,
    CapaDetallePopup,
    Ventanas,
    CapaGeojson,
    ControlHerramientas,
    ControlInformacion,
    ControlImpresion,
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
