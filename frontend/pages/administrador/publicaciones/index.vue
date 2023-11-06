<template>
    <AdministracionPagina titulo="Publicaciones">
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
                            label="Tipo"
                            prop="tipo"
                            :rules="{
                                required: true,
                                message: 'Seleccione el tipo',
                            }"
                        >
                            <a-select
                                v-model="form.tipo"
                                placeholder="Seleccione el tipo"
                            >
                                <a-select-option
                                    v-for="tipoPublicacion in tiposPublicacion"
                                    :key="tipoPublicacion.id"
                                >
                                    {{ tipoPublicacion.nombre }}
                                </a-select-option>
                            </a-select>
                        </a-form-model-item>
                        <a-form-model-item
                            label="Título"
                            prop="titulo"
                            :rules="{
                                required: true,
                                message: 'Ingrese el título',
                            }"
                        >
                            <a-input
                                v-model="form.titulo"
                                placeholder="Ingrese el título"
                            />
                        </a-form-model-item>
                        <a-form-model-item
                            label="Resumen"
                            prop="resumen"
                            :rules="{
                                required: true,
                                message: 'Ingrese el resumen',
                            }"
                        >
                            <a-input
                                v-model="form.resumen"
                                placeholder="Ingrese el resumen"
                                type="textarea"
                            />
                        </a-form-model-item>
                        <a-form-model-item
                            v-if="form.tipo !== tipoPublicacionDocumento"
                            label="Contenido"
                            prop="contenido"
                        >
                            <a-input
                                v-model="form.contenido"
                                placeholder="Ingrese el contenido"
                                type="textarea"
                            />
                        </a-form-model-item>
                        <a-form-model-item label="Imagen" prop="imagen">
                            <a-input
                                v-model="form.imagen"
                                placeholder="Ingrese la URL de una imagen"
                            />
                        </a-form-model-item>
                        <a-form-model-item
                            label="¿Está habilitado?"
                            prop="estaHabilitado"
                        >
                            <a-switch v-model="form.estaHabilitado" />
                        </a-form-model-item>
                        <a-button html-type="submit" type="primary">
                            <a-icon type="save" />
                            Guardar
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
                        title: 'Tipo',
                        dataIndex: 'tipo',
                        key: 'tipo',
                        scopedSlots: { customRender: 'tipo' },
                    },
                    {
                        title: 'Título',
                        dataIndex: 'titulo',
                        key: 'titulo',
                    },
                    {
                        title: '¿Habilitado?',
                        dataIndex: 'estaHabilitado',
                        key: 'estaHabilitado',
                        scopedSlots: { customRender: 'estaHabilitado' },
                    },
                    {
                        title: 'Acciones',
                        key: 'acciones',
                        scopedSlots: { customRender: 'acciones' },
                    },
                ]"
                :data-source="publicaciones"
                row-key="id"
                size="small"
            >
                <div slot="tipo" slot-scope="valor">
                    <a-tag color="purple">
                        {{ obtenerTipoPublicacion(valor) }}
                    </a-tag>
                </div>
                <div slot="estaHabilitado" slot-scope="valor">
                    <a-tag :color="valor ? 'green' : 'red'">
                        {{ valor ? 'Si' : 'No' }}
                    </a-tag>
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
import AdministracionPagina from '~/components/administrador/compartido/AdministracionPagina.vue';
import { LISTA_TIPOS_PUBLICACION } from '~/compartido/constantes';

export default {
    components: { AdministracionPagina },
    layout: 'administrador',
    data() {
        return {
            collapseActivo: undefined,
            tituloFormulario: 'Agregar registro',
            form: {
                id: undefined,
                tipo: undefined,
                titulo: '',
                resumen: '',
                contenido: '',
                imagen: '',
                estaHabilitado: true,
            },
            tiposPublicacion: [],
            publicaciones: [],
            tipoPublicacionDocumento: 'documento',
        };
    },
    async fetch() {
        await this.obtenerPublicaciones();
        this.obtenerTiposPublicacion();
    },
    methods: {
        async obtenerPublicaciones() {
            try {
                this.$iniciarCarga();
                const { data } = await this.$axios.get('/publicaciones/');
                this.publicaciones = data;
            } catch (error) {
                this.$manejarError(error);
            } finally {
                this.$finalizarCarga();
            }
        },
        obtenerTipoPublicacion(tipo) {
            const tipoPublicacion = this.tiposPublicacion.find(
                (item) => item.id === tipo
            );
            return tipoPublicacion ? tipoPublicacion.nombre : '';
        },
        obtenerTiposPublicacion() {
            this.tiposPublicacion = [...LISTA_TIPOS_PUBLICACION];
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
                    await this.$axios.put(
                        `/publicaciones/${this.form.id}/`,
                        this.form
                    );
                } else {
                    await this.$axios.post('/publicaciones/', this.form);
                }
                await this.obtenerPublicaciones();
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
                tipo: record.tipo,
                titulo: record.titulo,
                resumen: record.resumen,
                contenido: record.contenido,
                imagen: record.imagen,
                estaHabilitado: record.estaHabilitado,
            };
            this.tituloFormulario = 'Editar registro';
            this.collapseActivo = 'formularioPanel';
        },
        async eliminar(record) {
            this.$confirm({
                title: '¿Está seguro de eliminar la publicación?',
                content: 'Esta acción no se puede revertir',
                okText: 'Sí',
                okType: 'danger',
                cancelText: 'No',
                onOk: async () => {
                    try {
                        this.$iniciarCarga();
                        await this.$axios.delete(
                            `/publicaciones/${record.id}/`
                        );
                        await this.obtenerPublicaciones();
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
                tipo: undefined,
                titulo: '',
                resumen: '',
                contenido: '',
                imagen: '',
                estaHabilitado: true,
            };
            this.collapseActivo = undefined;
            this.tituloFormulario = 'Agregar registro';
            this.$refs.form.resetFields();
        },
    },
};
</script>

<style scoped></style>
