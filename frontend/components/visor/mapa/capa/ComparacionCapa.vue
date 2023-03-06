<script>
import L from "leaflet";
import { findRealParent } from "vue2-leaflet";
import "leaflet.fullscreen";
import "leaflet.fullscreen/Control.FullScreen.css";
export default {
  props: {
    capasComparables: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      mapa: null,
      comparadorControl: null,
    };
  },
  mounted() {
    this.$nextTick(() => {
      this.mapa = findRealParent(this.$parent).mapObject;
      if (this.capasComparables.length > 0) {
        this.comparadorControl = L.control.sideBySide();
        this.comparadorControl.addTo(this.mapa);
      }
    });
  },
  render: () => ({}),
};
</script>
