<template>
  <ADrawer
    :width="esMovil ? '100%' : 400"
    :mask-closable="false"
    :visible="estaAbiertoRolFormularioVentana"
    @close="cerrarRolFormularioVentana"
  >
    <span slot="title">
      <b>Actualizar roles</b>
    </span>
    <a-form-model
      ref="referenciaFormulario"
      :model="formulario"
      @submit.prevent="guardar()"
    >
      <a-form-model-item prop="esUsuario" label="Usuario:">
        <a-checkbox v-model="formulario.esUsuario" disabled />
      </a-form-model-item>
      <a-form-model-item prop="esAdministrador" label="Administrador:">
        <a-checkbox v-model="formulario.esAdministrador" />
      </a-form-model-item>
      <div>
        <a-button block html-type="submit" type="primary" icon="save">
          Actualizar roles
        </a-button>
      </div>
    </a-form-model>
  </ADrawer>
</template>

<script>
import { Drawer } from "ant-design-vue";
import { mapState, mapActions } from "vuex";

const formulario = {
  esUsuario: false,
  esAdministrador: false,
};

export default {
  components: {
    ADrawer: Drawer,
  },
  data() {
    return {
      formulario: { ...formulario },
    };
  },
  computed: {
    ...mapState(["esMovil"]),
    ...mapState("administrador", [
      "estaAbiertoRolFormularioVentana",
      "usuario",
    ]),
  },
  watch: {
    estaAbiertoRolFormularioVentana(value) {
      if (!value) {
        this.formulario = { ...formulario };
        this.$refs.referenciaFormulario?.resetFields();
      } else {
        const roles = this.usuario?.roles;
        if (roles) {
          this.formulario.esUsuario = roles.includes("usuario");
          this.formulario.esAdministrador = roles.includes("administrador");
        }
      }
    },
  },
  methods: {
    ...mapActions("administrador", [
      "cerrarRolFormularioVentana",
      "obtenerUsuarios",
    ]),
    guardar() {
      this.$refs.referenciaFormulario?.validate(async (valid) => {
        if (valid) {
          try {
            this.$iniciarCarga();
            await this.$axios.put(`/usuarios/${this.usuario.id}/roles/`, {
              ...this.formulario,
            });
            await this.obtenerUsuarios();
            this.cerrarRolFormularioVentana();
            this.$mostrarMensajeCorrecto();
          } catch (error) {
            this.$manejarError(error);
          } finally {
            this.$finalizarCarga();
          }
        }
      });
    },
  },
};
</script>
