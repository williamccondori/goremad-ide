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
    capasOperativas: [],
    informacionObjetoGeografico: undefined,

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
    estaAbiertoVentanaDescargarInformacion: false,
    estaAbiertoVentanaBuscar: false,
    estaAbiertoVentanaSubirInformacion: false,
    estructuraObjetosGeograficos: [],
    estaAbiertoVentanaInformacionCapaWfs: false,
    informacionCapaGeojson: undefined,
    estaAbiertoVentanaImprimir: false,
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
    establacerCapasWms({ commit }, capas) {
        commit('establecerCapas', capas);
    },
    establecerCapasWmsActivas({ commit }, capasActivas) {
        commit('establecerCapasWmsActivas', capasActivas);
    },
    establecerEstructuraCapasInteroperables({ commit }, capasEstructura) {
        commit('establecerEstructuraCapasInteroperables', capasEstructura);
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
    agregarCapaEnMapa({ commit }, capaEnMapa) {
        commit('agregarCapaEnMapa', capaEnMapa);
    },
    eliminarCapaEnMapa({ commit }, capaId) {
        commit('eliminarCapaEnMapa', capaId);
    },
    eliminarTodasCapasEnMapa({ commit }) {
        commit('eliminarTodasCapasEnMapa');
    },
    establecerInformacionObjetoGeografico(
        { commit },
        informacionObjetoGeografico
    ) {
        commit(
            'establecerInformacionObjetoGeografico',
            informacionObjetoGeografico
        );
    },

    /*----------  Capas base.  ----------*/

    establecerMapasBase({ commit }, capasBase) {
        commit('establecerMapasBase', capasBase);
    },
    establecerMapaBaseActiva({ commit }, capaBaseId) {
        commit('establecerMapaBaseActiva', capaBaseId);
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
    abrirCompartirVistaModal({ commit }) {
        commit('establecerEstaAbiertoCompartirVistaModal', true);
    },
    cerrarCompartirVistaModal({ commit }) {
        commit('establecerEstaAbiertoCompartirVistaModal', false);
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

    establecerEstructuraObjetosGeograficos(
        { commit },
        estructuraObjetosGeograficos
    ) {
        commit(
            'establecerEstructuraObjetosGeograficos',
            estructuraObjetosGeograficos
        );
    },
    establecerInformacionCapaGeojson({ commit }, informacionCapaGeojson) {
        commit('establecerInformacionCapaGeojson', informacionCapaGeojson);
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
    establecerCapasWmsActivas(state, payload) {
        state.capasActivas = payload;
    },
    establecerEstructuraCapasInteroperables(state, payload) {
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
    agregarCapaEnMapa(state, capaOperativa) {
        const existe = state.capasOperativas.find(
            (capa) => capa.id === capaOperativa.id
        );
        if (!existe) {
            state.capasOperativas.push(capaOperativa);
        }
    },
    eliminarCapaEnMapa(state, capaOperativaId) {
        state.capasOperativas = state.capasOperativas.filter(
            (capa) => capa.id !== capaOperativaId
        );
    },
    eliminarTodasCapasEnMapa(state) {
        state.capasOperativas = [];
    },

    establecerInformacionObjetoGeografico(state, payload) {
        state.informacionObjetoGeografico = payload;
    },

    /*----------  Capas base.  ----------*/

    establecerMapasBase(state, payload) {
        state.capasBase = payload;
    },
    establecerMapaBaseActiva(state, payload) {
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
    establecerEstructuraObjetosGeograficos(state, payload) {
        state.estructuraObjetosGeograficos = payload;
    },
    establecerInformacionCapaGeojson(state, payload) {
        state.informacionCapaGeojson = payload;
    },
};
