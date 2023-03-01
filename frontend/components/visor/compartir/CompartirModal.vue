<template>
  <AModal
    :footer="null"
    :visible="estaAbiertoCompartirVistaModal"
    @cancel="cerrarCompartirVistaModal()"
  >
    <span slot="title" style="text-transform: uppercase">
      <b>Compartir</b>
    </span>
    <AFormModel
      ref="referenciaFormulario"
      :model="formulario"
      @submit.prevent="compartir()"
    >
      <AFormModelItem label="Ruta" prop="url">
        <AInput v-model="formulario.url" :read-only="true">
          <AIcon slot="addonBefore" type="global" />
        </AInput>
      </AFormModelItem>
      <AButton html-type="submit" type="primary" block icon="copy">
        Copiar y cerrar ventana
      </AButton>
    </AFormModel>
  </AModal>
</template>

<script>
import { Modal, FormModel, Input, Icon, Button } from "ant-design-vue";
import { mapState, mapActions } from "vuex";

const formulario = {
  url: "",
};

export default {
  components: {
    AModal: Modal,
    AFormModel: FormModel,
    AFormModelItem: FormModel.Item,
    AInput: Input,
    AIcon: Icon,
    AButton: Button,
  },
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
