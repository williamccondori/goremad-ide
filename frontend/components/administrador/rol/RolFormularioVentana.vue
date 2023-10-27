<template>
    <ADrawer
        :mask-closable="false"
        :visible="estaAbiertoRolFormularioVentana"
        :width="esMovil ? '100%' : 400"
        @close="cerrarRolFormularioVentana"
    >
        <span slot="title">
            <b>Actualizar roles</b>
        </span>
        <AFormModel
            ref="referenciaFormulario"
            :model="formulario"
            @submit.prevent="guardar()"
        >
            <AFormModelItem label="Usuario:" prop="esUsuario">
                <ACheckbox v-model="formulario.esUsuario" disabled />
            </AFormModelItem>
            <AFormModelItem label="Administrador:" prop="esAdministrador">
                <ACheckbox v-model="formulario.esAdministrador" />
            </AFormModelItem>
            <div>
                <AButton block html-type="submit" icon="save" type="primary">
                    Actualizar roles
                </AButton>
            </div>
        </AFormModel>
    </ADrawer>
</template>

<script>
import { Drawer, FormModel, Checkbox, Button } from 'ant-design-vue';
import { mapState, mapActions } from 'vuex';

const formulario = {
    esUsuario: false,
    esAdministrador: false,
};

export default {
    components: {
        ADrawer: Drawer,
        AFormModel: FormModel,
        AFormModelItem: FormModel.Item,
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
            'estaAbiertoRolFormularioVentana',
            'usuario',
        ]),
    },
    watch: {
        estaAbiertoRolFormularioVentana(value) {
            if (!value) {
                this.formulario = { ...formulario };
                this.$refs.referenciaFormulario?.resetFields();
            } else {
                const roles = this.usuario?.roles;
                if (roles) {
                    this.formulario.esUsuario = roles.includes('usuario');
                    this.formulario.esAdministrador =
                        roles.includes('administrador');
                }
            }
        },
    },
    methods: {
        ...mapActions('administrador', [
            'cerrarRolFormularioVentana',
            'obtenerUsuarios',
        ]),
        guardar() {
            this.$refs.referenciaFormulario?.validate(async (valid) => {
                if (valid) {
                    try {
                        this.$iniciarCarga();
                        await this.$axios.put(
                            `/usuarios/${this.usuario.id}/roles/`,
                            {
                                ...this.formulario,
                            }
                        );
                        await this.obtenerUsuarios();
                        this.cerrarRolFormularioVentana();
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
