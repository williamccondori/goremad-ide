import { v4 as uuidv4 } from 'uuid';

export const state = () => ({
  /*----------  Mapa.  ----------*/

  centro: [0, 0],
  zoom: 0,
  bounds: undefined,
  informacionPosicion: {
    latitud: 0,
    longitud: 0,
    zoom: 0,
  },

  /*----------  Capas.  ----------*/

  capas: [],
  capasActivas: [],
  capasEstructura: [],
  capaSuperior: undefined,

  capasGEOJSON: [],

  informacionCapaOperativa: undefined,

  /*----------  Capas base.  ----------*/

  capasBase: [],
  capaBaseActiva: undefined,

  /*----------  Marcadores.  ----------*/

  marcadores: [],

  /*----------  Imagenes satelitales  ----------*/

  imagenesSatelitales: [],

  /*----------  Ventanas.  ----------*/

  estaAbiertoCapaCatalogoVentana: false,
  estaAbiertoCapaResumenVentana: false,
  estaAbiertoUbicacionVentana: false,
  estaAbiertoCoordenadaVentana: false,
  estaAbiertoDibujoVentana: false,
  estaAbiertoCapaBaseCatalogoVentana: false,
  estaAbiertoMarcadorCatalogoVentana: false,
  estaAbiertoMarcadorFormularioVentana: false,
  estaAbiertoImagenSatelitalCatalogoVentana: false,
  estaAbiertoImagenSatelitalBuscadorFormularioVentana: false,
  estaAbiertoAyudaVentana: false,
  estaAbiertoCompartirVistaModal: false,
  estaAbiertoComparacionVentana: false,
  estaAbiertoVentanaCapasOperables: false,
  estaAbiertoVentanaCapasInteroperables: false,
  estaAbiertoVentanaInformacionCapasOperables: false,
  estaAbiertoVentanaResultadoInformacionCapasOperables: false,
});

export const actions = {
  /*----------  Mapa.  ----------*/

  establecerCentro({ commit }, payload) {
    commit('establecerCentro', payload);
  },
  establecerZoom({ commit }, payload) {
    commit('establecerZoom', payload);
  },
  establecerBounds({ commit }, bounds) {
    commit('establecerBounds', bounds);
  },
  establecerInformacionPosicion({ commit }, payload) {
    if (payload.latitud || payload.longitud) {
      commit('establecerInformacionPosicionCentro', {
        latitud: payload.latitud,
        longitud: payload.longitud,
      });
    }
    if (payload.zoom) {
      commit('establecerInformacionPosicionZoom', payload.zoom);
    }
  },

  /*----------  Capas.  ----------*/

  agregarCapas({ commit }, capas) {
    commit('agregarCapas', capas);
  },
  establacerCapas({ commit }, capas) {
    commit('establecerCapas', capas);
  },
  establecerCapasActivas({ commit }, capasActivas) {
    commit('establecerCapasActivas', capasActivas);
  },
  establecerCapasEstructura({ commit }, capasEstructura) {
    commit('establecerCapasEstructura', capasEstructura);
  },
  establecerCapaTransparencia({ commit }, capaTransparencia) {
    commit('establecerCapaTransparencia', capaTransparencia);
  },
  establecerCapaSuperior({ commit }, capaSuperiorId) {
    commit('establecerCapaSuperior', capaSuperiorId);
  },
  eliminarCapaActiva({ commit }, capaActivaId) {
    commit('eliminarCapaActiva', capaActivaId);
  },
  agregarCapaOperativa({ commit }, capaOperativa) {
    commit('agregarCapaOperativa', capaOperativa);
  },
  eliminarCapaOperativa({ commit }, nombreCapaOperativa) {
    commit('eliminarCapaOperativa', nombreCapaOperativa);
  },
  establecerInformacionCapaOperativa({ commit }, informacionCapaOperativa) {
    commit('establecerInformacionCapaOperativa', informacionCapaOperativa);
  },

  /*----------  Capas base.  ----------*/

  establecerCapasBase({ commit }, capasBase) {
    commit('establecerCapasBase', capasBase);
  },
  establecerCapaBaseActiva({ commit }, capaBaseId) {
    commit('establecerCapaBaseActiva', capaBaseId);
  },

  /*----------  Marcadores.  ----------*/

  agregarMarcador({ commit }, marcador) {
    marcador.id = uuidv4();
    commit('agregarMarcador', marcador);
  },
  eliminarMarcador({ commit }, marcadorId) {
    commit('eliminarMarcador', marcadorId);
  },

  /*----------  Imagenes satelitales  ----------*/

  establecerImagenesSatelitales({ commit }, imagenesSatelitales) {
    commit('establecerImagenesSatelitales', imagenesSatelitales);
  },
  agregarImagenSatelital({ commit }, imagenSatelital) {
    commit('agregarImagenSatelital', imagenSatelital);
  },

  /*----------  Ventanas.  ----------*/

  abrirCapaCatalogoVentana({ commit }) {
    commit('establecerEstaAbiertoCapaCatalogoVentana', true);
  },
  cerrarCapaCatalogoVentana({ commit }) {
    commit('establecerEstaAbiertoCapaCatalogoVentana', false);
  },
  abrirCapaResumenVentana({ commit }) {
    commit('establecerEstaAbiertoCapaResumenVentana', true);
  },
  cerrarCapaResumenVentana({ commit }) {
    commit('establecerEstaAbiertoCapaResumenVentana', false);
  },
  abrirUbicacionVentana({ commit }) {
    commit('establecerEstaAbiertoUbicacionVentana', true);
  },
  cerrarUbicacionVentana({ commit }) {
    commit('establecerEstaAbiertoUbicacionVentana', false);
  },
  abrirCoordenadaVentana({ commit }) {
    commit('establecerEstaAbiertoCoordenadaVentana', true);
  },
  cerrarCoordenadaVentana({ commit }) {
    commit('establecerEstaAbiertoCoordenadaVentana', false);
  },
  abrirDibujoVentana({ commit }) {
    commit('establecerEstaAbiertoDibujoVentana', true);
  },
  cerrarDibujoVentana({ commit }) {
    commit('establecerEstaAbiertoDibujoVentana', false);
  },
  abrirCapaBaseCatalogoVentana({ commit }) {
    commit('establecerEstaAbiertoCapaBaseCatalogoVentana', true);
  },
  cerrarCapaBaseCatalogoVentana({ commit }) {
    commit('establecerEstaAbiertoCapaBaseCatalogoVentana', false);
  },
  abrirMarcadorCatalogoVentana({ commit }) {
    commit('establecerEstaAbiertoMarcadorCatalogoVentana', true);
  },
  cerrarMarcadorCatalogoVentana({ commit }) {
    commit('establecerEstaAbiertoMarcadorCatalogoVentana', false);
  },
  abrirMarcadorFormularioVentana({ commit }) {
    commit('establecerEstaAbiertoMarcadorFormularioVentana', true);
  },
  cerrarMarcadorFormularioVentana({ commit }) {
    commit('establecerEstaAbiertoMarcadorFormularioVentana', false);
  },
  abrirImagenSatelitalCatalogoVentana({ commit }) {
    commit('establecerEstaAbiertoImagenSatelitalCatalogoVentana', true);
  },
  cerrarImagenSatelitalCatalogoVentana({ commit }) {
    commit('establecerEstaAbiertoImagenSatelitalCatalogoVentana', false);
  },
  abrirImagenSatelitalBuscadorFormularioVentana({ commit }) {
    commit(
      'establecerEstaAbiertoImagenSatelitalBuscadorFormularioVentana',
      true
    );
  },
  cerrarImagenSatelitalBuscadorFormularioVentana({ commit }) {
    commit(
      'establecerEstaAbiertoImagenSatelitalBuscadorFormularioVentana',
      false
    );
  },
  abrirAyudaVentana({ commit }) {
    commit('establecerEstaAbiertoAyudaVentana', true);
  },
  cerrarAyudaVentana({ commit }) {
    commit('establecerEstaAbiertoAyudaVentana', false);
  },
  abrirCompartirVistaModal({ commit }) {
    commit('establecerEstaAbiertoCompartirVistaModal', true);
  },
  cerrarCompartirVistaModal({ commit }) {
    commit('establecerEstaAbiertoCompartirVistaModal', false);
  },
  abrirComparacionVentana({ commit }) {
    commit('establecerEstaAbiertoComparacionVentana', true);
  },
  cerrarComparacionVentana({ commit }) {
    commit('establecerEstaAbiertoComparacionVentana', false);
  },

  abrirVentana({ commit }, ventana) {
    commit(`establecerEstaAbiertoVentana`, { ventana, estaAbierto: true });
  },
  cerrarVentana({ commit }, ventana) {
    commit(`establecerEstaAbiertoVentana`, { ventana, estaAbierto: false });
  },
};

export const mutations = {
  /*----------  Mapa.  ----------*/

  establecerCentro(state, payload) {
    state.centro = payload;
  },
  establecerZoom(state, payload) {
    state.zoom = payload;
  },
  establecerBounds(state, payload) {
    state.bounds = payload;
  },
  establecerInformacionPosicionCentro(state, payload) {
    state.informacionPosicion.latitud = payload.latitud;
    state.informacionPosicion.longitud = payload.longitud;
  },
  establecerInformacionPosicionZoom(state, payload) {
    state.informacionPosicion.zoom = payload;
  },

  /*----------  Capas.  ----------*/

  agregarCapas(state, payload) {
    state.capas = [...state.capas, ...payload];
  },
  establecerCapas(state, payload) {
    state.capas = payload;
  },
  establecerCapasActivas(state, payload) {
    state.capasActivas = payload;
  },
  establecerCapasEstructura(state, payload) {
    state.capasEstructura = payload;
  },
  establecerCapaTransparencia(state, capaTransparencia) {
    const { id, transparencia } = capaTransparencia;
    const capa = state.capas.find((capa) => capa.id === id);
    capa.transparencia = transparencia;
  },
  establecerCapaSuperior(state, payload) {
    state.capaSuperior = payload;
  },
  eliminarCapaActiva(state, capaId) {
    state.capasActivas = state.capasActivas.filter(
      (capaActiva) => capaActiva !== capaId
    );
  },
  agregarCapaOperativa(state, capaOperativa) {
    const existe = state.capasGEOJSON.find(
      (capa) => capa.nombre === capaOperativa.nombre
    );
    if (!existe) {
      state.capasGEOJSON.push(capaOperativa);
    }
  },
  eliminarCapaOperativa(state, nombreCapaOperativa) {
    state.capasGEOJSON = state.capasGEOJSON.filter(
      (capa) => capa.nombre !== nombreCapaOperativa
    );
  },

  establecerInformacionCapaOperativa(state, informacionCapaOperativa) {
    state.informacionCapaOperativa = informacionCapaOperativa;
  },

  /*----------  Capas base.  ----------*/

  establecerCapasBase(state, payload) {
    state.capasBase = payload;
  },
  establecerCapaBaseActiva(state, payload) {
    state.capaBaseActiva = payload;
  },

  /*----------  Marcadores.  ----------*/

  agregarMarcador(state, payload) {
    state.marcadores.push(payload);
  },
  eliminarMarcador(state, payload) {
    state.marcadores = state.marcadores.filter(
      (marcador) => marcador.id !== payload
    );
  },

  /*----------  Imagenes satelitales  ----------*/

  establecerImagenesSatelitales(state, payload) {
    state.imagenesSatelitales = payload;
  },
  agregarImagenSatelital(state, payload) {
    state.imagenesSatelitales.push(payload);
  },

  /*----------  Ventanas.  ----------*/

  establecerEstaAbiertoCapaCatalogoVentana(state, payload) {
    state.estaAbiertoCapaCatalogoVentana = payload;
  },
  establecerEstaAbiertoCapaResumenVentana(state, payload) {
    state.estaAbiertoCapaResumenVentana = payload;
  },
  establecerEstaAbiertoUbicacionVentana(state, payload) {
    state.estaAbiertoUbicacionVentana = payload;
  },
  establecerEstaAbiertoCoordenadaVentana(state, payload) {
    state.estaAbiertoCoordenadaVentana = payload;
  },
  establecerEstaAbiertoDibujoVentana(state, payload) {
    state.estaAbiertoDibujoVentana = payload;
  },
  establecerEstaAbiertoCapaBaseCatalogoVentana(state, payload) {
    state.estaAbiertoCapaBaseCatalogoVentana = payload;
  },
  establecerEstaAbiertoMarcadorCatalogoVentana(state, payload) {
    state.estaAbiertoMarcadorCatalogoVentana = payload;
  },
  establecerEstaAbiertoMarcadorFormularioVentana(state, payload) {
    state.estaAbiertoMarcadorFormularioVentana = payload;
  },
  establecerEstaAbiertoImagenSatelitalCatalogoVentana(state, payload) {
    state.estaAbiertoImagenSatelitalCatalogoVentana = payload;
  },
  establecerEstaAbiertoImagenSatelitalBuscadorFormularioVentana(
    state,
    payload
  ) {
    state.estaAbiertoImagenSatelitalBuscadorFormularioVentana = payload;
  },
  establecerEstaAbiertoAyudaVentana(state, payload) {
    state.estaAbiertoAyudaVentana = payload;
  },
  establecerEstaAbiertoCompartirVistaModal(state, payload) {
    state.estaAbiertoCompartirVistaModal = payload;
  },
  establecerEstaAbiertoComparacionVentana(state, payload) {
    state.estaAbiertoComparacionVentana = payload;
  },

  establecerEstaAbiertoVentana(state, payload) {
    const nombreEstado = `estaAbiertoVentana${payload.ventana}`;
    state[nombreEstado] = payload.estaAbierto;
  },
};
