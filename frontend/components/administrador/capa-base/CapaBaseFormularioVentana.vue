<template>
    <ADrawer
        :mask-closable="false"
        :visible="estaAbiertoCapaBaseFormularioVentana"
        :width="esMovil ? '100%' : 400"
        @close="cerrarCapaBaseFormularioVentana()"
    >
        <span slot="title" style="text-transform: uppercase">
            <b>{{ titulo }}</b>
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
                        message: 'Ingrese el nombre de la capa base',
                    },
                ]"
            >
                <AInput
                    v-model="formulario.nombre"
                    placeholder="Ingrese el nombre de la capa base"
                />
            </AFormModelItem>
            <AFormModelItem
                label="URL:"
                prop="url"
                :rules="[
                    {
                        required: true,
                        message: 'Ingrese la URL de la capa base',
                    },
                ]"
            >
                <AInput
                    v-model="formulario.url"
                    placeholder="Ingrese la URL de la capa base"
                />
            </AFormModelItem>
            <AFormModelItem
                label="Atribución:"
                prop="atribucion"
                :rules="[
                    {
                        required: true,
                        message: 'Ingrese la atribución de la capa base',
                    },
                ]"
            >
                <AInput
                    v-model="formulario.atribucion"
                    placeholder="Ingrese la atribución de la capa base"
                />
            </AFormModelItem>
            <AFormModelItem label="¿Está habilitado?:" prop="estaHabilitado">
                <ACheckbox v-model="formulario.estaHabilitado" />
            </AFormModelItem>
            <div>
                <AButton block html-type="submit" icon="save" type="primary">
                    {{ titulo }}
                </AButton>
            </div>
        </AFormModel>
    </ADrawer>
</template>

<script>
import { Drawer, FormModel, Input, Checkbox, Button } from 'ant-design-vue';
import { mapState, mapActions } from 'vuex';

const formulario = {
    nombre: '',
    url: '',
    atribucion: '',
    estaHabilitado: true,
};

export default {
    components: {
        ADrawer: Drawer,
        AFormModel: FormModel,
        AFormModelItem: FormModel.Item,
        AInput: Input,
        ACheckbox: Checkbox,
        AButton: Button,
    },
    data() {
        return {
            formulario: { ...formulario },
        };
    },
    computed: {
        ...mapState(['esMovil']),
        ...mapState('administrador', [
            'estaAbiertoCapaBaseFormularioVentana',
            'capaBase',
        ]),
        esEdicion() {
            return this.capaBase !== undefined;
        },
        titulo() {
            return this.esEdicion ? 'Actualizar capa base' : 'Crear capa base';
        },
    },
    watch: {
        estaAbiertoCapaBaseFormularioVentana(value) {
            if (!value) {
                this.formulario = { ...formulario };
                this.$refs.referenciaFormulario?.resetFields();
            } else {
                if (this.esEdicion && this.capaBase) {
                    this.formulario.nombre = this.capaBase.nombre;
                    this.formulario.url = this.capaBase.url;
                    this.formulario.atribucion = this.capaBase.atribucion;
                    this.formulario.estaHabilitado =
                        this.capaBase.estaHabilitado;
                }
            }
        },
    },
    methods: {
        ...mapActions('administrador', [
            'cerrarCapaBaseFormularioVentana',
            'obtenerCapasBase',
        ]),
        guardar() {
            this.$refs.referenciaFormulario?.validate(async (valid) => {
                if (valid) {
                    try {
                        this.$iniciarCarga();
                        if (this.esEdicion) {
                            await this.$axios.put(
                                `/capas-base/${this.capaBase.id}/`,
                                {
                                    ...this.formulario,
                                }
                            );
                        } else {
                            await this.$axios.post('/capas-base/', {
                                ...this.formulario,
                            });
                        }
                        await this.obtenerCapasBase();
                        this.cerrarCapaBaseFormularioVentana();
                        this.$mostrarMensajeCorrecto();
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
