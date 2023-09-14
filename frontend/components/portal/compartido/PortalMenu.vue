<template>
  <ALayoutSider v-model="esMovil" :width="esMovil ? 'auto' : '15rem'">
    <AMenu
      class="menu"
      :default-selected-keys="[$route.path]"
      :router="true"
      theme="dark"
      @click="seleccionarOpcion"
    >
      <AMenuItem key="/portal">
        <AIcon type="home" />
        <span>Inicio</span>
      </AMenuItem>
      <AMenuItem key="/portal/interoperabilidad">
        <AIcon type="global" />
        <span>Interoperabilidad</span>
      </AMenuItem>
      <AMenuItem key="/portal/catalogo-objetos">
        <AIcon type="folder" />
        <span>Catálogo de objetos</span>
      </AMenuItem>
      <AMenuItem key="/administrador">
        <AIcon type="apartment" />
        <span>Portal de administración</span>
      </AMenuItem>
    </AMenu>
  </ALayoutSider>
</template>

<script>
import { mapState } from 'vuex';
import { Menu, Icon, Layout } from 'ant-design-vue';
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
