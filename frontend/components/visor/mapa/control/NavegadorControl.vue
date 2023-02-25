<script>
import { mapState } from "vuex";
import L from "leaflet";
import { findRealParent } from "vue2-leaflet";
import "leaflet-navbar";
import "leaflet-navbar/Leaflet.NavBar.css";
export default {
  computed: {
    ...mapState("visor", ["centro", "zoom"]),
  },
  mounted() {
    this.$nextTick(() => {
      const mapa = findRealParent(this.$parent).mapObject;
      // Configuracion del control.
      mapa.addControl(
        L.control.navbar({
          position: "topleft",
          zoom: this.zoom,
          center: this.centro,
          forwardTitle: "Ir al siguiente punto en el historial de navegación",
          backTitle: "Ir al punto anterior en el historial de navegación",
          homeTitle: "Ir al punto de inicio",
        })
      );
    });
  },
  render: () => ({}),
};
</script>
