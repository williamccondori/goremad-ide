<template>
  <LLayerGroup>
    <LGeoJson
      v-for="capaActiva in capasActivas"
      :key="capaActiva.id"
      :geojson="capaActiva.geojson"
      :name="capaActiva.nombre"
      :opacity="capaActiva.transparencia"
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
      const capasGeojson = this.capasOperativas.filter(
        (capa) => capa.esGeojson
      );
      return capasGeojson.map((capa) => ({
        id: capa.id,
        origen: capa.geojson.origen,
        nombre: capa.geojson.nombre,
        descripcion: capa.geojson.descripcion,
        geojson: capa.geojson.geometria,
        estilo: capa.geojson.estilo,
        cuadroDelimitador: capa.geojson.cuadroDelimitador,
        transparencia: capa.geojson.transparencia,
        codigo: capa.geojson.codigo,
      }));
    },
  },
  methods: {
    ...mapActions('visor', [
      'abrirVentana',
      'establecerInformacionCapaGeojson',
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
        opacity: 1,
        weight: 3,
      });
    },
    reestablecerPoligono(e, estilosPorDefecto) {
      const capa = e.target;
      capa.setStyle(estilosPorDefecto);
    },
    async seleccionarPoligono(e, feature) {
      const capa = e.target;
      const identificador = capa?.options?.identificador;

      const capaGeojson = this.capasActivas.find(
        (capa) => capa.id === identificador
      );

      // Manejo de alias de propiedades.

      let propiedades = {};
      if (capaGeojson.origen === 'POSTGRESQL') {
        try {
          this.$iniciarCarga();
          const propiedadesAntiguas = feature.properties;
          const { data } = await this.$axios.get(
            `/visor/objetos-geograficos/${capaGeojson.id}/propiedades/?registro_id=${propiedadesAntiguas.id}`
          );
          propiedades = data;
        } catch (error) {
          this.$manejarError(error);
        } finally {
          this.$finalizarCarga();
        }
      } else {
        propiedades = feature.properties;
      }

      this.establecerInformacionCapaGeojson({
        nombre: capaGeojson.nombre,
        descripcion: capaGeojson.descripcion,
        codigo: capaGeojson.codigo,
        propiedades: propiedades,
        estilo: capaGeojson.estilo,
      });

      const cuadroDelimitador = capa.getBounds();
      this.establecerBounds(cuadroDelimitador);

      this.abrirVentana('InformacionCapaWfs');
    },
  },
};
</script>
