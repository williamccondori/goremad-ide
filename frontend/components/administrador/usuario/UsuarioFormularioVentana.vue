<template>
    <ADrawer
        :mask-closable="false"
        :visible="estaAbiertoUsuarioFormularioVentana"
        :width="esMovil ? '100%' : 400"
        @close="cerrarUsuarioFormularioVentana"
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
                label="Correo electrónico:"
                prop="email"
                :rules="[
                    {
                        required: true,
                        message: 'Ingrese el correo electrónico del usuario',
                    },
                    {
                        type: 'email',
                        message: 'Ingrese un correo electrónico válido',
                    },
                ]"
            >
                <AInput
                    v-model="formulario.email"
                    :disabled="esEdicion"
                    placeholder="Ingrese el correo electrónico del usuario"
                />
            </AFormModelItem>
            <AFormModelItem
                label="Usuario:"
                prop="username"
                :rules="
                    !esEdicion
                        ? [
                              {
                                  required: true,
                                  message: 'Ingrese el usuario',
                              },
                              {
                                  pattern: /^[a-zA-Z0-9]+$/,
                                  message: 'Ingrese un usuario válido',
                              },
                          ]
                        : []
                "
            >
                <AInput
                    v-model="formulario.username"
                    :disabled="esEdicion"
                    placeholder="Ingrese el usuario"
                />
            </AFormModelItem>
            <AFormModelItem
                label="Contraseña:"
                prop="password"
                :rules="
                    !esEdicion
                        ? [
                              {
                                  required: true,
                                  message: 'Ingrese la contraseña del usuario',
                              },
                          ]
                        : []
                "
            >
                <AInputPassword
                    v-model="formulario.password"
                    :disabled="esEdicion"
                    placeholder="Ingrese la contraseña del usuario"
                />
            </AFormModelItem>
            <AFormModelItem label="Nombres:" prop="nombres">
                <AInput
                    v-model="formulario.nombres"
                    placeholder="Ingrese los nombres del usuario"
                />
            </AFormModelItem>
            <AFormModelItem label="Apellidos:" prop="apellidos">
                <AInput
                    v-model="formulario.apellidos"
                    placeholder="Ingrese los apellidos del usuario"
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
import { Drawer, FormModel, Input, Button, Checkbox } from 'ant-design-vue';
import { mapState, mapActions } from 'vuex';

const formulario = {
    email: '',
    username: '',
    password: '',
    nombres: undefined,
    apellidos: undefined,
    estaHabilitado: true,
};

export default {
    components: {
        ADrawer: Drawer,
        AFormModel: FormModel,
        AFormModelItem: FormModel.Item,
        AInput: Input,
        AInputPassword: Input.Password,
        AButton: Button,
        ACheckbox: Checkbox,
    },
    data() {
        return {
            formulario: { ...formulario },
        };
    },
    computed: {
        ...mapState(['esMovil']),
        ...mapState('administrador', [
            'estaAbiertoUsuarioFormularioVentana',
            'usuario',
        ]),
        esEdicion() {
            return this.usuario !== undefined;
        },
        titulo() {
            return this.esEdicion ? 'Actualizar usuario' : 'Crear usuario';
        },
    },
    watch: {
        estaAbiertoUsuarioFormularioVentana(value) {
            if (!value) {
                this.formulario = { ...formulario };
                this.$refs.referenciaFormulario?.resetFields();
            } else {
                if (this.esEdicion && this.usuario) {
                    this.formulario.email = this.usuario.email;
                    this.formulario.username = this.usuario.username;
                    this.formulario.nombres = this.usuario.nombres;
                    this.formulario.apellidos = this.usuario.apellidos;
                    this.formulario.estaHabilitado =
                        this.usuario.estaHabilitado;
                }
            }
        },
    },
    methods: {
        ...mapActions('administrador', [
            'cerrarUsuarioFormularioVentana',
            'obtenerUsuarios',
        ]),
        guardar() {
            this.$refs.referenciaFormulario?.validate(async (valid) => {
                if (valid) {
                    try {
                        this.$iniciarCarga();
                        if (this.esEdicion) {
                            await this.$axios.put(
                                `/usuarios/${this.usuario.id}/`,
                                {
                                    ...this.formulario,
                                }
                            );
                        } else {
                            await this.$axios.post('/usuarios/', {
                                ...this.formulario,
                            });
                        }
                        await this.obtenerUsuarios();
                        this.cerrarUsuarioFormularioVentana();
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
