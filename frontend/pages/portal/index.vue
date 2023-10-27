<template>
    <PortalPagina>
        <a-alert
            description="En esta página podrás encontrar información geográfica de la región, así como también información de los servicios que ofrece el Gobierno Regional de Madre de Dios."
            message="¡Bienvenido a la Infraestructura de Datos Espaciales del Gobierno Regional de Madre de Dios!"
            type="success"
        />
        <a-button @click="irCatalogoMetadatos()">
            Catálogo de Metadatos
        </a-button>
        <a-button @click="irSistemaCentrosPoblados()">
            Sistema de Categorización de Centros Poblados
        </a-button>
    </PortalPagina>
</template>

<script>
import PortalPagina from '@/components/portal/compartido/PortalPagina.vue';
export default {
    components: {
        PortalPagina,
    },
    auth: false,
    layout: 'portal',
    methods: {
        irCatalogoMetadatos() {
            window.open(
                'https://metadatos.ide.regionmadrededios.gob.pe/geonetwork',
                '_blank'
            );
        },
        irSistemaCentrosPoblados() {
            window.open(
                'https://centrospoblados.regionmadrededios.gob.pe',
                '_blank'
            );
        },
    },
};
</script>
