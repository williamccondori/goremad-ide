<template>
  <LLayerGroup>
    <LGeoJson
      v-for="elemento in elementosActivos"
      :key="elemento.id"
      :attribution="atribucionGeneral"
      :geojson="elemento.geojson"
      layer-type="overlay"
      :name="elemento.nombre"
      :opacity="elemento.transparencia"
      :options="{
        identificador: elemento.id,
        style: elemento.estilo,
        onEachFeature: (feature, layer) =>
          onEachFeature(elemento.estilo, feature, layer),
        pointToLayer: (feature, latlng) =>
          puntoACirculo(elemento.id, feature, latlng, elemento.estilo),
      }"
      :visible="true"
      :z-index="2"
    />
  </LLayerGroup>
</template>

<script>
import L from 'leaflet';
import { mapState, mapActions } from 'vuex';
import { LGeoJson, LLayerGroup } from 'vue2-leaflet';
import {
  ESTILO_HOVER_CAPA_GEOJSON,
  ORIGEN_CAPA_GEOJSON,
  TIPO_GEOMETRIA,
  ATRIBUCION_GENERAL,
} from '../../../compartido/constantes';

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
      atribucionGeneral: ATRIBUCION_GENERAL,
    };
  },
  computed: {
    ...mapState('visor', ['capasOperativas']),
    elementosActivos() {
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
      capa.setStyle(ESTILO_HOVER_CAPA_GEOJSON);
    },
    reestablecerPoligono(e, estilosPorDefecto) {
      const capa = e.target;
      capa.setStyle(estilosPorDefecto);
    },
    async seleccionarPoligono(e, feature) {
      const capa = e.target;
      const identificador = capa?.options?.identificador;
      const capaGeojson = this.elementosActivos.find(
        (capa) => capa.id === identificador
      );
      if (capaGeojson) {
        let propiedades = {};
        if (capaGeojson.origen === ORIGEN_CAPA_GEOJSON.POSTGRESQL) {
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
        const tipoGeometriaOrigen =
          capaGeojson.geojson.features[0].geometry.type;
        if (tipoGeometriaOrigen === TIPO_GEOMETRIA.PUNTO) {
          const latlng = capa.getLatLng();
          this.establecerBounds([latlng, latlng]);
        } else {
          const cuadroDelimitador = capa.getBounds();
          this.establecerBounds(cuadroDelimitador);
        }
        this.abrirVentana('InformacionCapaWfs');
      }
    },
    puntoACirculo(capaId, feature, latlng, estilosPorDefecto) {
      if (feature.geometry.type === TIPO_GEOMETRIA.PUNTO) {
        return L.circleMarker(latlng, {
          radius: 5,
          fillColor: estilosPorDefecto.fillColor,
          color: estilosPorDefecto.color,
          weight: estilosPorDefecto.weight,
          opacity: estilosPorDefecto.opacity,
          fillOpacity: estilosPorDefecto.fillOpacity,
          identificador: capaId,
        });
      }
    },
  },
};
</script>
PUNTOPUNTO
