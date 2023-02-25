<template>
  <a-card size="small">
    <a-button html-type="button" type="dashed" block>
      Compartir vista
    </a-button>
    <a-divider />
    <a-button
      html-type="button"
      type="dashed"
      block
      @click="abrirUbicacionVentana()"
    >
      Buscar ubicaciones
    </a-button>
    <a-divider />
    <a-button
      html-type="button"
      type="dashed"
      block
      @click="abrirBuscadorCoordenadasVentana()"
    >
      Buscar por coordenadas
    </a-button>
    <a-divider />
    <a-button
      html-type="button"
      type="primary"
      block
      @click="abrirInformacionUsuarioVentana()"
    >
      Información del usuario
    </a-button>
    <a-divider />
    <a-switch v-model="permiteConsultaInformacion" size="small" /> Extraer
    información de las capas
    <CompartirVistaModal />
    <UbicacionVentana />
    <BuscadorCoordenadasVentana />
    <InformacionUsuarioVentana />
  </a-card>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  components: {},
  computed: {
    ...mapState("visor", ["consultarInformacion"]),
    permiteConsultaInformacion: {
      get() {
        return this.consultarInformacion;
      },
      set(valor) {
        this.establacerConsultarInformacion(valor);
      },
    },
  },
  methods: {
    ...mapActions("visor", [
      "abrirCompartirVistaModal",
      "abrirUbicacionVentana",
      "abrirBuscadorCoordenadasVentana",
      "abrirInformacionUsuarioVentana",
      "establacerConsultarInformacion",
    ]),
  },
};
</script>
