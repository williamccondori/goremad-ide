<template>
  <a-layout-sider v-model="esMovil" :width="esMovil ? 'auto' : '15rem'">
    <a-menu
      class="menu"
      theme="dark"
      :router="true"
      :default-selected-keys="[$route.path]"
      @click="seleccionarOpcion"
    >
      <a-menu-item key="/administrador">
        <a-icon type="home" />
        <span>Inicio</span>
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
      <a-menu-item key="/administrador/configuraciones">
        <a-icon type="setting" />
        <span>Configuraciones</span>
      </a-menu-item>
    </a-menu>
  </a-layout-sider>
</template>

<script>
import { mapState } from "vuex";
export default {
  computed: {
    ...mapState(["esMovil"]),
  },
  methods: {
    seleccionarOpcion({ key }) {
      this.$router.push(key);
    },
  },
};
</script>

<style scoped>
.menu {
  height: 100%;
}
</style>
