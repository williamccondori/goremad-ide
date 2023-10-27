<template>
    <ADrawer
        placement="left"
        :visible="estaAbiertoMarcadorFormularioVentana"
        :width="esMovil ? '100%' : 400"
        @close="cerrarMarcadorFormularioVentana()"
    >
        <span slot="title" style="text-transform: uppercase">
            <b>Agregar marcador</b>
        </span>
        <AFormModel
            ref="referenciaFormulario"
            :model="formulario"
            @submit.prevent="guardar()"
        >
            <AFormModelItem
                label="Nombre:"
                prop="nombre"
                :rules="[
                    {
                        required: true,
                        message: 'Ingrese el nombre del marcador',
                    },
                ]"
            >
                <AInput
                    v-model="formulario.nombre"
                    placeholder="Ingrese el nombre del marcador"
                />
            </AFormModelItem>
            <AFormModelItem
                label="Zoom:"
                prop="zoom"
                :rules="[
                    {
                        required: true,
                        message: 'Ingrese el zoom del mapa',
                    },
                ]"
            >
                <AInput
                    v-model="formulario.zoom"
                    disabled
                    placeholder="Ingrese el zoom del mapa"
                />
            </AFormModelItem>
            <ARow :gutter="16">
                <ACol :span="12">
                    <AFormModelItem
                        label="Latitud:"
                        prop="latitud"
                        :rules="[
                            {
                                required: true,
                                message: 'Ingrese la latitud del mapa',
                            },
                        ]"
                    >
                        <AInput v-model="formulario.latitud" disabled />
                    </AFormModelItem>
                </ACol>
                <ACol :span="12">
                    <AFormModelItem
                        label="Longitud:"
                        prop="longitud"
                        :rules="[
                            {
                                required: true,
                                message: 'Ingrese la longitud del mapa',
                            },
                        ]"
                    >
                        <AInput v-model="formulario.longitud" disabled />
                    </AFormModelItem>
                </ACol>
            </ARow>
            <AButton block html-type="submit" icon="save" type="primary">
                Guardar
            </AButton>
        </AFormModel>
    </ADrawer>
</template>

<script>
import { Drawer, FormModel, Input, Button, Row, Col } from 'ant-design-vue';
import { mapState, mapActions } from 'vuex';

const formulario = {
    nombre: '',
    zoom: 0,
    latitud: 0,
    longitud: 0,
};

export default {
    components: {
        ADrawer: Drawer,
        AFormModel: FormModel,
        AFormModelItem: FormModel.Item,
        AInput: Input,
        AButton: Button,
        ARow: Row,
        ACol: Col,
    },
    data() {
        return {
            formulario: { ...formulario },
        };
    },
    computed: {
        ...mapState(['esMovil']),
        ...mapState('visor', [
            'estaAbiertoMarcadorFormularioVentana',
            'informacionPosicion',
        ]),
    },
    watch: {
        estaAbiertoMarcadorFormularioVentana(valor) {
            if (!valor) {
                this.limpiar();
            } else {
                if (this.informacionPosicion) {
                    this.formulario.zoom = this.informacionPosicion.zoom;
                    this.formulario.latitud = this.informacionPosicion.latitud;
                    this.formulario.longitud =
                        this.informacionPosicion.longitud;
                }
            }
        },
    },
    methods: {
        ...mapActions('visor', [
            'cerrarMarcadorFormularioVentana',
            'agregarMarcador',
        ]),
        guardar() {
            this.$refs.referenciaFormulario?.validate((valid) => {
                if (valid) {
                    this.agregarMarcador({ ...this.formulario });
                    this.$mostrarMensajeCorrecto();
                    this.cerrarMarcadorFormularioVentana();
                }
            });
        },
        limpiar() {
            this.formulario = { ...formulario };
            this.$refs.referenciaFormulario?.resetFields();
        },
    },
};
</script>
