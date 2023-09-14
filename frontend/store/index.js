export const state = () => ({
  /**
   * Indica si se esta cargando algun dato.
   */
  estaCargando: false,
  /**
   * Indica si el tamanio de la pantalla representa un dispositivo movil.
   */
  esMovil: window.innerWidth < 720,
  tamanioVentana: window.innerWidth < 720 ? '100%' : '400',
});

export const actions = {
  establecerCargando({ commit }, payload) {
    commit('establecerCargando', payload);
  },
  establecerEsMovil({ commit }, esMovil) {
    commit('establecerEsMovil', esMovil);
  },
  actualizarTamanioVentana({ commit }, tamanioVentana) {
    const nuevoTamanioVentana = tamanioVentana < 720 ? '100%' : '400';
    commit('establecerTamanioVentana', nuevoTamanioVentana);
  },
};

export const mutations = {
  establecerCargando: (state, payload) => (state.estaCargando = payload),
  establecerEsMovil: (state, payload) => (state.esMovil = payload),
  establecerTamanioVentana: (state, nuevoTamanioVentana) =>
    (state.tamanioVentana = nuevoTamanioVentana),
};
