<template>
    <AdministracionPagina>
        <a-space class="app--w-100" direction="vertical">
            <a-alert
                :closable="false"
                description="Módulo de administración de contenidos de la plataforma geoespacial GEOGOREMAD."
                message="¡Bienvenido al módulo de administración del GEOGOREMAD!"
                type="success"
            />
            <div v-if="resumen" class="contenedor">
                <!--                <a-card hoverable>-->
                <!--                    <a-statistic-->
                <!--                        title="Total de servicios locales"-->
                <!--                        :value="resumen.totalServiciosLocales"-->
                <!--                    />-->
                <!--                </a-card>-->
                <a-card hoverable>
                    <a-statistic
                        title="Total de capas base"
                        :value="resumen.totalCapasBase"
                    />
                </a-card>
                <a-card hoverable>
                    <a-statistic
                        title="Total de servicios externos"
                        :value="resumen.totalServiciosExternos"
                    />
                </a-card>
                <a-card hoverable>
                    <a-statistic
                        title="Total de usuarios"
                        :value="resumen.totalUsuarios"
                    />
                </a-card>
            </div>
        </a-space>
    </AdministracionPagina>
</template>

<script>
import { mapActions, mapState } from 'vuex';
import AdministracionPagina from '@/components/administrador/compartido/AdministracionPagina.vue';

export default {
    components: {
        AdministracionPagina,
    },
    layout: 'administrador',
    async fetch() {
        try {
            this.$iniciarCarga();
            await this.obtenerResumen();
        } catch (error) {
            this.$manejarError(error);
        } finally {
            this.$finalizarCarga();
        }
    },
    computed: {
        ...mapState('administrador', ['resumen']),
    },
    methods: {
        ...mapActions('administrador', ['obtenerResumen']),
    },
};
</script>

<style scoped>
.contenedor {
    gap: 1rem;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
}
</style>
