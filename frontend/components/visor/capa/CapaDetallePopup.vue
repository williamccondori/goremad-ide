<template>
    <LMarker
        v-if="posicion"
        ref="referenciaMarcador"
        :lat-lng="posicion"
        :icon="marcadorIcono"
        @ready="marcadorListo"
    >
        <LPopup>
            <a-tabs type="card">
                <a-tab-pane
                    v-for="caracteristica in caracteristicas"
                    :key="caracteristica.id"
                >
                    <span slot="tab">
                        <i class="bx bx-table" />
                    </span>
                    <div class="app--contenedor-vertical-pequenio">
                        <div>
                            <a-tag color="green">
                                Servicio: <b>{{ caracteristica.titulo }} </b>
                            </a-tag>
                        </div>
                        <a-table
                            bordered
                            :columns="columnas"
                            :data-source="caracteristica.propiedades"
                            :pagination="false"
                            row-key="clave"
                            size="small"
                        />
                    </div>
                </a-tab-pane>
            </a-tabs>
        </LPopup>
    </LMarker>
</template>

<script>
import L from 'leaflet';
import { mapState } from 'vuex';
import { v4 as uuidv4 } from 'uuid';
import { findRealParent, LMarker, LPopup } from 'vue2-leaflet';

export default {
    components: {
        LMarker,
        LPopup,
    },
    data() {
        return {
            posicion: undefined,
            caracteristicas: [],
            marcadorIcono: L.icon({
                iconUrl: require('@/assets/img/marcador.png'),
                iconSize: [30, 30],
                iconAnchor: [15, 15],
            }),
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
        marcadorListo() {
            const marcardor = this.$refs.referenciaMarcador?.mapObject;
            if (marcardor) {
                marcardor.openPopup();
            }
        },
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
                capas = capas.filter((capa) =>
                    this.capasActivas.includes(capa.id)
                );
                if (capas.length === 0) {
                    return;
                }
                serviciosAConsultar.push({
                    id: servicioId,
                    url: capas[0].urlQuery,
                    capas: capas.map((capa) => capa.nombre).join(','),
                    filtros: capas[0].filtros
                });
            });
            try {
                this.$iniciarCarga();
                let serviciosEncontrados = [];
                const parametros = this.$obtenerParametrosConsulta(
                    this.mapa,
                    latitudLongitud
                );
                for (const servicio of serviciosAConsultar) {
                    parametros.url = servicio.url;
                    parametros.layers = servicio.capas;
                    parametros.filtros = servicio.filtros;
                    const { data } = await this.$axios.get(
                        '/visor/web-map-services/features/',
                        {
                            params: parametros,
                        }
                    );
                    if (data.length > 0) {
                        serviciosEncontrados = [
                            ...serviciosEncontrados,
                            {
                                id: servicio.id,
                                resultados: data,
                            },
                        ];
                    }
                }
                if (serviciosEncontrados.length > 0) {
                    this.posicion = latitudLongitud;
                    serviciosEncontrados.forEach((servicioEncontrado) => {
                        servicioEncontrado.resultados.forEach((resultado) => {
                            this.caracteristicas.push({
                                id: uuidv4(),
                                titulo: this.obtenerTituloServicio(
                                    servicioEncontrado.id
                                ),
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
