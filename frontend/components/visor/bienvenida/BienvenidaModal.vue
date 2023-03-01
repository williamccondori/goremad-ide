<template>
  <AModal
    :title="null"
    :footer="null"
    :closable="false"
    :visible="estaAbiertoBienvenidaModal"
  >
    <div class="cabecera">
      <NuxtImg src="/logo.png" alt="logo" provider="static" />
      <h1>GEOGOREMAD</h1>
      <h2>Infraestructura de Datos Espaciales</h2>
    </div>
    <div style="text-align: justify">
      <p>
        Una <b>Infraestructura de Datos Espaciales (IDE)</b> es el conjunto de
        políticas, estándares, organizaciones, recursos humanos y recursos
        tecnológicos que facilitan el intercambio, la producción, obtención, uso
        y acceso de la información espacial a nivel regional y nacional, a fin
        de apoyar el desarrollo territorial del departamento de Madre de Dios
        para favorecer la oportuna toma de decisiones. Es por ello que se ha
        desarrollado la presente plataforma tecnológica, la cual lleva por
        nombre <b>GEOGOREMAD</b>. Es importante precisar, que la información
        disponible en esta plataforma se encuentra en constante actualización.
        Esto es debido a la realización de nuevos estudios o a la corrección de
        información errónea.
      </p>
    </div>
    <ACheckbox v-model="terminosAceptados">
      Acepto los términos y condiciones de uso.
    </ACheckbox>
    <ADivider />
    <AButton
      html-type="button"
      type="primary"
      :disabled="!terminosAceptados"
      block
      @click="cerrarModal()"
    >
      Ingresar
    </AButton>
  </AModal>
</template>

<script>
import { Modal, Checkbox, Divider, Button } from "ant-design-vue";
export default {
  components: {
    AModal: Modal,
    ACheckbox: Checkbox,
    ADivider: Divider,
    AButton: Button,
  },
  data() {
    return {
      terminosAceptados: false,
      estaAbiertoBienvenidaModal: true,
    };
  },
  methods: {
    cerrarModal() {
      this.estaAbiertoBienvenidaModal = false;
    },
  },
};
</script>

<style scoped>
.cabecera {
  text-align: center;
}
.cabecera img {
  width: 8rem;
}
.cabecera h1,
.cabecera h2 {
  font-size: 1rem;
  font-weight: bolder;
}
.cabecera h1 {
  color: orange;
}
.cabecera h2 {
  color: green;
}
</style>
