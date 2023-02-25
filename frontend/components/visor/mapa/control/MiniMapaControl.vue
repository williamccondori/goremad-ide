<script>
import { mapState } from "vuex";
import L from "leaflet";
import { findRealParent } from "vue2-leaflet";
import MiniMap from "leaflet-minimap";
import "leaflet-minimap/dist/Control.MiniMap.min.css";
export default {
  data() {
    return {
      tileLayer: undefined,
    };
  },
  computed: {
    ...mapState(["esMovil"]),
    ...mapState("visor", ["capasBase", "capaBaseActiva"]),
    capaBaseActivaUrl() {
      const elementosActivos = this.capasBase.filter(
        (elemento) => elemento.id === this.capaBaseActiva
      );
      return elementosActivos.length === 0
        ? undefined
        : elementosActivos[0].url;
    },
  },
  watch: {
    capaBaseActivaUrl(valor) {
      if (valor) {
        this.tileLayer.setUrl(valor);
      }
    },
  },
  mounted() {
    this.$nextTick(() => {
      const mapa = findRealParent(this.$parent).mapObject;
      // Configuracion del control.
      this.tileLayer = L.tileLayer(this.capaBaseActivaUrl);
      mapa.addControl(
        new MiniMap(this.tileLayer, {
          toggleDisplay: true,
          minimized: this.esMovil,
          strings: {
            hideText: "Ocultar Mini Mapa",
            showText: "Mostrar Mini Mapa",
          },
        })
      );
    });
  },
  render: () => ({}),
};
</script>
