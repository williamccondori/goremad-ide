<template>
  <AdministracionPagina titulo="Configuraciones">
    <a-tabs type="card">
      <a-tab-pane key="1" tab="Usuarios">
        <a-space direction="vertical" class="app--w-100">
          <a-button
            type="primary"
            icon="plus"
            @click="abrirUsuarioFormularioVentana()"
          >
            Crear usuario
          </a-button>
          <UsuarioCatalogo />
        </a-space>
        <UsuarioFormularioVentana />
      </a-tab-pane>
      <a-tab-pane key="2" tab="Roles">
        <RolCatalogo />
        <RolFormularioVentana />
      </a-tab-pane>
      <a-tab-pane key="3" tab="Variables">
        <VariableFormulario />
      </a-tab-pane>
    </a-tabs>
  </AdministracionPagina>
</template>

<script>
import { mapActions } from "vuex";
import AdministracionPagina from "@/components/administrador/compartido/AdministracionPagina.vue";
import UsuarioCatalogo from "@/components/administrador/usuario/UsuarioCatalogo.vue";
import UsuarioFormularioVentana from "@/components/administrador/usuario/UsuarioFormularioVentana.vue";
import RolCatalogo from "@/components/administrador/rol/RolCatalogo.vue";
import RolFormularioVentana from "@/components/administrador/rol/RolFormularioVentana.vue";
import VariableFormulario from "~/components/administrador/variable/VariableFormulario.vue";
export default {
  components: {
    AdministracionPagina,
    UsuarioCatalogo,
    UsuarioFormularioVentana,
    RolCatalogo,
    RolFormularioVentana,
    VariableFormulario,
  },
  layout: "administrador",
  methods: {
    ...mapActions("administrador", ["abrirUsuarioFormularioVentana"]),
  },
};
</script>
