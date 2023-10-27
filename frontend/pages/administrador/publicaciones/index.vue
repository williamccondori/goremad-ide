<script>
import AdministracionPagina from '~/components/administrador/compartido/AdministracionPagina.vue';

export default {
    name: 'Index',
    components: { AdministracionPagina },
};
</script>

<template>
    <AdministracionPagina>
        <a-space direction="vertical" style="width: 100%">
            <div>Página</div>
        </a-space>
    </AdministracionPagina>
</template>

<style scoped></style>
