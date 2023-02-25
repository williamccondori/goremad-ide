<template>
  <div>
    <LWMSTileLayer
      v-for="elemento in elementosActivos"
      :key="elemento.id"
      :attribution="elemento.atribucion"
      :base-url="elemento.url"
      :layers="elemento.capa"
      :name="elemento.titulo"
      :transparent="true"
      :visible="true"
      :z-index="1"
      format="image/png"
      layer-type="layer"
    />
    <LMarker v-if="posicionCapa" :lat-lng="posicionCapa">
      <LPopup>
        <a-tabs type="card">
          <a-tab-pane
            v-for="informacionCapa in informacionesCapa"
            :key="informacionCapa.capa"
          >
            <span slot="tab"> <a-icon type="table" /> </span>
            <a-tag color="green">Capa: {{ informacionCapa.capa }}</a-tag>
            <a-divider />
            <a-table
              :columns="columns"
              :data-source="informacionCapa.informacion"
              size="small"
            >
              <template slot="clave" slot-scope="fila">
                <b>{{ fila.clave }}:</b>
              </template>
            </a-table>
          </a-tab-pane>
        </a-tabs>
        <a-button type="primary" @click="abrirInformacionCapaVentana()">
          Consultar
        </a-button>
      </LPopup>
    </LMarker>
  </div>
</template>

<script>
import { mapState } from "vuex";
import { LWMSTileLayer, LPopup, LMarker, findRealParent } from "vue2-leaflet";
export default {
  components: {
    LWMSTileLayer,
    LPopup,
    LMarker,
  },
  data() {
    return {
      posicionCapa: undefined,
      informacionesCapa: [],
      columns: [
        {
          key: "clave",
          title: "Descripción",
          scopedSlots: { customRender: "clave" },
        },
        {
          key: "valor",
          title: "Valor",
          dataIndex: "valor",
        },
      ],
    };
  },
  computed: {
    ...mapState("visor", [
      "capasInteroperables",
      "capasInteroperablesActivas",
      "consultarInformacion",
    ]),
    elementosActivos() {
      return this.capasInteroperables.filter((elemento) =>
        this.capasInteroperablesActivas.includes(elemento.id)
      );
    },
  },
  watch: {
    consultarInformacion(valor) {
      if (!valor) {
        this.posicionCapa = undefined;
        this.informacionesCapa = [];
      }
    },
  },
  mounted() {
    this.$nextTick(this.inicializarMapa);
  },
  methods: {
    async inicializarMapa() {
      this.mapa = findRealParent(this.$parent).mapObject;
      this.mapa.on("click", async (e) => this.obtenerCaracteristicas(e.latlng));
    },
    async obtenerCaracteristicas(latitudLongitud) {
      this.posicionCapa = undefined;
      this.informacionesCapa = [];
      if (this.consultarInformacion) {
        try {
          this.$iniciarCarga();
          // Se generan los parametros de consulta de caracteristicas.
          const parametros = this.$obtenerParametrosConsulta(
            this.mapa,
            latitudLongitud
          );
          // Se realiza la consulta de caracteristicas para cada capa interoperable activa.
          const informaciones = [];
          for (let i = 0; i < this.capasInteroperablesActivas.length; i++) {
            const capaInteroperableActivaId =
              this.capasInteroperablesActivas[i];
            // Se busca el identificador en la lista de capas interoperables activas.
            const capaInteroperableActiva = this.capasInteroperables.find(
              (x) => x.id === capaInteroperableActivaId
            );
            if (capaInteroperableActiva) {
              // Se agrega la informacion de la capa (url y nombre de sub capas activas).
              parametros.url = capaInteroperableActiva.url;
              parametros.layers = capaInteroperableActiva.capa;
              // Se realiza la consulta de caracteristicas.
              const { data } = await this.$axios.get(
                "/visor/servicios-externos/features/",
                {
                  params: parametros,
                }
              );
              if (data.length > 0) {
                informaciones.push({
                  capa: capaInteroperableActiva.titulo,
                  informacion: data,
                });
              }
            }
          }
          if (informaciones.length > 0) {
            this.posicionCapa = latitudLongitud;
            this.informacionesCapa = informaciones;
          }
        } catch (error) {
          this.$manejarError(error);
        } finally {
          this.$finalizarCarga();
        }
      }
    },
    abrirInformacionCapaVentana() {
      alert("abrirInformacionCapaVentana");
    },
  },
};
</script>
