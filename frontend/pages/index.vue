<template>
    <div style="height: 100vh">
        <div v-if="estaCargando || !configuracionAplicada" style="height: 100%">
            <PaginaCarga />
        </div>
        <div v-if="configuracionAplicada" style="height: 100%">
            <Cabecera />
            <div style="height: calc(100vh - 60px)">
                <ModalBienvenida />
                <Mapa />
            </div>
        </div>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import PaginaCarga from '../components/compartido/PaginaCarga.vue';
import Cabecera from '../components/compartido/Cabecera.vue';
import ModalBienvenida from '../components/visor/ModalBienvenida.vue';
import Mapa from '../components/visor/Mapa.vue';
export default {
    components: { PaginaCarga, Cabecera, ModalBienvenida, Mapa },
    auth: false,
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
                this.establecerCentro([
                    configuracionInicial.latitudInicial,
                    configuracionInicial.longitudInicial,
                ]);
                this.establecerZoom(configuracionInicial.zoomInicial);
                this.establecerMapasBase(configuracionInicial.capasBase);
                this.establecerMapaBaseActiva(
                    configuracionInicial.capaBaseIncialId
                );
                this.establacerCapasWms(configuracionInicial.serviciosExternos);
                this.establecerCapasWmsActivas(
                    configuracionInicial.capasActivas
                );
                this.establecerEstructuraObjetosGeograficos(
                    configuracionInicial.estructuraObjetosGeograficos
                );
                this.establecerInformacionObjetoGeografico(undefined);
                this.establecerEstructuraCapasInteroperables(
                    configuracionInicial.estructura
                );
                this.eliminarTodasCapasEnMapa();
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
            this.actualizarTamanioVentana(window.innerWidth);
        });
    },
    methods: {
        ...mapActions(['actualizarTamanioVentana']),
        ...mapActions('visor', [
            'establecerCentro',
            'establecerZoom',
            'establecerMapasBase',
            'establecerMapaBaseActiva',
            'establacerCapasWms',
            'establecerCapasWmsActivas',
            'establecerEstructuraObjetosGeograficos',
            'establecerInformacionObjetoGeografico',
            'establecerEstructuraCapasInteroperables',
            'eliminarTodasCapasEnMapa',
            'establecerImagenesSatelitales',
        ]),
    },
};
</script>
