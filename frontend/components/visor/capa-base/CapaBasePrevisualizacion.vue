<template>
    <a-card
        hoverable
        size="small"
        @click="establecerMapaBaseActiva(capaBase.id)"
    >
        <template #cover>
            <client-only>
                <LMap
                    :center="center"
                    :options="opciones"
                    style="height: 5rem"
                    :zoom="1"
                >
                    <LTileLayer :url="capaBase.url" />
                </LMap>
            </client-only>
        </template>
        <a-card-meta
            :description="capaBase.atribucion"
            :title="capaBase.nombre"
        />
    </a-card>
</template>

<script>
import { mapActions } from 'vuex';
import { LMap, LTileLayer } from 'vue2-leaflet';
export default {
    components: {
        LMap,
        LTileLayer,
    },
    props: {
        capaBase: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            center: [0, 0],
            opciones: {
                dragging: false,
                zoomControl: false,
                attributionControl: false,
                scrollWheelZoom: false,
            },
        };
    },
    methods: {
        ...mapActions('visor', ['establecerMapaBaseActiva']),
    },
};
</script>
