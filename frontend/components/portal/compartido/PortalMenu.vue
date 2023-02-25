<template>
  <a-layout-sider v-model="esMovil" :width="esMovil ? 'auto' : '15rem'">
    <a-menu
      class="menu"
      theme="dark"
      :router="true"
      :default-selected-keys="[$route.path]"
      @click="seleccionarOpcion"
    >
      <a-menu-item key="/">
        <a-icon type="home" />
        <span>Inicio</span>
      </a-menu-item>
      <a-menu-item key="/visor-geogoremad">
        <a-icon type="appstore" />
        <span>Visor <b style="color: orange">GEOGOREMAD</b></span>
      </a-menu-item>
      <a-menu-item key="/interoperabilidad">
        <a-icon type="appstore" />
        <span>Interoperabilidad</span>
      </a-menu-item>
      <a-menu-item key="/administrador">
        <a-icon type="appstore" />
        <span>Portal de administración</span>
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
