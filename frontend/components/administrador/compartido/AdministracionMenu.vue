<template>
  <ALayoutSider v-model="esMovil" :width="esMovil ? 'auto' : '15rem'">
    <AMenu
      class="menu"
      :default-selected-keys="[$route.path]"
      :router="true"
      theme="dark"
      @click="seleccionarOpcion"
    >
      <AMenuItem key="/administrador">
        <AIcon type="home" />
        <span>Inicio</span>
      </AMenuItem>
      <AMenuItem key="/administrador/capas-base">
        <AIcon type="camera" />
        <span>Capas base</span>
      </AMenuItem>
      <AMenuItem key="/administrador/servicios-externos">
        <AIcon type="global" />
        <span>Servicios externos</span>
      </AMenuItem>
      <AMenuItem key="/administrador/grupos-capas">
        <AIcon type="cluster" />
        <span>Grupos de capas</span>
      </AMenuItem>
      <AMenuItem key="/administrador/imagenes-satelitales">
        <AIcon type="picture" />
        <span>Imágenes satelitales</span>
      </AMenuItem>
      <AMenuItem key="/administrador/configuraciones">
        <AIcon type="setting" />
        <span>Configuraciones</span>
      </AMenuItem>
    </AMenu>
  </ALayoutSider>
</template>

<script>
import { Menu, Icon, Layout } from 'ant-design-vue';
import { mapState } from 'vuex';
export default {
  components: {
    AMenu: Menu,
    AMenuItem: Menu.Item,
    AIcon: Icon,
    ALayoutSider: Layout.Sider,
  },
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

<style scoped>
.menu {
  height: 100%;
}
</style>
