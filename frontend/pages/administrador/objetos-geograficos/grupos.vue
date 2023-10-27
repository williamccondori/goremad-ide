<template>
    <AdministracionPagina titulo="Grupos">
        <a-space direction="vertical" style="width: 100%">
            <a-form-model ref="form" :model="form" @submit.prevent="guardar()">
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
                <a-form-model-item label="Descripción" prop="descripcion">
                    <a-input
                        v-model="form.descripcion"
                        placeholder="Ingrese la descripción"
                        type="textarea"
                    />
                </a-form-model-item>
                <a-form-model-item
                    label="Tema"
                    prop="temaId"
                    :rules="{
                        required: true,
                        message: 'Seleccione el tema',
                    }"
                >
                    <a-select
                        v-model="form.temaId"
                        placeholder="Seleccione el tema"
                    >
                        <a-select-option v-for="tema in temas" :key="tema.id">
                            {{ tema.nombre }}
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
                        title: 'Tema',
                        dataIndex: 'temaNombre',
                        key: 'temaNombre',
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
                :data-source="grupos"
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
            form: {
                id: undefined,
                codigo: '',
                nombre: '',
                descripcion: '',
                temaId: undefined,
            },
            temas: [],
            grupos: [],
        };
    },
    async fetch() {
        await this.obtenerTemas();
        await this.obtenerGrupos();
    },
    methods: {
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
        async obtenerGrupos() {
            try {
                this.$iniciarCarga();
                const { data } = await this.$axios.get('/grupos/');
                this.grupos = data;
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
                    await this.$axios.put(
                        `/grupos/${this.form.id}/`,
                        this.form
                    );
                } else {
                    await this.$axios.post('/grupos/', this.form);
                }
                await this.obtenerGrupos();
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
                temaId: record.temaId,
            };
        },
        eliminar(record) {
            this.$confirm({
                title: '¿Está seguro de eliminar el grupo?',
                content: 'Esta acción no se puede revertir',
                okText: 'Sí',
                okType: 'danger',
                cancelText: 'No',
                onOk: async () => {
                    try {
                        this.$iniciarCarga();
                        await this.$axios.delete(`/grupos/${record.id}/`);
                        await this.obtenerGrupos();
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
                temaId: undefined,
            };
            this.$refs.form.resetFields();
        },
    },
};
</script>
