<template>
  <div class="app--contenedor-horizontal-espaciado cabecera">
    <div class="app--contenedor" style="align-items: center; gap: 1rem">
      <img src="/logo.png" alt="logo" width="60" />
      <div class="titulo">
        <NuxtLink to="/">
          <h1>
            <span>Infraestructura de Datos Espaciales</span>
          </h1>
          <h2>Gobierno Regional de Madre de Dios</h2>
        </NuxtLink>
      </div>
    </div>
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
        <a-button type="dashed" class="avatar">
          <a-avatar shape="circle" icon="user" />
          <span>
            {{ $auth.user?.username }}
          </span>
          <a-icon type="down" />
        </a-button>
      </a-dropdown>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  computed: {
    ...mapState(["esMovil"]),
  },
  methods: {
    seleccionarOpcion({ key }) {
      if (key === "cerrarSesion") {
        this.$auth.logout();
      } else if (key === "irAdministrador") {
        this.$router.push("/administrador");
      } else if (key === "irVisor") {
        this.$router.push("/geogoremad");
      }
    },
  },
};
</script>

<style scoped>
.cabecera {
  z-index: 999;
  padding: 0 2rem;
  background-color: white;
  box-shadow: rgb(1 41 112 / 10%) 0px 2px 20px;
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
</style>
