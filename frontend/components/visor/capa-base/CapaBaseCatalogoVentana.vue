<template>
    <a-drawer
        :visible="estaAbiertoCapaBaseCatalogoVentana"
        :width="esMovil ? '100%' : 400"
        @close="cerrarCapaBaseCatalogoVentana()"
    >
        <span slot="title">
            <b>Mapas base</b>
        </span>
        <div class="app--contenedor-vertical">
            <a-row align="middle" justify="space-between" type="flex">
                <span>Todos los elementos:</span>
                <a-tag color="green">
                    {{ capasBase.length }}
                </a-tag>
            </a-row>
            <a-row :gutter="[16, 16]">
                <a-col
                    v-for="capaBase in capasBase"
                    :key="capaBase.id"
                    :span="12"
                >
                    <CapaBasePrevisualizacion :capa-base="capaBase" />
                </a-col>
            </a-row>
        </div>
    </a-drawer>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import CapaBasePrevisualizacion from '~/components/visor/capa-base/CapaBasePrevisualizacion.vue';
export default {
    components: {
        CapaBasePrevisualizacion,
    },
    computed: {
        ...mapState(['esMovil']),
        ...mapState('visor', [
            'estaAbiertoCapaBaseCatalogoVentana',
            'capasBase',
        ]),
    },
    methods: {
        ...mapActions('visor', ['cerrarCapaBaseCatalogoVentana']),
    },
};
</script>
