<template>
  <a-modal
    :footer="null"
    :visible="estaAbiertoCompartirVistaModal"
    @cancel="cerrarCompartirVistaModal()"
  >
    <span slot="title">
      <b>Compartir</b>
    </span>
    <a-form-model
      ref="referenciaFormulario"
      :model="formulario"
      @submit.prevent="compartir()"
    >
      <a-form-model-item label="Ruta" prop="url">
        <a-input v-model="formulario.url" :read-only="true">
          <a-icon slot="addonBefore" type="global" />
        </a-input>
      </a-form-model-item>
      <a-button html-type="submit" type="primary" block icon="copy">
        Copiar y cerrar ventana
      </a-button>
    </a-form-model>
  </a-modal>
</template>

<script>
import { mapState, mapActions } from "vuex";

const formulario = {
  url: "",
};

export default {
  data() {
    return {
      formulario: { ...formulario },
    };
  },
  computed: {
    ...mapState("visor", [
      "estaAbiertoCompartirVistaModal",
      "informacionPosicion",
    ]),
  },
  watch: {
    estaAbiertoCompartirVistaModal(valor) {
      if (valor) {
        const urlBase = window.location.href.split("?")[0];
        const { latitud, longitud, zoom } = this.informacionPosicion;
        this.formulario.url = `${urlBase}?latitud=${latitud}&longitud=${longitud}&zoom=${zoom}`;
      }
    },
  },
  methods: {
    ...mapActions("visor", ["cerrarCompartirVistaModal"]),
    compartir() {
      navigator.clipboard.writeText(this.formulario.url);
      this.cerrarCompartirVistaModal();
    },
  },
};
</script>
