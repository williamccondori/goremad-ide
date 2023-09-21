<template>
  <div v-if="configuracionAplicada" class="app--pagina">
    <a-spin :spinning="estaCargando">
      <div
        style="
          height: 100%;
          display: grid;
          grid-template-rows: var(--altura-cabecera) 1fr;
        "
      >
        <AplicacionCabecera />
        <nuxt />
      </div>
    </a-spin>
  </div>
  <div v-else class="app--pagina">
    <PaginaCarga />
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import AplicacionCabecera from '@/components/compartido/AplicacionCabecera.vue';
import PaginaCarga from '@/components/visor/compartido/PaginaCarga.vue';
export default {
  components: { AplicacionCabecera, PaginaCarga },
  data() {
    return {
      configuracionAplicada: false,
    };
  },
  async fetch() {
    try {
      const { data: configuracionInicial } = await this.$axios.get(
        '/visor/iniciales/'
      );

      if (configuracionInicial) {
        this.configuracionAplicada = true;
        // Se establece la posicion inicial de la vista del mapa.
        this.establecerCentro([
          configuracionInicial.latitudInicial,
          configuracionInicial.longitudInicial,
        ]);
        this.establecerZoom(configuracionInicial.zoomInicial);
        // Se establece la informacion de las capas base.
        this.establecerCapasBase(configuracionInicial.capasBase);
        this.establecerCapaBaseActiva(configuracionInicial.capaBaseIncialId);
        // Se establece la informacion de las capas.
        this.establacerCapas(configuracionInicial.serviciosExternos);
        this.establecerCapasActivas(configuracionInicial.capasActivas);
        // Se establce la estructura de arbol de las capas.
        this.establecerCapasEstructura(configuracionInicial.estructura);
        this.establecerEstructuraObjetosGeograficos(
          configuracionInicial.estructuraObjetosGeograficos
        );
        this.establecerImagenesSatelitales([]);
      }
    } catch (error) {
      this.$manejarError(error);
    }
  },
  computed: {
    ...mapState(['estaCargando']),
  },
  mounted() {
    window.addEventListener('resize', () => {
      this.establecerEsMovil(window.innerWidth < 720);
      this.actualizarTamanioVentana(window.innerWidth);
    });
  },
  methods: {
    ...mapActions(['establecerEsMovil', 'actualizarTamanioVentana']),
    ...mapActions('visor', [
      'establecerCentro',
      'establecerZoom',
      'establecerCapasBase',
      'establecerCapaBaseActiva',
      'establacerCapas',
      'establecerCapasActivas',
      'establecerCapasEstructura',
      'establecerImagenesSatelitales',
      'establecerEstructuraObjetosGeograficos',
    ]),
  },
};
</script>
