<template>
  <ALayoutSider v-model="esMovil" :width="esMovil ? 'auto' : '15rem'">
    <AMenu
      class="menu"
      theme="dark"
      :router="true"
      :default-selected-keys="[$route.path]"
      @click="seleccionarOpcion"
    >
      <AMenuItem key="/">
        <AIcon type="home" />
        <span>Inicio</span>
      </AMenuItem>
      <AMenuItem key="/visor-geogoremad">
        <AIcon type="appstore" />
        <span>Visor <b style="color: orange">GEOGOREMAD</b></span>
      </AMenuItem>
      <AMenuItem key="/interoperabilidad">
        <AIcon type="appstore" />
        <span>Interoperabilidad</span>
      </AMenuItem>
      <AMenuItem key="/administrador">
        <AIcon type="appstore" />
        <span>Portal de administración</span>
      </AMenuItem>
    </AMenu>
  </ALayoutSider>
</template>

<script>
import { mapState } from "vuex";
import { Menu, Icon, Layout } from "ant-design-vue";
export default {
  components: {
    AMenu: Menu,
    AMenuItem: Menu.Item,
    AIcon: Icon,
    ALayoutSider: Layout.Sider,
  },
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
