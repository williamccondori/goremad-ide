<template>
    <ATable
        bordered
        :columns="columnas"
        :data-source="serviciosExternos"
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
                    title: 'Atribucion',
                    dataIndex: 'atribucion',
                    key: 'atribucion',
                },
                {
                    title: 'Nombre',
                    dataIndex: 'nombre',
                    key: 'nombre',
                },
                {
                    title: 'URL',
                    dataIndex: 'url',
                    key: 'url',
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
            await this.obtenerServiciosExternos();
        } catch (error) {
            this.$manejarError(error);
        } finally {
            this.$finalizarCarga();
        }
    },
    computed: {
        ...mapState('administrador', ['serviciosExternos']),
    },
    methods: {
        ...mapActions('administrador', [
            'obtenerServiciosExternos',
            'abrirServicioExternoFormularioActualizacionVentana',
        ]),
        async editar(servicioExternoId) {
            try {
                this.$iniciarCarga();
                const { data } = await this.$axios.get(
                    `/servicios-externos/${servicioExternoId}/`
                );
                this.abrirServicioExternoFormularioActualizacionVentana(data);
            } catch (error) {
                this.$manejarError(error);
            } finally {
                this.$finalizarCarga();
            }
        },
        async eliminar(servicioExternoId) {
            try {
                this.$iniciarCarga();
                await this.$axios.delete(
                    `/servicios-externos/${servicioExternoId}/`
                );
                await this.obtenerServiciosExternos();
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
