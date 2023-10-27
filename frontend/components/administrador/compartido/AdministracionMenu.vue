<template>
    <a-layout-sider v-model="esMovil" :width="esMovil ? 'auto' : '15rem'">
        <a-menu
            :default-selected-keys="[$route.path]"
            :router="true"
            style="height: 100%"
            @click="(opcion) => seleccionarOpcion(opcion)"
        >
            <a-menu-item key="/administrador">
                <a-icon type="home" />
                <span>Inicio</span>
            </a-menu-item>
            <a-menu-item key="/administrador/objetos-geograficos">
                <a-icon type="cluster" />
                <span>Objetos geográficos</span>
            </a-menu-item>
            <a-menu-item key="/administrador/capas-base">
                <a-icon type="camera" />
                <span>Capas base</span>
            </a-menu-item>
            <a-menu-item key="/administrador/servicios-externos">
                <a-icon type="global" />
                <span>Servicios externos</span>
            </a-menu-item>
            <a-menu-item key="/administrador/grupos-capas">
                <a-icon type="cluster" />
                <span>Grupos de capas</span>
            </a-menu-item>
            <a-menu-item key="/administrador/imagenes-satelitales">
                <a-icon type="picture" />
                <span>Imágenes satelitales</span>
            </a-menu-item>
            <a-menu-item key="/administrador/configuraciones">
                <a-icon type="setting" />
                <span>Configuraciones</span>
            </a-menu-item>
        </a-menu>
    </a-layout-sider>
</template>

<script>
import { mapState } from 'vuex';
export default {
    computed: {
        ...mapState(['esMovil']),
    },
    methods: {
        seleccionarOpcion({ key }) {
            this.$router.push(key);
        },
    },
};
</script>
