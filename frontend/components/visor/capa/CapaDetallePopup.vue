<template>
  <LMarker v-if="posicion" :lat-lng="posicion">
    <LPopup>
      <ATabs type="card">
        <ATabPane
          v-for="caracteristica in caracteristicas"
          :key="caracteristica.id"
        >
          <span slot="tab">
            <i class="bx bx-table" />
          </span>
          <div class="app--contenedor-vertical-pequenio">
            <div>
              <ATag color="green">
                Servicio: <b>{{ caracteristica.titulo }} </b>
              </ATag>
            </div>
            <ATable
              bordered
              :columns="columnas"
              :data-source="caracteristica.propiedades"
              :pagination="false"
              row-key="clave"
              size="small"
            />
          </div>
        </ATabPane>
      </ATabs>
    </LPopup>
  </LMarker>
</template>

<script>
import { Tabs, Tag, Table } from 'ant-design-vue';
import { mapState } from 'vuex';
import { v4 as uuidv4 } from 'uuid';
import { LMarker, LPopup, findRealParent } from 'vue2-leaflet';
export default {
  components: {
    ATabs: Tabs,
    ATabPane: Tabs.TabPane,
    ATag: Tag,
    ATable: Table,
    LMarker,
    LPopup,
  },
  data() {
    return {
      posicion: undefined,
      caracteristicas: [],
      columnas: [
        {
          title: 'Propiedad',
          dataIndex: 'clave',
          key: 'clave',
          width: '50%',
        },
        {
          title: 'Valor',
          dataIndex: 'valor',
          key: 'valor',
          width: '50%',
        },
      ],
    };
  },
  computed: {
    ...mapState('visor', ['capas', 'capasActivas']),
  },
  mounted() {
    this.mapa = findRealParent(this.$parent).mapObject;
    this.mapa.on('click', () => {
      this.posicion = undefined;
      this.caracteristicas = [];
    });
    this.mapa.on('contextmenu', async (e) => {
      this.posicion = undefined;
      this.caracteristicas = [];
      await this.obtenerCaracteristicas(e.latlng);
    });
  },
  methods: {
    obtenerTituloServicio(servicioId) {
      const servicio = this.capas.find(
        (servicio) => servicio.servicioId === servicioId
      );
      return servicio ? servicio.servicioTitulo : '';
    },
    async obtenerCaracteristicas(latitudLongitud) {
      const servicios = {};
      this.capas.forEach((servicio) => {
        servicios[servicio.servicioId] = [
          ...(servicios[servicio.servicioId] || []),
          servicio,
        ];
      });
      const serviciosAConsultar = [];
      Object.keys(servicios).forEach((servicioId) => {
        let capas = servicios[servicioId];
        capas = capas.filter((capa) => this.capasActivas.includes(capa.id));
        if (capas.length === 0) {
          return;
        }
        serviciosAConsultar.push({
          id: servicioId,
          url: capas[0].url,
          capas: capas.map((capa) => capa.nombre),
        });
      });
      try {
        this.$iniciarCarga();
        let serviciosEncontrados = [];
        const parametros = this.$obtenerParametrosConsulta(
          this.mapa,
          latitudLongitud
        );

        const boundingBox = this.mapa.getBounds();
        const southWest = boundingBox.getSouthWest();
        const northEast = boundingBox.getNorthEast();
        const bbox = `${southWest.lng},${southWest.lat},${northEast.lng},${northEast.lat}`;
        const srs = 'EPSG:4326';

        for (const servicio of serviciosAConsultar) {
          for (const capa of servicio.capas) {
            const getFeatureInfoReponse = await fetch(
              servicio.url +
                '&version=1.1.1&request=GetFeatureInfo&layers=' +
                capa +
                '&query_layers=' +
                capa +
                '&styles=&bbox=' +
                bbox +
                '&width=' +
                parametros.width +
                '&height=' +
                parametros.height +
                '&srs=' +
                srs +
                '&info_format=' +
                'text/html' +
                '&x=' +
                parametros.x +
                '&y=' +
                parametros.y
            );
            const data = await getFeatureInfoReponse.json();
            if (data) {
              const tempElement = document.createElement('div');
              tempElement.innerHTML = data;
              // Recorrer todos los elementos descendientes y quitarles los atributos de estilo
              const elementsWithStyles = tempElement.querySelectorAll('*');
              for (var i = 0; i < elementsWithStyles.length; i++) {
                elementsWithStyles[i].removeAttribute('style');
              }
              // Obtener el contenido del elemento temporal sin estilos
              const contentWithoutStyles = tempElement.innerHTML;
              console.log(contentWithoutStyles);
            }
          }
        }
        if (serviciosEncontrados.length > 0) {
          this.posicion = latitudLongitud;
          serviciosEncontrados.forEach((servicioEncontrado) => {
            servicioEncontrado.resultados.forEach((resultado) => {
              this.caracteristicas.push({
                id: uuidv4(),
                titulo: this.obtenerTituloServicio(servicioEncontrado.id),
                propiedades: resultado.informacion,
              });
            });
          });
        }
      } catch (error) {
        this.$manejarError(error);
      } finally {
        this.$finalizarCarga();
      }
    },
  },
};
</script>
