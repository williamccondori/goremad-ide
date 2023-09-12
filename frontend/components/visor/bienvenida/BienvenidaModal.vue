<template>
  <a-modal
    :title="null"
    :footer="null"
    :closable="false"
    :visible="estaAbiertoBienvenidaModal"
  >
    <div style="text-align: center">
      <img src="/logo.png" alt="logo" style="width: 8rem" />
      <h1 style="font-size: 1rem; font-weight: bolder; color: orange">
        GEOGOREMAD
      </h1>
      <h2 style="font-size: 1rem; font-weight: bolder; color: green">
        Infraestructura de Datos Espaciales
      </h2>
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
    <a-checkbox v-model="terminosAceptados">
      Acepto los términos y condiciones de uso.
    </a-checkbox>
    <a-divider />
    <a-button
      html-type="button"
      type="primary"
      :disabled="!terminosAceptados"
      block
      @click="cerrarModal()"
    >
      Ingresar
    </a-button>
  </a-modal>
</template>

<script>
export default {
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
