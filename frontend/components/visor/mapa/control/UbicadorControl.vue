<script>
import L from "leaflet";
import { findRealParent } from "vue2-leaflet";
import "leaflet.locatecontrol";
import "leaflet.locatecontrol/dist/L.Control.Locate.min.css";
export default {
  mounted() {
    this.$nextTick(() => {
      const mapa = findRealParent(this.$parent).mapObject;
      // Configuracion del control.
      mapa.addControl(
        L.control.locate({
          strings: {
            title: "Ir a mi ubicación",
            metersUnit: "metros",
            popup: "Estás en {distance} {unit} de este punto",
            locateIcon: "fa fa-map-marker",
          },
        })
      );
    });
  },
  render: () => ({}),
};
</script>

<style>
.leaflet-control-locate a .leaflet-control-locate-location-arrow {
  width: 0.8rem;
  height: 0.8rem;
  margin: 0.5rem;
}
</style>
