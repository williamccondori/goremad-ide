<template>
    <a-spin :spinning="estaCargando">
        <div class="container">
            <Cabecera />
            <a-layout style="background: none">
                <AdministracionMenu v-if="$auth.loggedIn" />
                <a-layout-content style="padding: 1rem">
                    <nuxt />
                </a-layout-content>
            </a-layout>
        </div>
    </a-spin>
</template>

<script>
import { Layout, Spin } from 'ant-design-vue';
import { mapActions, mapState } from 'vuex';
import Cabecera from '@/components/compartido/Cabecera.vue';
import AdministracionMenu from '@/components/administrador/compartido/AdministracionMenu.vue';

export default {
    components: {
        ASpin: Spin,
        ALayout: Layout,
        ALayoutContent: Layout.Content,
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
.container {
    height: 100vh;
    display: grid;
    grid-template-rows: 60px 1fr;
    background-size: 5px 5px;
    background-image: radial-gradient(
        hsla(215 28% 17% / 0.2) 0.5px,
        hsla(0 0% 95% / 1) 0.5px
    );
}
</style>
