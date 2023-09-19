<template>
  <div style="padding: 0 2rem; background-color: white">
    <a-row align="middle" justify="space-between" type="flex">
      <a-col>
        <NuxtLink
          class="app--contenedor"
          style="align-items: center; gap: 1rem"
          to="/"
        >
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
        <div v-if="$auth.loggedIn">
          <a-dropdown>
            <a-menu slot="overlay" @click="seleccionarOpcion">
              <a-menu-item key="irVisor">
                <a-icon type="global" />
                Visor <b style="color: orange">GEOGOREMAD</b>
              </a-menu-item>
              <a-menu-item key="irAdministrador">
                <a-icon type="gold" />
                Administrador
              </a-menu-item>
              <a-menu-item key="cerrarSesion">
                <a-icon type="lock" />
                Cerrar sesión
              </a-menu-item>
            </a-menu>
            <AButton class="avatar" type="dashed">
              <a-avatar
                icon="user"
                shape="circle"
                style="margin-right: 0.5rem"
              />
              <span>
                {{ $auth.user?.username }}
              </span>
              <a-icon type="down" />
            </AButton>
          </a-dropdown>
        </div>
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
