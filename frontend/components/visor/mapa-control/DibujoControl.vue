<script>
import L from "leaflet";
import { findRealParent } from "vue2-leaflet";

import "@/plugins/leaflet-draw.js";

export default {
  data() {
    return {
      mapa: undefined,
      editablesGrupoCapa: undefined,
    };
  },
  mounted() {
    this.$nextTick(() => {
      this.mapa = findRealParent(this.$parent).mapObject;
      this.iniciarDibujoControl();
    });
  },
  methods: {
    iniciarDibujoControl() {
      this.editablesGrupoCapa = new L.FeatureGroup();
      this.mapa.addLayer(this.editablesGrupoCapa);

      const dibujoControl = new L.Control.Draw({
        position: "topright",
        draw: {
          polyline: {
            shapeOptions: {
              color: "green",
            },
          },
          polygon: {
            allowIntersection: false,
            drawError: {
              color: "red",
              message: " ¡No se puede dibujar un polígono que se interseque!",
            },
            shapeOptions: {
              color: "green",
            },
          },
          rectangle: {
            shapeOptions: {
              color: "green",
              clickable: false,
            },
          },
          circle: false,
          circlemarker: false,
        },
        edit: {
          featureGroup: this.editablesGrupoCapa,
        },
      });
      this.mapa.addControl(dibujoControl);

      this.mapa.on("draw:created", (evento) => {
        const tipo = evento.layerType;
        const capa = evento.layer;

        if (tipo === "marker") {
          capa.bindPopup("¡Hola!");
        }

        this.editablesGrupoCapa.addLayer(capa);
      });
    },
  },
  render: () => ({}),
};
</script>
