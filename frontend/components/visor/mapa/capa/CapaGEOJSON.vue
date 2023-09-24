<template>
  <LLayerGroup>
    <LGeoJson
      v-for="capaActiva in capasActivas"
      :key="capaActiva.id"
      :geojson="capaActiva.geojson"
      :name="capaActiva.nombre"
      :options="{
        identificador: capaActiva.id,
        style: capaActiva.estilo,
        onEachFeature: (feature, layer) =>
          onEachFeature(capaActiva.estilo, feature, layer),
      }"
    />
  </LLayerGroup>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import { LGeoJson, LLayerGroup } from 'vue2-leaflet';

export default {
  components: {
    LGeoJson,
    LLayerGroup,
  },
  data() {
    return {
      layerOptions: {
        onEachFeature: this.onEachFeature,
      },
    };
  },
  computed: {
    ...mapState('visor', ['capasOperativas']),
    capasActivas() {
      const capasWfs = this.capasOperativas.filter((capa) => capa.esVectorial);
      return capasWfs.map((capa) => ({
        id: capa.id,
        nombre: capa.wfs.nombre,
        geojson: capa.wfs.geometria,
        estilo: capa.wfs.estilo,
      }));
    },
  },
  methods: {
    ...mapActions('visor', [
      'abrirVentana',
      'establecerInformacionCapaWfs',
      'establecerBounds',
    ]),
    onEachFeature(estilosPorDefecto, feature, layer) {
      layer.setStyle(estilosPorDefecto);
      layer.on({
        mouseover: this.resaltarPoligono,
        mouseout: (e) => this.reestablecerPoligono(e, estilosPorDefecto),
        click: (e) => this.seleccionarPoligono(e, feature),
      });
    },
    resaltarPoligono(e) {
      const capa = e.target;
      capa.setStyle({
        color: '#00FFFF',
        fillColor: '#FFFFFF',
        fillOpacity: 0.5,
        lineJoin: 'bevel',
        opacity: 1,
        weight: 3,
      });
    },
    reestablecerPoligono(e, estilosPorDefecto) {
      const capa = e.target;
      capa.setStyle(estilosPorDefecto);
    },
    seleccionarPoligono(e, feature) {
      const capa = e.target;
      const identificador = capa?.options?.identificador;

      const capaGEOJSON = this.capasActivas.find(
        (capa) => capa.id === identificador
      );
      this.establecerInformacionCapaWfs({
        nombre: capaGEOJSON.nombre,
        propiedades: feature.properties,
      });

      const cuadroDelimitador = capa.getBounds();
      this.establecerBounds(cuadroDelimitador);

      this.abrirVentana('InformacionCapaWfs');
    },
  },
};
</script>
