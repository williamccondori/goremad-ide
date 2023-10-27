<template>
    <AdministracionPagina titulo="Servicios externos">
        <ASpace class="app--w-100" direction="vertical">
            <AButton
                icon="plus"
                type="primary"
                @click="abrirServicioExternoFormularioVentana()"
            >
                Crear servicio externo
            </AButton>
            <ServicioExternoCatalogo />
        </ASpace>
        <ServicioExternoFormularioVentana />
    </AdministracionPagina>
</template>

<script>
import { Button, Space } from 'ant-design-vue';
import { mapActions } from 'vuex';
import AdministracionPagina from '@/components/administrador/compartido/AdministracionPagina.vue';
import ServicioExternoCatalogo from '@/components/administrador/servicio-externo/ServicioExternoCatalogo.vue';
import ServicioExternoFormularioVentana from '@/components/administrador/servicio-externo/ServicioExternoFormularioVentana.vue';
export default {
    components: {
        AButton: Button,
        ASpace: Space,
        AdministracionPagina,
        ServicioExternoCatalogo,
        ServicioExternoFormularioVentana,
    },
    layout: 'administrador',
    methods: {
        ...mapActions('administrador', [
            'abrirServicioExternoFormularioVentana',
        ]),
    },
};
</script>
