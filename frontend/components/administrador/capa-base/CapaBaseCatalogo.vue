<template>
    <a-table
        bordered
        :columns="columnas"
        :data-source="capasBase"
        row-key="id"
        size="middle"
    >
        <template #acciones="id">
            <a-button size="small" type="dashed" @click="editar(id)">
                <AIcon type="edit" />
            </a-button>
            <a-popconfirm
                title="¿Está seguro que desea eliminar este registro?"
                @confirm="eliminar(id)"
            >
                <a-button size="small" type="dashed">
                    <AIcon type="delete" />
                </a-button>
            </a-popconfirm>
        </template>
    </a-table>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
    data() {
        return {
            columnas: [
                {
                    title: 'Nombre',
                    dataIndex: 'nombre',
                    key: 'nombre',
                },
                {
                    title: 'Acciones',
                    dataIndex: 'id',
                    key: 'id',
                    scopedSlots: {
                        customRender: 'acciones',
                    },
                },
            ],
        };
    },
    async fetch() {
        try {
            this.$iniciarCarga();
            await this.obtenerCapasBase();
        } catch (error) {
            this.$manejarError(error);
        } finally {
            this.$finalizarCarga();
        }
    },
    computed: {
        ...mapState('administrador', ['capasBase']),
    },
    methods: {
        ...mapActions('administrador', [
            'obtenerCapasBase',
            'abrirCapaBaseFormularioActualizacionVentana',
        ]),
        async editar(capaBaseId) {
            try {
                this.$iniciarCarga();
                const { data } = await this.$axios.get(
                    `/capas-base/${capaBaseId}/`
                );
                this.abrirCapaBaseFormularioActualizacionVentana(data);
            } catch (error) {
                this.$manejarError(error);
            } finally {
                this.$finalizarCarga();
            }
        },
        async eliminar(capaBaseId) {
            try {
                this.$iniciarCarga();
                await this.$axios.delete(`/capas-base/${capaBaseId}/`);
                await this.obtenerCapasBase();
                this.$mostrarMensajeCorrecto();
            } catch (error) {
                this.$manejarError(error);
            } finally {
                this.$finalizarCarga();
            }
        },
    },
};
</script>
