<template>
  <a-form-model
    ref="referenciaFormulario"
    :model="formulario"
    @submit.prevent="iniciarSesion()"
  >
    <a-form-model-item
      prop="username"
      :rules="[
        {
          required: true,
          message: 'Ingrese el nombre de usuario',
        },
      ]"
    >
      <a-input
        v-model="formulario.username"
        placeholder="Ingrese el nombre de usuario"
      >
        <template #prefix>
          <a-icon type="user" style="color: gray" />
        </template>
      </a-input>
    </a-form-model-item>
    <a-form-model-item
      prop="password"
      :rules="[
        {
          required: true,
          message: 'Ingrese la contraseña de usuario',
        },
      ]"
    >
      <a-input-password
        v-model="formulario.password"
        placeholder="Ingrese la contraseña de usuario"
      >
        <template #prefix>
          <a-icon type="key" style="color: gray" />
        </template>
      </a-input-password>
    </a-form-model-item>
    <div>
      <a-button html-type="submit" type="primary" block>
        Iniciar sesión
      </a-button>
      <a-divider />
      <a-button block @click="() => $router.push('/')">
        Regresar al inicio
      </a-button>
    </div>
  </a-form-model>
</template>

<script>
const formulario = {
  username: "",
  password: "",
};

export default {
  data() {
    return {
      formulario: { ...formulario },
    };
  },
  methods: {
    iniciarSesion() {
      this.$refs.referenciaFormulario?.validate(async (valid) => {
        if (valid) {
          try {
            this.$iniciarCarga();
            const formulario = new FormData();
            formulario.append("username", this.formulario.username);
            formulario.append("password", this.formulario.password);
            await this.$auth.loginWith("local", {
              data: formulario,
            });
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
