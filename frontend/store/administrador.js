export const state = () => ({
  resumen: undefined,

  /*----------  Capas base.  ----------*/

  capasBase: [],
  capaBase: undefined,

  /*----------  Servicios externos.  ----------*/

  serviciosExternos: [],
  servicioExterno: undefined,

  /*----------  Grupos de capas.  ----------*/

  gruposCapas: [],
  estructuraGruposCapas: [],

  /*----------  Configuraciones.  ----------*/

  usuarios: [],
  usuario: undefined,
  configuraciones: [],

  /*----------  Ventanas.  ----------*/

  estaAbiertoCapaBaseFormularioVentana: false,
  estaAbiertoServicioExternoFormularioVentana: false,
  estaAbiertoUsuarioFormularioVentana: false,
  estaAbiertoRolFormularioVentana: false,
});

export const actions = {
  async obtenerResumen({ commit }) {
    const { data } = await this.$axios.get("/resumenes/");
    commit("establecerResumen", data);
  },

  /*----------  Capas base.  ----------*/

  async obtenerCapasBase({ commit }) {
    const { data } = await this.$axios.get("/capas-base/");
    commit("establecerCapasBase", data);
  },

  /*----------  Servicios externos.  ----------*/

  async obtenerServiciosExternos({ commit }, incluirCapas = false) {
    const { data } = await this.$axios.get("/servicios-externos/", {
      params: { incluirCapas: incluirCapas },
    });
    commit("establecerServiciosExternos", data);
  },

  /*----------  Grupos de capas.  ----------*/

  async obtenerGruposCapas({ commit }) {
    const { data } = await this.$axios.get("/grupos-capas/");
    commit("establecerGruposCapas", data);
  },
  async obtenerGruposCapasEstructura({ commit }) {
    const { data } = await this.$axios.get("/grupos-capas/estructuras/");
    commit("establecerGruposCapasEstructura", data);
  },

  /*----------  Configuraciones.  ----------*/

  async obtenerUsuarios({ commit }) {
    const { data } = await this.$axios.get("/usuarios/");
    commit("establecerUsuarios", data);
  },
  async obtenerConfiguraciones({ commit }) {
    const { data } = await this.$axios.get("/configuraciones/");
    commit("establecerConfiguraciones", data);
  },

  /*----------  Ventanas.  ----------*/

  abrirCapaBaseFormularioVentana({ commit }) {
    commit("establecerCapaBase", undefined);
    commit("establecerEstaAbiertoCapaBaseFormularioVentana", true);
  },
  abrirCapaBaseFormularioActualizacionVentana({ commit }, capaBase) {
    commit("establecerCapaBase", capaBase);
    commit("establecerEstaAbiertoCapaBaseFormularioVentana", true);
  },
  cerrarCapaBaseFormularioVentana({ commit }) {
    commit("establecerEstaAbiertoCapaBaseFormularioVentana", false);
  },
  abrirServicioExternoFormularioVentana({ commit }) {
    commit("establecerServicioExterno", undefined);
    commit("establecerEstaAbiertoServicioExternoFormularioVentana", true);
  },
  abrirServicioExternoFormularioActualizacionVentana(
    { commit },
    servicioExterno
  ) {
    commit("establecerServicioExterno", servicioExterno);
    commit("establecerEstaAbiertoServicioExternoFormularioVentana", true);
  },
  cerrarServicioExternoFormularioVentana({ commit }) {
    commit("establecerEstaAbiertoServicioExternoFormularioVentana", false);
  },
  abrirUsuarioFormularioVentana({ commit }) {
    commit("establecerUsuario", undefined);
    commit("establecerEstaAbiertoUsuarioFormularioVentana", true);
  },
  abrirUsuarioFormularioActualizacionVentana({ commit }, usuario) {
    commit("establecerUsuario", usuario);
    commit("establecerEstaAbiertoUsuarioFormularioVentana", true);
  },
  cerrarUsuarioFormularioVentana({ commit }) {
    commit("establecerEstaAbiertoUsuarioFormularioVentana", false);
  },
  abrirRolFormularioActualizacionVentana({ commit }, usuario) {
    commit("establecerUsuario", usuario);
    commit("establecerEstaAbiertoRolFormularioVentana", true);
  },
  cerrarRolFormularioVentana({ commit }) {
    commit("establecerEstaAbiertoRolFormularioVentana", false);
  },
};

export const mutations = {
  establecerResumen(state, payload) {
    state.resumen = payload;
  },

  /*----------  Capas base.  ----------*/

  establecerCapasBase(state, payload) {
    state.capasBase = payload;
  },
  establecerCapaBase(state, payload) {
    state.capaBase = payload;
  },

  /*----------  Servicios externos.  ----------*/

  establecerServiciosExternos(state, payload) {
    state.serviciosExternos = payload;
  },
  establecerServicioExterno(state, payload) {
    state.servicioExterno = payload;
  },

  /*----------  Grupo de capas.  ----------*/

  establecerGruposCapas(state, payload) {
    state.gruposCapas = payload;
  },
  establecerGruposCapasEstructura(state, payload) {
    state.estructuraGruposCapas = payload;
  },

  /*----------  Configuraciones.  ----------*/

  establecerUsuarios(state, payload) {
    state.usuarios = payload;
  },
  establecerUsuario(state, payload) {
    state.usuario = payload;
  },
  establecerConfiguraciones(state, payload) {
    state.configuraciones = payload;
  },

  /*----------  Ventanas.  ----------*/

  establecerEstaAbiertoCapaBaseFormularioVentana(state, payload) {
    state.estaAbiertoCapaBaseFormularioVentana = payload;
  },
  establecerEstaAbiertoServicioExternoFormularioVentana(state, payload) {
    state.estaAbiertoServicioExternoFormularioVentana = payload;
  },
  establecerEstaAbiertoUsuarioFormularioVentana(state, payload) {
    state.estaAbiertoUsuarioFormularioVentana = payload;
  },
  establecerEstaAbiertoRolFormularioVentana(state, payload) {
    state.estaAbiertoRolFormularioVentana = payload;
  },
};
