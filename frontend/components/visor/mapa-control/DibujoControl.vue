<script>
import { findRealParent } from "vue2-leaflet";
import "@geoman-io/leaflet-geoman-free";
import "@geoman-io/leaflet-geoman-free/dist/leaflet-geoman.css";

export default {
  data() {
    return {
      esGrupo: false,
    };
  },
  mounted() {
    this.$nextTick(() => {
      const mapa = findRealParent(this.$parent).mapObject;
      mapa.pm.setLang("es");
      mapa.on("pm:create", (e) => {
        const geojson = e.layer.toGeoJSON();
        console.log(geojson);
      });
      mapa.pm.addControls({
        position: "topright",
        drawCircle: false,
        drawRectangle: false,
        drawCircleMarker: false,
        drawText: false,
        cutPolygon: false,
        rotateMode: false,
      });
    });
  },
  render: () => ({}),
};
</script>
