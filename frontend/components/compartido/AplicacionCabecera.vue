<template>
  <div class="app--contenedor-horizontal-espaciado cabecera">
    <NuxtLink
      class="app--contenedor"
      style="align-items: center; gap: 1rem"
      to="/"
    >
      <img alt="logo" src="/logo.png" width="60" />
      <div v-if="!esMovil" class="titulo">
        <h1>
          <span>Infraestructura de Datos Espaciales</span>
        </h1>
        <h2>Gobierno Regional de Madre de Dios</h2>
      </div>
    </NuxtLink>
    <div v-if="$auth.loggedIn">
      <ADropdown>
        <AMenu slot="overlay" @click="seleccionarOpcion">
          <AMenuItem key="irVisor">
            <AIcon type="global" />
            Visor <b style="color: orange">GEOGOREMAD</b>
          </AMenuItem>
          <AMenuItem key="irAdministrador">
            <AIcon type="gold" />
            Administrador
          </AMenuItem>
          <AMenuItem key="cerrarSesion">
            <AIcon type="lock" />
            Cerrar sesión
          </AMenuItem>
        </AMenu>
        <AButton class="avatar" type="dashed">
          <AAvatar icon="user" shape="circle" />
          <span>
            {{ $auth.user?.username }}
          </span>
          <AIcon type="down" />
        </AButton>
      </ADropdown>
    </div>
  </div>
</template>

<script>
import { Avatar, Button, Dropdown, Icon, Menu } from 'ant-design-vue';
import { mapState } from 'vuex';
export default {
  components: {
    AAvatar: Avatar,
    AButton: Button,
    ADropdown: Dropdown,
    AIcon: Icon,
    AMenu: Menu,
    AMenuItem: Menu.Item,
  },
  computed: {
    ...mapState(['esMovil']),
  },
  methods: {
    seleccionarOpcion({ key }) {
      if (key === 'cerrarSesion') {
        this.$auth.logout();
      } else if (key === 'irAdministrador') {
        this.$router.push('/administrador');
      } else if (key === 'irVisor') {
        this.$router.push('/');
      }
    },
  },
};
</script>

<style scoped>
.cabecera {
  padding: 0 2rem;
  background-color: #212121;
  box-shadow: 0 2px 2px 0 rgb(0 0 0 / 14%), 0 3px 1px -2px rgb(0 0 0 / 12%),
    0 1px 5px 0 rgb(0 0 0 / 20%);
  z-index: 1000;
}
.avatar {
  display: flex;
  align-items: center;
  cursor: pointer;
  gap: 0.5rem;
}
.titulo h1,
.titulo h2 {
  margin: 0;
  padding: 0;
  font-weight: bold;
}
.titulo h1 span {
  color: green;
}
.titulo h2 {
  color: orange;
}
</style>
