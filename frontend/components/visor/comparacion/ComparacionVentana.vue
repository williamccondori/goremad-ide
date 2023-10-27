<template>
    <a-drawer
        :visible="estaAbiertoComparacionVentana"
        :width="esMovil ? '100%' : 400"
        @close="cerrarComparacionVentana()"
    >
        <span slot="title" style="text-transform: uppercase">
            <b>Comparar capas activas</b>
        </span>
        <a-form-model
            ref="referenciaFormulario"
            :model="formulario"
            @submit.prevent="comparar()"
        >
            <a-form-model-item
                label="Capa de la izquierda"
                prop="capaIzquierda"
                :rules="[
                    {
                        required: true,
                        message: 'Seleccione la capa de la izquierda',
                    },
                ]"
            >
                <a-select
                    v-model="formulario.capaIzquierda"
                    placeholder="Seleccione  la capa de la izquierda"
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
            <a-form-model-item
                label="Capa de la derecha"
                prop="capaDerecha"
                :rules="[
                    {
                        required: true,
                        message: 'Seleccione la capa de la derecha',
                    },
                ]"
            >
                <a-select
                    v-model="formulario.capaDerecha"
                    placeholder="Seleccione  la capa de la derecha"
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
            <div>
                <a-button block html-type="submit" icon="check" type="primary">
                    Comparar
                </a-button>
            </div>
        </a-form-model>
    </a-drawer>
</template>

<script>
import { mapState, mapActions } from 'vuex';

const formulario = {
    capaIzquierda: undefined,
    capaDerecha: undefined,
};

export default {
    data() {
        return {
            formulario: { ...formulario },
        };
    },
    computed: {
        ...mapState(['esMovil']),
        ...mapState('visor', [
            'estaAbiertoComparacionVentana',
            'capas',
            'capasActivas',
        ]),
        elementosActivos() {
            return this.capas.filter((capa) =>
                this.capasActivas.includes(capa.id)
            );
        },
    },
    watch: {
        estaAbiertoComparacionVentana(valor) {
            if (!valor) {
                this.formulario = { ...formulario };
                this.$refs.referenciaFormulario?.resetFields();
            }
        },
    },
    methods: {
        ...mapActions('visor', ['cerrarComparacionVentana']),
        comparar() {
            this.$refs.referenciaFormulario?.validate((valid) => {
                if (valid) {
                    try {
                        this.$iniciarCarga();
                        if (
                            this.formulario.capaIzquierda ===
                            this.formulario.capaDerecha
                        ) {
                            this.$mostrarMensajeAdvertencia(
                                'No puede comparar la misma capa en ambas posiciones'
                            );
                            return;
                        }
                    } catch (error) {
                        this.$manejarError(error);
                    } finally {
                        this.$finalizarCarga();
                    }
                }
            });
        },
    },
};
</script>
