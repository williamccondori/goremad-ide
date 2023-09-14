<template>
  <AFormModel
    ref="referenciaFormulario"
    :model="formulario"
    @submit.prevent="iniciarSesion()"
  >
    <AFormModelItem
      prop="username"
      :rules="[
        {
          required: true,
          message: 'Ingrese el nombre de usuario',
        },
      ]"
    >
      <AInput
        v-model="formulario.username"
        placeholder="Ingrese el nombre de usuario"
      >
        <template #prefix>
          <AIcon style="color: gray" type="user" />
        </template>
      </AInput>
    </AFormModelItem>
    <AFormModelItem
      prop="password"
      :rules="[
        {
          required: true,
          message: 'Ingrese la contraseña de usuario',
        },
      ]"
    >
      <AInputPassword
        v-model="formulario.password"
        placeholder="Ingrese la contraseña de usuario"
      >
        <template #prefix>
          <AIcon style="color: gray" type="key" />
        </template>
      </AInputPassword>
    </AFormModelItem>
    <div>
      <AButton block html-type="submit" type="primary">
        Iniciar sesión
      </AButton>
      <ADivider />
      <AButton block @click="() => $router.push('/')">
        Regresar al inicio
      </AButton>
    </div>
  </AFormModel>
</template>

<script>
import { FormModel, Input, Icon, Button, Divider } from 'ant-design-vue';

const formulario = {
  username: '',
  password: '',
};

export default {
  components: {
    AFormModel: FormModel,
    AFormModelItem: FormModel.Item,
    AInput: Input,
    AInputPassword: Input.Password,
    AIcon: Icon,
    AButton: Button,
    ADivider: Divider,
  },
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
            formulario.append('username', this.formulario.username);
            formulario.append('password', this.formulario.password);
            await this.$auth.loginWith('local', {
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
