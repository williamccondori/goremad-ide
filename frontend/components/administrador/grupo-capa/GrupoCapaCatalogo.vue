<template>
    <div>
        <ATree
            :default-expand-all="true"
            :replace-fields="{
                key: 'id',
                title: 'label',
            }"
            :selectable="false"
            :tree-data="estructuraGruposCapas"
        >
            <template #title="{ id, label }">
                <ADropdown :trigger="['contextmenu']">
                    <span>{{ label }}</span>
                    <template #overlay>
                        <AMenu
                            @click="
                                ({ key: menuId }) => seleccionar(id, menuId)
                            "
                        >
                            <AMenuItem key="crear">Crear</AMenuItem>
                            <AMenuItem v-if="id !== 'root'" key="actualizar">
                                Actualizar
                            </AMenuItem>
                            <AMenuItem v-if="id !== 'root'" key="eliminar">
                                Eliminar
                            </AMenuItem>
                        </AMenu>
                    </template>
                </ADropdown>
            </template>
        </ATree>
        <ADrawer
            :mask-closable="false"
            :visible="estaAbiertoGrupoCapaFormularioVentana"
            :width="esMovil ? '100%' : 400"
            @close="cerrarServicioExternoFormularioVentana()"
        >
            <span slot="title" style="text-transform: uppercase">
                <b>{{ titulo }}</b>
            </span>
            <AFormModel
                ref="referenciaFormulario"
                :model="formulario"
                @submit.prevent="guardar()"
            >
                <AFormModelItem label="Grupo de capas:" prop="grupoCapaId">
                    <ASelect
                        v-model="formulario.grupoCapaId"
                        :allow-clear="true"
                        :disabled="!esEdicion"
                        placeholder="Todos los elementos"
                    >
                        <ASelectOption
                            v-for="elemento in gruposCapas"
                            :key="elemento.id"
                            :value="elemento.id"
                        >
                            {{ elemento.nombre }}
                        </ASelectOption>
                    </ASelect>
                </AFormModelItem>
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
                    label="¿Está habilitado?:"
                    prop="estaHabilitado"
                >
                    <ACheckbox v-model="formulario.estaHabilitado" />
                </AFormModelItem>
                <div>
                    <AButton
                        block
                        html-type="submit"
                        icon="save"
                        type="primary"
                    >
                        {{ titulo }}
                    </AButton>
                </div>
            </AFormModel>
        </ADrawer>
    </div>
</template>

<script>
import {
    Drawer,
    Tree,
    Dropdown,
    Menu,
    Select,
    FormModel,
    Input,
    Checkbox,
    Button,
} from 'ant-design-vue';
import { mapState, mapActions } from 'vuex';

const formulario = {
    nombre: '',
    grupoCapaId: undefined,
    estaHabilitado: true,
};

export default {
    components: {
        ADrawer: Drawer,
        ATree: Tree,
        ADropdown: Dropdown,
        AMenu: Menu,
        AMenuItem: Menu.Item,
        ASelect: Select,
        ASelectOption: Select.Option,
        AFormModel: FormModel,
        AFormModelItem: FormModel.Item,
        AInput: Input,
        ACheckbox: Checkbox,
        AButton: Button,
    },
    data() {
        return {
            formulario: { ...formulario },
            esEdicion: false,
            grupoCapaId: undefined,
            estaAbiertoGrupoCapaFormularioVentana: false,
        };
    },
    async fetch() {
        try {
            this.$iniciarCarga();
            await this.obtenerGruposCapasEstructura();
            await this.obtenerGruposCapas();
        } catch (error) {
            this.$manejarError(error);
        } finally {
            this.$finalizarCarga();
        }
    },
    computed: {
        ...mapState(['esMovil']),
        ...mapState('administrador', ['gruposCapas', 'estructuraGruposCapas']),
        titulo() {
            return this.esEdicion
                ? 'Actualizar servicio externo'
                : 'Crear grupo de capas';
        },
    },
    methods: {
        ...mapActions('administrador', [
            'obtenerGruposCapas',
            'obtenerGruposCapasEstructura',
        ]),
        async seleccionar(grupoCapaId, menuId) {
            switch (menuId) {
                case 'crear':
                    this.crear(grupoCapaId);
                    break;
                case 'actualizar':
                    await this.actualizar(grupoCapaId);
                    break;
                case 'eliminar':
                    await this.eliminar(grupoCapaId);
                    break;
                default:
                    break;
            }
        },
        crear(grupoCapaId) {
            this.formulario.grupoCapaId =
                grupoCapaId === 'root' ? undefined : grupoCapaId;
            this.esEdicion = false;
            this.grupoCapaId = undefined;
            this.estaAbiertoGrupoCapaFormularioVentana = true;
        },
        async actualizar(grupoCapaId) {
            try {
                this.$iniciarCarga();
                const { data } = await this.$axios.get(
                    `/grupos-capas/${grupoCapaId}/`
                );
                this.formulario = { ...data };
                if (data.grupoCapaId === null) {
                    this.formulario.grupoCapaId = undefined;
                }
                this.esEdicion = true;
                this.grupoCapaId = grupoCapaId;
                this.estaAbiertoGrupoCapaFormularioVentana = true;
            } catch (error) {
                this.$manejarError(error);
            } finally {
                this.$finalizarCarga();
            }
        },
        async eliminar(grupoCapaId) {
            try {
                this.$iniciarCarga();
                await this.$axios.delete(`/grupos-capas/${grupoCapaId}/`);
                await this.obtenerGruposCapasEstructura();
                await this.obtenerGruposCapas();
                this.$mostrarMensajeCorrecto();
            } catch (error) {
                this.$manejarError(error);
            } finally {
                this.$finalizarCarga();
            }
        },
        guardar() {
            this.$refs.referenciaFormulario?.validate(async (valid) => {
                if (valid) {
                    try {
                        this.$iniciarCarga();
                        this.formulario.grupoCapaId =
                            this.formulario.grupoCapaId === 'root'
                                ? undefined
                                : this.formulario.grupoCapaId;

                        if (this.esEdicion) {
                            await this.$axios.put(
                                `/grupos-capas/${this.grupoCapaId}/`,
                                {
                                    ...this.formulario,
                                }
                            );
                        } else {
                            await this.$axios.post('/grupos-capas/', {
                                ...this.formulario,
                            });
                        }
                        await this.obtenerGruposCapasEstructura();
                        await this.obtenerGruposCapas();
                        this.cerrarServicioExternoFormularioVentana();
                        this.$mostrarMensajeCorrecto();
                    } catch (error) {
                        this.$manejarError(error);
                    } finally {
                        this.$finalizarCarga();
                    }
                }
            });
        },
        cerrarServicioExternoFormularioVentana() {
            this.formulario = { ...formulario };
            this.$refs.referenciaFormulario?.resetFields();
            this.estaAbiertoGrupoCapaFormularioVentana = false;
        },
    },
};
</script>
