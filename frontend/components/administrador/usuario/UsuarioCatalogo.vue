<template>
    <ATable
        bordered
        :columns="columnas"
        :data-source="usuarios"
        row-key="id"
        size="middle"
    >
        <template #acciones="id">
            <AButton size="small" type="dashed" @click="editar(id)">
                <AIcon type="edit" />
            </AButton>
            <APopconfirm
                title="¿Está seguro que desea eliminar este registro?"
                @confirm="eliminar(id)"
            >
                <AButton size="small" type="dashed">
                    <AIcon type="delete" />
                </AButton>
            </APopconfirm>
        </template>
    </ATable>
</template>

<script>
import { Table, Button, Popconfirm, Icon } from 'ant-design-vue';
import { mapState, mapActions } from 'vuex';
export default {
    components: {
        ATable: Table,
        AButton: Button,
        APopconfirm: Popconfirm,
        AIcon: Icon,
    },
    data() {
        return {
            columnas: [
                {
                    title: 'Usuario',
                    dataIndex: 'username',
                    key: 'username',
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
            await this.obtenerUsuarios();
        } catch (error) {
            this.$manejarError(error);
        } finally {
            this.$finalizarCarga();
        }
    },
    computed: {
        ...mapState('administrador', ['usuarios']),
    },
    methods: {
        ...mapActions('administrador', [
            'obtenerUsuarios',
            'abrirUsuarioFormularioActualizacionVentana',
        ]),
        async editar(usuarioId) {
            try {
                this.$iniciarCarga();
                const { data } = await this.$axios.get(
                    `/usuarios/${usuarioId}/`
                );
                this.abrirUsuarioFormularioActualizacionVentana(data);
            } catch (error) {
                this.$manejarError(error);
            } finally {
                this.$finalizarCarga();
            }
        },
        async eliminar(usuarioId) {
            try {
                this.$iniciarCarga();
                await this.$axios.delete(`/usuarios/${usuarioId}/`);
                await this.obtenerUsuarios();
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
