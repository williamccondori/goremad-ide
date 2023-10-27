<template>
    <AdministracionPagina titulo="Temas">
        <a-space direction="vertical" style="width: 100%">
            <a-collapse v-model="collapseActivo">
                <a-collapse-panel
                    key="formularioPanel"
                    :header="tituloFormulario"
                >
                    <a-form-model
                        ref="form"
                        :model="form"
                        @submit.prevent="guardar()"
                    >
                        <a-form-model-item
                            label="Código"
                            prop="codigo"
                            :rules="{
                                required: true,
                                message: 'Ingrese el código',
                            }"
                        >
                            <a-input
                                v-model="form.codigo"
                                placeholder="Ingrese el código"
                            />
                        </a-form-model-item>
                        <a-form-model-item
                            label="Nombre"
                            prop="nombre"
                            :rules="{
                                required: true,
                                message: 'Ingrese el nombre',
                            }"
                        >
                            <a-input
                                v-model="form.nombre"
                                placeholder="Ingrese el nombre"
                            />
                        </a-form-model-item>
                        <a-form-model-item
                            label="Descripción"
                            prop="descripcion"
                        >
                            <a-input
                                v-model="form.descripcion"
                                placeholder="Ingrese la descripción"
                                type="textarea"
                            />
                        </a-form-model-item>
                        <a-form-model-item
                            label="Catálogo"
                            prop="catalogoId"
                            :rules="{
                                required: true,
                                message: 'Seleccione el catálogo',
                            }"
                        >
                            <a-select
                                v-model="form.catalogoId"
                                placeholder="Seleccione el catálogo"
                            >
                                <a-select-option
                                    v-for="catalogo in catalogos"
                                    :key="catalogo.id"
                                >
                                    {{ catalogo.nombre }}
                                </a-select-option>
                            </a-select>
                        </a-form-model-item>
                        <a-button html-type="submit" type="primary">
                            <a-icon type="save" /> Guardar
                        </a-button>
                        <a-button type="danger" @click="limpiar()">
                            <a-icon type="redo" />
                            Limpiar
                        </a-button>
                    </a-form-model>
                </a-collapse-panel>
            </a-collapse>
            <a-table
                bordered
                :columns="[
                    {
                        title: 'Código',
                        dataIndex: 'codigo',
                        key: 'codigo',
                        scopedSlots: { customRender: 'codigo' },
                    },
                    {
                        title: 'Catálogo',
                        dataIndex: 'catalogoNombre',
                        key: 'catalogoNombre',
                    },
                    {
                        title: 'Nombre',
                        dataIndex: 'nombre',
                        key: 'nombre',
                    },
                    {
                        title: 'Acciones',
                        key: 'acciones',
                        scopedSlots: { customRender: 'acciones' },
                    },
                ]"
                :data-source="temas"
                row-key="id"
                size="small"
            >
                <div slot="codigo" slot-scope="text">
                    <a-tag color="purple">{{ text }}</a-tag>
                </div>
                <div slot="acciones" slot-scope="text, record">
                    <a-button type="dashed" @click="editar(record)">
                        <a-icon type="edit" />
                    </a-button>
                    <a-button type="dashed" @click="eliminar(record)">
                        <a-icon type="delete" />
                    </a-button>
                </div>
            </a-table>
        </a-space>
    </AdministracionPagina>
</template>

<script>
import AdministracionPagina from '@/components/administrador/compartido/AdministracionPagina.vue';
export default {
    components: {
        AdministracionPagina,
    },
    layout: 'administrador',
    data() {
        return {
            collapseActivo: undefined,
            tituloFormulario: 'Agregar registro',
            form: {
                id: undefined,
                codigo: '',
                nombre: '',
                descripcion: '',
                catalogoId: undefined,
            },
            catalogos: [],
            temas: [],
        };
    },
    async fetch() {
        await this.obtenerCatalogos();
        await this.obtenerTemas();
    },
    methods: {
        async obtenerCatalogos() {
            try {
                this.$iniciarCarga();
                const { data } = await this.$axios.get('/catalogos/');
                this.catalogos = data;
            } catch (error) {
                this.$manejarError(error);
            } finally {
                this.$finalizarCarga();
            }
        },
        async obtenerTemas() {
            try {
                this.$iniciarCarga();
                const { data } = await this.$axios.get('/temas/');
                this.temas = data;
            } catch (error) {
                this.$manejarError(error);
            } finally {
                this.$finalizarCarga();
            }
        },
        async validarFormulario() {
            try {
                await this.$refs.form.validate();
                return true;
            } catch (error) {
                this.$message.error('Los campos ingresados son inválidos');
                return false;
            }
        },
        async guardar() {
            const formularioValido = await this.validarFormulario();
            if (!formularioValido) return;
            try {
                this.$iniciarCarga();
                if (this.form.id) {
                    await this.$axios.put(`/temas/${this.form.id}/`, this.form);
                } else {
                    await this.$axios.post('/temas/', this.form);
                }
                await this.obtenerTemas();
                this.limpiar();
                this.$mostrarMensajeCorrecto();
            } catch (error) {
                this.$manejarError(error);
            } finally {
                this.$finalizarCarga();
            }
        },
        editar(record) {
            this.form = {
                id: record.id,
                codigo: record.codigo,
                nombre: record.nombre,
                descripcion: record.descripcion,
                catalogoId: record.catalogoId,
            };
            this.tituloFormulario = 'Editar registro';
            this.collapseActivo = 'formularioPanel';
        },
        eliminar(record) {
            this.$confirm({
                title: '¿Está seguro de eliminar el tema?',
                content: 'Esta acción no se puede revertir',
                okText: 'Sí',
                okType: 'danger',
                cancelText: 'No',
                onOk: async () => {
                    try {
                        this.$iniciarCarga();
                        await this.$axios.delete(`/temas/${record.id}/`);
                        await this.obtenerTemas();
                        this.$mostrarMensajeCorrecto();
                    } catch (error) {
                        this.$manejarError(error);
                    } finally {
                        this.$finalizarCarga();
                    }
                },
            });
        },
        limpiar() {
            this.form = {
                id: undefined,
                codigo: '',
                nombre: '',
                descripcion: '',
                catalogoId: undefined,
            };
            this.collapseActivo = undefined;
            this.tituloFormulario = 'Agregar registro';
            this.$refs.form.resetFields();
        },
    },
};
</script>
