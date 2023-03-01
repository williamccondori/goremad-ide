<template>
  <ADrawer
    :width="esMovil ? '100%' : 400"
    :mask-closable="false"
    :visible="estaAbiertoUsuarioFormularioVentana"
    @close="cerrarUsuarioFormularioVentana"
  >
    <span slot="title" style="text-transform: uppercase">
      <b>{{ titulo }}</b>
    </span>
    <a-form-model
      ref="referenciaFormulario"
      :model="formulario"
      @submit.prevent="guardar()"
    >
      <a-form-model-item
        prop="email"
        label="Correo electrónico:"
        :rules="[
          {
            required: true,
            message: 'Ingrese el correo electrónico del usuario',
          },
          {
            type: 'email',
            message: 'Ingrese un correo electrónico válido',
          },
        ]"
      >
        <a-input
          v-model="formulario.email"
          :disabled="esEdicion"
          placeholder="Ingrese el correo electrónico del usuario"
        />
      </a-form-model-item>
      <a-form-model-item
        prop="username"
        label="Usuario:"
        :rules="
          !esEdicion
            ? [
                {
                  required: true,
                  message: 'Ingrese el usuario',
                },
                {
                  pattern: /^[a-zA-Z0-9]+$/,
                  message: 'Ingrese un usuario válido',
                },
              ]
            : []
        "
      >
        <a-input
          v-model="formulario.username"
          :disabled="esEdicion"
          placeholder="Ingrese el usuario"
        />
      </a-form-model-item>
      <a-form-model-item
        prop="password"
        label="Contraseña:"
        :rules="
          !esEdicion
            ? [
                {
                  required: true,
                  message: 'Ingrese la contraseña del usuario',
                },
              ]
            : []
        "
      >
        <a-input-password
          v-model="formulario.password"
          :disabled="esEdicion"
          placeholder="Ingrese la contraseña del usuario"
        />
      </a-form-model-item>
      <a-form-model-item prop="nombres" label="Nombres:">
        <a-input
          v-model="formulario.nombres"
          placeholder="Ingrese los nombres del usuario"
        />
      </a-form-model-item>
      <a-form-model-item prop="apellidos" label="Apellidos:">
        <a-input
          v-model="formulario.apellidos"
          placeholder="Ingrese los apellidos del usuario"
        />
      </a-form-model-item>
      <a-form-model-item prop="estaHabilitado" label="¿Está habilitado?:">
        <a-checkbox v-model="formulario.estaHabilitado" />
      </a-form-model-item>
      <div>
        <a-button block html-type="submit" type="primary" icon="save">
          {{ titulo }}
        </a-button>
      </div>
    </a-form-model>
  </ADrawer>
</template>

<script>
import { Drawer } from "ant-design-vue";
import { mapState, mapActions } from "vuex";

const formulario = {
  email: "",
  username: "",
  password: "",
  nombres: undefined,
  apellidos: undefined,
  estaHabilitado: true,
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
      "estaAbiertoUsuarioFormularioVentana",
      "usuario",
    ]),
    esEdicion() {
      return this.usuario !== undefined;
    },
    titulo() {
      return this.esEdicion ? "Actualizar usuario" : "Crear usuario";
    },
  },
  watch: {
    estaAbiertoUsuarioFormularioVentana(value) {
      if (!value) {
        this.formulario = { ...formulario };
        this.$refs.referenciaFormulario?.resetFields();
      } else {
        if (this.esEdicion && this.usuario) {
          this.formulario.email = this.usuario.email;
          this.formulario.username = this.usuario.username;
          this.formulario.nombres = this.usuario.nombres;
          this.formulario.apellidos = this.usuario.apellidos;
          this.formulario.estaHabilitado = this.usuario.estaHabilitado;
        }
      }
    },
  },
  methods: {
    ...mapActions("administrador", [
      "cerrarUsuarioFormularioVentana",
      "obtenerUsuarios",
    ]),
    guardar() {
      this.$refs.referenciaFormulario?.validate(async (valid) => {
        if (valid) {
          try {
            this.$iniciarCarga();
            if (this.esEdicion) {
              await this.$axios.put(`/usuarios/${this.usuario.id}/`, {
                ...this.formulario,
              });
            } else {
              await this.$axios.post("/usuarios/", { ...this.formulario });
            }
            await this.obtenerUsuarios();
            this.cerrarUsuarioFormularioVentana();
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
