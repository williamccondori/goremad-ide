<template>
    <a-drawer
        :visible="estaAbiertoCapaResumenVentana"
        :width="esMovil ? '100%' : 400"
        @close="cerrarCapaResumenVentana()"
    >
        <span slot="title" style="text-transform: uppercase">
            <b>Información de las capas activas</b>
        </span>
        <a-form-model ref="referenciaFormulario" :model="formulario">
            <a-form-model-item label="Capa activa">
                <a-select
                    v-model="formulario.elementoActivoId"
                    :allow-clear="true"
                    placeholder="Seleccione"
                    @change="cambiarElementoActivoId"
                >
                    <a-select-option
                        v-for="elemento in elementosActivos"
                        :key="elemento.id"
                        :value="elemento.id"
                    >
                        {{ elemento.titulo }}
                    </a-select-option>
                </a-select>
            </a-form-model-item>
        </a-form-model>
        <div v-if="elementoActivo" class="app--contenedor-vertical-pequenio">
            <a-descriptions
                bordered
                :column="1"
                size="small"
                :title="elementoActivo.titulo"
            >
                <a-descriptions-item label="Servicio:">
                    {{ elementoActivo.servicioTitulo }}
                </a-descriptions-item>
                <a-descriptions-item label="Autor:">
                    {{ elementoActivo.atribucion }}
                </a-descriptions-item>
                <a-descriptions-item label="Título:">
                    {{ elementoActivo.titulo }}
                </a-descriptions-item>
                <a-descriptions-item label="Nombre:">
                    <ATag size="small"> {{ elementoActivo.nombre }}</ATag>
                </a-descriptions-item>
                <a-descriptions-item label="Leyenda:">
                    <img alt="Leyenda" :src="elementoActivo.urlLeyenda" />
                </a-descriptions-item>
            </a-descriptions>
            <a-card size="small">
                <span>Transparencia:</span>
                <a-slider
                    v-model="transparencia"
                    :max="1"
                    :min="0"
                    :step="0.1"
                />
            </a-card>
            <a-card size="small">
                <a-button
                    block
                    icon="upload"
                    @click="traerAlFrente(elementoActivo.id)"
                >
                    Traer al frente
                </a-button>
                <a-divider />
                <a-button
                    block
                    icon="search"
                    @click="verAreaCobertura(elementoActivo.cuadroDelimitador)"
                >
                    Zoom a la capa
                </a-button>
                <a-divider />
                <a-button
                    block
                    icon="delete"
                    type="danger"
                    @click="eliminarCapaActivaYCerrar(elementoActivo.id)"
                >
                    Remover capa del mapa
                </a-button>
            </a-card>
        </div>
    </a-drawer>
</template>

<script>
import { mapActions, mapState } from 'vuex';

const formulario = {
    elementoActivoId: undefined,
};

export default {
    data() {
        return {
            formulario: { ...formulario },
            elementoActivo: undefined,
        };
    },
    computed: {
        ...mapState(['esMovil']),
        ...mapState('visor', [
            'estaAbiertoCapaResumenVentana',
            'capasActivas',
            'capas',
        ]),
        elementosActivos() {
            return this.capas.filter((capa) => {
                return this.capasActivas.includes(capa.id);
            });
        },
        transparencia: {
            get() {
                return this.elementoActivo.transparencia ?? 1;
            },
            set(transparencia) {
                this.establecerCapaTransparencia({
                    id: this.elementoActivo.id,
                    transparencia,
                });
            },
        },
    },
    watch: {
        estaAbiertoCapaResumenVentana(valor) {
            if (valor) {
                this.formulario = { ...formulario };
                this.elementoActivo = undefined;
            }
        },
    },
    methods: {
        ...mapActions('visor', [
            'cerrarCapaResumenVentana',
            'establecerCapaTransparencia',
            'establecerCapaSuperior',
            'establecerBounds',
            'eliminarCapaActiva',
        ]),
        cambiarElementoActivoId(capaActivaId) {
            this.elementoActivo = this.elementosActivos.find(
                (elemento) => elemento.id === capaActivaId
            );
        },
        traerAlFrente(capaId) {
            this.establecerCapaSuperior(capaId);
        },
        verAreaCobertura(cuadroDelimitador) {
            const bounds = [
                [cuadroDelimitador[1], cuadroDelimitador[0]],
                [cuadroDelimitador[3], cuadroDelimitador[2]],
            ];
            this.establecerBounds(bounds);
        },
        eliminarCapaActivaYCerrar(id) {
            this.eliminarCapaActiva(id);
            this.establecerCapaTransparencia({ id, transparencia: 1 });
            this.cerrarCapaResumenVentana();
        },
    },
};
</script>
