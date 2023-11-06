<template>
    <div style="min-height: 100vh">
        <a-spin :spinning="estaCargando">
            <div class="container">
                <Cabecera />
                <div class="fondo" style="height: calc(100vh - 60px)">
                    <a-layout style="height: 100%; background: none">
                        <AdministracionMenu v-if="$auth.loggedIn" />
                        <a-layout-content style="padding: 1rem">
                            <nuxt />
                        </a-layout-content>
                    </a-layout>
                </div>
            </div>
        </a-spin>
    </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';
import Cabecera from '@/components/compartido/Cabecera.vue';
import AdministracionMenu from '@/components/administrador/compartido/AdministracionMenu.vue';

export default {
    components: {
        Cabecera,
        AdministracionMenu,
    },
    computed: {
        ...mapState(['estaCargando']),
    },
    mounted() {
        window.addEventListener('resize', () => {
            this.establecerEsMovil(window.innerWidth < 720);
        });
    },
    methods: {
        ...mapActions(['establecerEsMovil']),
    },
};
</script>

<style scoped>
.fondo {
    background-size: 5px 5px;
    background-image: radial-gradient(
        hsla(215 28% 17% / 0.2) 0.5px,
        hsla(0 0% 95% / 1) 0.5px
    );
}
</style>
