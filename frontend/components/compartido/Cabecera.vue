<template>
  <div
    style="
      background-color: white;
      height: 60px;
      padding: 0 1rem;
      border-bottom: 2px solid orange;
    "
  >
    <a-row align="middle" justify="space-between" type="flex">
      <a-col>
        <NuxtLink style="display: flex; align-items: center; gap: 1rem" to="/">
          <img alt="logo" src="/logo.png" width="60" />
          <div v-if="!esMovil" class="titulo">
            <div>
              <b style="color: hsl(122, 39%, 49%)">
                Infraestructura de Datos Espaciales</b
              >
            </div>
            <div>
              <b style="color: orange">Gobierno Regional de Madre de Dios</b>
            </div>
          </div>
        </NuxtLink>
      </a-col>
      <a-col>
        <a-dropdown>
          <a-menu slot="overlay" @click="seleccionarOpcion">
            <a-menu-item key="irVisor">
              <a-icon type="global" />
              Visor
            </a-menu-item>
            <a-menu-item key="irAdministrador">
              <a-icon type="gold" />
              Administrador
            </a-menu-item>
            <a-menu-item v-if="$auth.loggedIn" key="cerrarSesion">
              <a-icon type="lock" />
              Cerrar sesión
            </a-menu-item>
          </a-menu>
          <a-button class="avatar" type="dashed">
            <a-avatar icon="user" shape="circle" style="margin-right: 0.5rem" />
            <span>
              {{ $auth.user?.username ?? 'Iniciar sesión' }}
            </span>
            <a-icon type="down" />
          </a-button>
        </a-dropdown>
      </a-col>
    </a-row>
  </div>
</template>
<script>
import { mapState } from 'vuex';
export default {
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
