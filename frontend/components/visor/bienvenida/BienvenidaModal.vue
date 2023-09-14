<template>
  <a-modal
    class="modal-bienvenida"
    :closable="false"
    :footer="null"
    :title="null"
    :visible="estaAbiertoBienvenidaModal"
  >
    <div style="text-align: center">
      <div style="display: flex; justify-content: center; margin-bottom: 2rem">
        <div class="contenedor-imagen">
          <div class="borde grande borde1" />
          <div class="borde grande borde2" />
          <div class="borde pequeno borde3" />
          <div class="borde pequeno borde4" />
          <img id="logoPrincipal" alt="logo" src="/logo.png" />
        </div>
      </div>
      <h1 style="font-size: 1rem; color: orange">
        <b>GEOGOREMAD</b>
      </h1>
      <h2 style="font-size: 0.8rem; font-weight: bolder; color: green">
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
      block
      :disabled="!terminosAceptados"
      html-type="button"
      type="primary"
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

<style>
.modal-bienvenida .ant-modal-wrap .ant-modal-content .ant-modal-body,
.modal-bienvenida
  .ant-modal-wrap
  .ant-modal-content
  .ant-modal-body
  .ant-checkbox-wrapper {
  background-color: #212121 !important;
  color: white;
}

#logoPrincipal {
  border-radius: 50%;
  animation: palpitar 1s infinite alternate;
}

/* Variables */
:root {
  --imagen-tamano: 150px;
  --borde-grande-tamano: 150px;
  --borde-pequeno-tamano: 100px;
  --borde-grosor: 5px;
  --borde-desplazamiento: calc(var(--borde-grosor) * 1);
}

.contenedor-imagen {
  position: relative;
  width: var(--imagen-tamano);
  height: var(--imagen-tamano);
}

.contenedor-imagen img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  position: relative;
  z-index: 3;
}

.borde {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: var(--borde-grande-tamano);
  height: var(--borde-grande-tamano);
  border-radius: 50%;
  z-index: 1;
  box-sizing: border-box;
}

/* Bordes grandes */
.grande {
  width: var(--borde-grande-tamano);
  height: var(--borde-grande-tamano);
}

/* Bordes pequeños */
.pequeno {
  width: var(--borde-pequeno-tamano);
  height: var(--borde-pequeno-tamano);
  z-index: 2;
  top: calc((var(--borde-grande-tamano) - var(--borde-pequeno-tamano)) / 2);
  left: calc((var(--borde-grande-tamano) - var(--borde-pequeno-tamano)) / 2);
}

/* Primer borde grande */
.borde1 {
  border: var(--borde-grosor) solid transparent;
  border-top: var(--borde-grosor) solid green;
  border-right: var(--borde-grosor) solid green;
  animation: rotar 2.5s infinite linear;
}

/* Segundo borde grande */
.borde2 {
  border: var(--borde-grosor) solid transparent;
  border-bottom: var(--borde-grosor) solid orange;
  border-left: var(--borde-grosor) solid orange;
  animation: rotar 2.5s infinite linear;
}

/* Tercer borde pequeño */
.borde3 {
  background-color: rgb(255 255 255 / 56%);
  border: var(--borde-grosor) solid transparent;
  border-top: var(--borde-grosor) solid green;
  border-right: var(--borde-grosor) solid green;
  animation: rotarInverso 2.5s infinite linear;
  top: var(--borde-desplazamiento);
  left: var(--borde-desplazamiento);
  width: calc(var(--borde-grande-tamano) - 2 * var(--borde-desplazamiento));
  height: calc(var(--borde-grande-tamano) - 2 * var(--borde-desplazamiento));
}

/* Cuarto borde pequeño */
.borde4 {
  background-color: rgb(255 255 255 / 56%);
  border: var(--borde-grosor) solid transparent;
  border-bottom: var(--borde-grosor) solid orange;
  border-left: var(--borde-grosor) solid orange;
  animation: rotarInverso 2.5s infinite linear;
  top: var(--borde-desplazamiento);
  left: var(--borde-desplazamiento);
  width: calc(var(--borde-grande-tamano) - 2 * var(--borde-desplazamiento));
  height: calc(var(--borde-grande-tamano) - 2 * var(--borde-desplazamiento));
}

/* Animación para los bordes grandes */
@keyframes rotar {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

/* Animación para los bordes pequeños */
@keyframes rotarInverso {
  from {
    transform: rotate(360deg);
  }
  to {
    transform: rotate(0deg);
  }
}

@keyframes palpitar {
  from {
    transform: scale(1);
  }
  to {
    transform: scale(1.1);
  }
}
</style>
