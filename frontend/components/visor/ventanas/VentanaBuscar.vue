<template>
    <a-drawer
        :visible="estaAbiertoVentanaBuscar"
        :width="tamanioVentana"
        @close="cerrarVentana('Buscar')"
    >
        <span slot="title">
            <b>Buscar</b>
        </span>
        <a-space direction="vertical" style="width: 100%">
            <a-tabs default-active-key="buscarPorCriterio" type="card">
                <a-tab-pane key="buscarPorCriterio" tab="Buscar por criterio">
                    <a-space direction="vertical" style="width: 100%">
                        <a-form-model
                            ref="form1"
                            :model="form1"
                            @submit.prevent="buscarPorCriterio()"
                        >
                            <a-form-model-item
                                label="Término de búsqueda"
                                prop="query"
                                :rules="[
                                    {
                                        required: true,
                                        message:
                                            'Ingrese el término de búsqueda',
                                    },
                                ]"
                            >
                                <a-input
                                    v-model="form1.query"
                                    placeholder="Ingrese el término de búsqueda"
                                />
                            </a-form-model-item>
                            <a-button
                                block
                                html-type="submit"
                                icon="search"
                                type="primary"
                            >
                                Buscar
                            </a-button>
                        </a-form-model>
                        <a-divider />
                        <div>
                            <span>Todos los elementos:</span>
                            <ATag color="green" style="margin: 0">
                                {{ resultados.length }}
                            </ATag>
                        </div>
                        <a-button
                            v-for="resultado in resultados"
                            :key="resultado.id"
                            block
                            type="dashed"
                            @click="verResultadoPorCriterio(resultado)"
                        >
                            {{ resultado.nombre }}
                        </a-button>
                        <a-button
                            block
                            :disabled="resultados.length === 0"
                            icon="delete"
                            type="danger"
                            @click="limpiarResultadoPorCriterio()"
                        >
                            Limpiar
                        </a-button>
                    </a-space>
                </a-tab-pane>
                <a-tab-pane
                    key="buscarPorCoordenadas"
                    tab="Buscar por coordenadas"
                >
                    <a-space direction="vertical" style="width: 100%">
                        <a-form-model
                            ref="form2"
                            :model="form2"
                            @submit.prevent="buscarPorCoordenada()"
                        >
                            <a-form-model-item
                                label="Sistema de coordenadas"
                                prop="proyeccion"
                                :rules="[
                                    {
                                        required: true,
                                        message:
                                            'Seleccione el sistema de coordenadas',
                                    },
                                ]"
                            >
                                <a-select
                                    v-model="form2.proyeccion"
                                    @change="cambiarProyeccion()"
                                >
                                    <a-select-option value="latlong"
                                        >GEOGRÁFICA</a-select-option
                                    >
                                    <a-select-option value="utm"
                                        >UTM</a-select-option
                                    >
                                </a-select>
                            </a-form-model-item>
                            <a-form-model-item
                                label="Datum"
                                prop="datum"
                                :rules="[
                                    {
                                        required: form2.proyeccion === 'utm',
                                        message: 'Seleccione el Datum',
                                    },
                                ]"
                            >
                                <a-select
                                    v-model="form2.datum"
                                    :disabled="form2.proyeccion !== 'utm'"
                                >
                                    <a-select-option
                                        v-for="datum in datums"
                                        :key="datum.codigo"
                                        :value="datum.codigo"
                                    >
                                        {{ datum.etiqueta }}
                                    </a-select-option>
                                </a-select>
                            </a-form-model-item>
                            <a-form-model-item
                                label="Zona UTM"
                                prop="zona"
                                :rules="[
                                    {
                                        required: form2.proyeccion === 'utm',
                                        message: 'Seleccione la zona UTM',
                                    },
                                ]"
                            >
                                <a-select
                                    v-model="form2.zona"
                                    :disabled="form2.proyeccion !== 'utm'"
                                >
                                    <a-select-option value="17"
                                        >17</a-select-option
                                    >
                                    <a-select-option value="18"
                                        >18</a-select-option
                                    >
                                    <a-select-option value="19"
                                        >19</a-select-option
                                    >
                                </a-select>
                            </a-form-model-item>
                            <a-form-model-item
                                :label="
                                    form2.proyeccion === 'utm' ? 'Y' : 'Latitud'
                                "
                                prop="y"
                                :rules="[
                                    {
                                        required: true,
                                        message: `Ingrese el valor para: ${
                                            form2.proyeccion === 'utm'
                                                ? 'Y'
                                                : 'Latitud'
                                        }`,
                                    },
                                ]"
                            >
                                <a-input
                                    v-model="form2.y"
                                    placeholder="Ingrese el término de búsqueda"
                                />
                            </a-form-model-item>
                            <a-form-model-item
                                :label="
                                    form2.proyeccion === 'utm'
                                        ? 'X'
                                        : 'Longitud'
                                "
                                prop="x"
                                :rules="[
                                    {
                                        required: true,
                                        message: `Ingrese el valor para: ${
                                            form2.proyeccion === 'utm'
                                                ? 'X'
                                                : 'Longitud'
                                        }`,
                                    },
                                ]"
                            >
                                <a-input
                                    v-model="form2.x"
                                    placeholder="Ingrese el término de búsqueda"
                                />
                            </a-form-model-item>
                            <a-button
                                block
                                html-type="submit"
                                icon="search"
                                type="primary"
                            >
                                Buscar
                            </a-button>
                        </a-form-model>
                        <a-button
                            block
                            icon="delete"
                            type="danger"
                            @click="limpiarResultadoPorCoordenada()"
                        >
                            Limpiar
                        </a-button>
                    </a-space>
                </a-tab-pane>
            </a-tabs>
        </a-space>
    </a-drawer>
</template>

<script>
import { mapState, mapActions } from 'vuex';
export default {
    data() {
        return {
            form1: {
                query: '',
            },
            resultados: [],
            datumsLatLong: [{ codigo: 'WGS84', etiqueta: 'WGS84' }],
            datumsUtm: [{ codigo: 'PSAD56', etiqueta: 'PSAD56' }],
            form2: {
                proyeccion: 'latlong',
                datum: 'WGS84',
                zona: 17,
                x: 0,
                y: 0,
            },
            datums: this.datumsLatLong,
        };
    },
    computed: {
        ...mapState(['tamanioVentana']),
        ...mapState('visor', ['estaAbiertoVentanaBuscar']),
    },
    methods: {
        ...mapActions('visor', [
            'cerrarVentana',
            'establecerCentro',
            'establecerZoom',
        ]),
        async validarFormulario(formulario) {
            try {
                await formulario.validate();
                return true;
            } catch (error) {
                this.$message.error('Los campos ingresados son inválidos');
                return false;
            }
        },
        async buscarPorCriterio() {
            const formularioValido = await this.validarFormulario(
                this.$refs.form1
            );
            if (!formularioValido) return;
            try {
                this.$iniciarCarga();
                const { data } = await this.$axios.get('/visor/ubicaciones/', {
                    params: {
                        query: this.form1.query,
                    },
                });
                this.resultados = data;
            } catch (error) {
                this.$manejarError(error);
            } finally {
                this.$finalizarCarga();
            }
        },
        async buscarPorCoordenada() {
            const formularioValido = await this.validarFormulario(
                this.$refs.form2
            );
            if (!formularioValido) return;
            try {
                this.$iniciarCarga();
                const { data } = await this.$axios.get('/visor/coordenadas/', {
                    params: this.form2,
                });
                this.establecerCentro([data.latitud, data.longitud]);
                this.establecerZoom(15);
            } catch (error) {
                this.$manejarError(error);
            } finally {
                this.$finalizarCarga();
            }
        },
        verResultadoPorCriterio(resultado) {
            this.establecerCentro(resultado.centro);
            this.establecerZoom(resultado.zoom);
        },
        limpiarResultadoPorCriterio() {
            this.form1 = {
                query: '',
            };
            this.$refs.form1.resetFields();
            this.resultados = [];
        },
        limpiarResultadoPorCoordenada() {
            this.form2 = {
                proyeccion: 'latlong',
                datum: 'WGS84',
                zona: 17,
                x: 0,
                y: 0,
            };
            this.$refs.form2.resetFields();
        },
        cambiarProyeccion() {
            const { proyeccion } = this.form2;
            if (proyeccion === 'utm') {
                this.datums = this.datumsUtm;
                this.form2.datum = 'PSAD56';
            } else {
                this.datums = this.datumsLatLong;
                this.form2.datum = 'WGS84';
            }
        },
    },
};
</script>
