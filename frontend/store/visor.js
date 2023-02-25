import { v4 as uuidv4 } from "uuid";

const estadoInicial = {
  /*----------  Mapa.  ----------*/

  centro: [0, 0],
  zoom: 0,
  bounds: undefined,
  informacionPosicion: {
    latitud: 0,
    longitud: 0,
    zoom: 0,
  },

  /*----------  Configuracion.  ----------*/

  consultarInformacion: false,

  /*----------  Capas.  ----------*/

  capas: [],
  capasActivas: [],
  capasEstructura: [],
  capaSuperior: undefined,

  /*----------  Capas base.  ----------*/

  capasBase: [],
  capaBaseActiva: undefined,

  /*----------  Marcadores.  ----------*/

  marcadores: [],

  // Interoperabilidad
  capasInteroperables: [],
  capasInteroperablesEstructura: [
    {
      id: "root",
      label: "Todos los elementos",
      children: [],
    },
  ],
  capasInteroperablesActivas: [],

  // Ventanas
  estaAbiertoUbicacionVentana: false,
  estaAbiertoInformacionUsuarioVentana: false,
  estaAbiertoCoordenadaVentana: false,
  estaAbiertoDibujoVentana: false,
  estaAbiertoCompartirVistaModal: false,
  estaAbiertoCapaVentana: false,
  estaAbiertoCapaBaseVentana: false,
  estaAbiertoMarcadorVentana: false,
  estaAbiertoMarcadorFormularioVentana: false,
  estaAbiertoWebMapServiceFormularioVentana: false,
  estaAbiertoSubirArchivoVentana: false,
  estaAbiertoSubirArchivoFormularioVentana: false,
  estaAbiertoDescargarArchivoVentana: false,
  estaAbiertoInformacionCapaVentana: false,
  estaAbiertoCapaDetalleVentana: false,
  estaAbiertoCapaElementoVentana: false,
  estaAbiertoAyudaVentana: false,
};

export const state = () => ({
  ...estadoInicial,
});

export const actions = {
  /*----------  Mapa.  ----------*/

  establecerCentro({ commit }, payload) {
    commit("establecerCentro", payload);
  },
  establecerZoom({ commit }, payload) {
    commit("establecerZoom", payload);
  },
  establecerBounds({ commit }, bounds) {
    commit("establecerBounds", bounds);
  },
  establecerInformacionPosicion({ commit }, payload) {
    if (payload.latitud || payload.longitud) {
      commit("establecerInformacionPosicionCentro", {
        latitud: payload.latitud,
        longitud: payload.longitud,
      });
    }
    if (payload.zoom) {
      commit("establecerInformacionPosicionZoom", payload.zoom);
    }
  },

  // #region Consultar de informacion.

  establacerConsultarInformacion({ commit }, payload) {
    commit("ESTABLECER_CONSULTAR_INFORMACION", payload);
  },

  // #endregion

  /*----------  Capas.  ----------*/

  establacerCapas({ commit }, capas) {
    commit("establecerCapas", capas);
  },
  establecerCapasActivas({ commit }, capasActivas) {
    commit("establecerCapasActivas", capasActivas);
  },
  establecerCapasEstructura({ commit }, capasEstructura) {
    commit("establecerCapasEstructura", capasEstructura);
  },
  establecerCapaTransparencia({ commit }, capaTransparencia) {
    commit("establecerCapaTransparencia", capaTransparencia);
  },
  establecerCapaSuperior({ commit }, capaSuperiorId) {
    commit("establecerCapaSuperior", capaSuperiorId);
  },
  eliminarCapaActiva({ commit }, capaActivaId) {
    commit("eliminarCapaActiva", capaActivaId);
  },

  /*----------  Capas base.  ----------*/

  establecerCapasBase({ commit }, capasBase) {
    commit("establecerCapasBase", capasBase);
  },
  establecerCapaBaseActiva({ commit }, capaBaseId) {
    commit("establecerCapaBaseActiva", capaBaseId);
  },

  /*----------  Marcadores.  ----------*/

  agregarMarcador({ commit }, marcador) {
    marcador.id = uuidv4();
    commit("agregarMarcador", marcador);
  },
  eliminarMarcador({ commit }, marcadorId) {
    commit("eliminarMarcador", marcadorId);
  },

  // Interoperabilidad
  agregarCapaInteroperabilidad({ commit }, capa) {
    const idPrincipal = uuidv4();
    const capasInteroperables = capa.capas.map((x) => {
      return {
        id: uuidv4(),
        titulo: x.titulo,
        nombre: x.nombre,
        url: capa.url,
        capa: x.nombre,
        atribucion: capa.atribucion,
        grupoCapaId: idPrincipal,
      };
    });
    const capaInteoperableEstructura = {
      id: idPrincipal,
      label: capa.titulo,
      children: capasInteroperables.map((x) => {
        return {
          id: x.id,
          label: x.titulo,
        };
      }),
    };
    commit("AGREGAR_CAPAS_INTEROPERABLES", capasInteroperables);
    commit(
      "AGREGAR_CAPA_INTEROPERABLE_A_ESTRUCTURA",
      capaInteoperableEstructura
    );
  },
  establecerCapasInteroperablesActivas({ commit }, capasInteroperablesActivas) {
    commit(
      "ESTABLECER_CAPAS_INTEROPERABLES_ACTIVAS",
      capasInteroperablesActivas
    );
  },

  // Ventanas
  abrirUbicacionVentana({ commit }) {
    commit("ESTABLECER_UBICACION_VENTANA", true);
  },
  cerrarUbicacionVentana({ commit }) {
    commit("ESTABLECER_UBICACION_VENTANA", false);
  },
  abrirInformacionUsuarioVentana({ commit }) {
    commit("ESTABLECER_INFORMACION_USUARIO_VENTANA", true);
  },
  cerrarInformacionUsuarioVentana({ commit }) {
    commit("ESTABLECER_INFORMACION_USUARIO_VENTANA", false);
  },
  abrirCoordenadaVentana({ commit }) {
    commit("ESTABLECER_COORDENADA_VENTANA", true);
  },
  cerrarCoordenadaVentana({ commit }) {
    commit("ESTABLECER_COORDENADA_VENTANA", false);
  },
  abrirDibujoVentana({ commit }) {
    commit("ESTABLECER_DIBUJO_VENTANA", true);
  },
  cerrarDibujoVentana({ commit }) {
    commit("ESTABLECER_DIBUJO_VENTANA", false);
  },
  abrirCompartirVistaModal({ commit }) {
    commit("ESTABLECER_COMPARTIR_VISTA_MODAL", true);
  },
  cerrarCompartirVistaModal({ commit }) {
    commit("ESTABLECER_COMPARTIR_VISTA_MODAL", false);
  },
  abrirCapaVentana({ commit }) {
    commit("ESTABLECER_CAPA_VENTANA", true);
  },
  cerrarCapaVentana({ commit }) {
    commit("ESTABLECER_CAPA_VENTANA", false);
  },
  abrirCapaBaseVentana({ commit }) {
    commit("ESTABLECER_CAPA_BASE_VENTANA", true);
  },
  cerrarCapaBaseVentana({ commit }) {
    commit("ESTABLECER_CAPA_BASE_VENTANA", false);
  },
  abrirMarcadorVentana({ commit }) {
    commit("ESTABLECER_MARCADOR_VENTANA", true);
  },
  cerrarMarcadorVentana({ commit }) {
    commit("ESTABLECER_MARCADOR_VENTANA", false);
  },
  abrirMarcadorFormularioVentana({ commit }) {
    commit("ESTABLECER_MARCADOR_FORMULARIO_VENTANA", true);
  },
  cerrarMarcadorFormularioVentana({ commit }) {
    commit("ESTABLECER_MARCADOR_FORMULARIO_VENTANA", false);
  },
  abrirWebMapServiceFormularioVentana({ commit }) {
    commit("ESTABLECER_WEB_MAP_SERVICE_FORMULARIO_VENTANA", true);
  },
  cerrarWebMapServiceFormularioVentana({ commit }) {
    commit("ESTABLECER_WEB_MAP_SERVICE_FORMULARIO_VENTANA", false);
  },
  abrirSubirArchivoVentana({ commit }) {
    commit("ESTABLECER_SUBIR_ARCHIVO_VENTANA", true);
  },
  cerrarSubirArchivoVentana({ commit }) {
    commit("ESTABLECER_SUBIR_ARCHIVO_VENTANA", false);
  },
  abrirSubirArchivoFormularioVentana({ commit }) {
    commit("ESTABLECER_SUBIR_ARCHIVO_FORMULARIO_VENTANA", true);
  },
  cerrarSubirArchivoFormularioVentana({ commit }) {
    commit("ESTABLECER_SUBIR_ARCHIVO_FORMULARIO_VENTANA", false);
  },
  abrirDescargarArchivoVentana({ commit }) {
    commit("ESTABLECER_DESCARGAR_ARCHIVO_VENTANA", true);
  },
  cerrarDescargarArchivoVentana({ commit }) {
    commit("ESTABLECER_DESCARGAR_ARCHIVO_VENTANA", false);
  },
  abrirInformacionCapaVentana({ commit }) {
    commit("ESTABLECER_INFORMACION_CAPA_VENTANA", true);
  },
  cerrarInformacionCapaVentana({ commit }) {
    commit("ESTABLECER_INFORMACION_CAPA_VENTANA", false);
  },
  abrirCapaDetalleVentana({ commit }) {
    commit("ESTABLECER_CAPA_DETALLE_VENTANA", true);
  },
  cerrarCapaDetalleVentana({ commit }) {
    commit("ESTABLECER_CAPA_DETALLE_VENTANA", false);
  },
  abrirCapaElementoVentana({ commit }) {
    commit("ESTABLECER_CAPA_ELEMENTO_VENTANA", true);
  },
  cerrarCapaElementoVentana({ commit }) {
    commit("ESTABLECER_CAPA_ELEMENTO_VENTANA", false);
  },
  abrirAyudaVentana({ commit }) {
    commit("establecerEstaAbiertoAyudaVentana", true);
  },
  cerrarAyudaVentana({ commit }) {
    commit("establecerEstaAbiertoAyudaVentana", false);
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

  // Consultar informacion.
  ESTABLECER_CONSULTAR_INFORMACION(state, payload) {
    state.consultarInformacion = payload;
  },

  /*----------  Capas.  ----------*/

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

  // Interoperabilidad
  AGREGAR_CAPAS_INTEROPERABLES(state, payload) {
    payload.forEach((capaInteroperable) => {
      state.capasInteroperables.push(capaInteroperable);
    });
  },
  AGREGAR_CAPA_INTEROPERABLE_A_ESTRUCTURA(state, payload) {
    const root = state.capasInteroperablesEstructura.find(
      (capaInteroperable) => capaInteroperable.id === "root"
    );
    if (root) {
      root.children.push(payload);
    }
  },
  ESTABLECER_CAPAS_INTEROPERABLES_ACTIVAS(state, payload) {
    state.capasInteroperablesActivas = payload;
  },

  // Ventanas
  ESTABLECER_UBICACION_VENTANA(state, payload) {
    state.estaAbiertoUbicacionVentana = payload;
  },
  ESTABLECER_INFORMACION_USUARIO_VENTANA(state, payload) {
    state.estaAbiertoInformacionUsuarioVentana = payload;
  },
  ESTABLECER_COORDENADA_VENTANA(state, payload) {
    state.estaAbiertoCoordenadaVentana = payload;
  },
  ESTABLECER_DIBUJO_VENTANA(state, payload) {
    state.estaAbiertoDibujoVentana = payload;
  },
  ESTABLECER_COMPARTIR_VISTA_MODAL(state, payload) {
    state.estaAbiertoCompartirVistaModal = payload;
  },
  ESTABLECER_CAPA_VENTANA(state, payload) {
    state.estaAbiertoCapaVentana = payload;
  },
  ESTABLECER_CAPA_BASE_VENTANA(state, payload) {
    state.estaAbiertoCapaBaseVentana = payload;
  },
  ESTABLECER_MARCADOR_VENTANA(state, payload) {
    state.estaAbiertoMarcadorVentana = payload;
  },
  ESTABLECER_MARCADOR_FORMULARIO_VENTANA(state, payload) {
    state.estaAbiertoMarcadorFormularioVentana = payload;
  },
  ESTABLECER_WEB_MAP_SERVICE_FORMULARIO_VENTANA(state, payload) {
    state.estaAbiertoWebMapServiceFormularioVentana = payload;
  },
  ESTABLECER_SUBIR_ARCHIVO_VENTANA(state, payload) {
    state.estaAbiertoSubirArchivoVentana = payload;
  },
  ESTABLECER_SUBIR_ARCHIVO_FORMULARIO_VENTANA(state, payload) {
    state.estaAbiertoSubirArchivoFormularioVentana = payload;
  },
  ESTABLECER_DESCARGAR_ARCHIVO_VENTANA(state, payload) {
    state.estaAbiertoDescargarArchivoVentana = payload;
  },
  ESTABLECER_INFORMACION_CAPA_VENTANA(state, payload) {
    state.estaAbiertoInformacionCapaVentana = payload;
  },
  ESTABLECER_CAPA_DETALLE_VENTANA(state, payload) {
    state.estaAbiertoCapaDetalleVentana = payload;
  },
  ESTABLECER_CAPA_ELEMENTO_VENTANA(state, payload) {
    state.estaAbiertoCapaElementoVentana = payload;
  },
  establecerEstaAbiertoAyudaVentana(state, payload) {
    state.estaAbiertoAyudaVentana = payload;
  },
};
