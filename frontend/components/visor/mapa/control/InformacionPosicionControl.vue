<template>
    <LControl position="bottomright">
        <div v-if="informacionPosicion">
            <ATag class="informacion-posicion" color="green">
                <i class="bx bxs-map" />
                {{ informacionPosicion.latitud }},
                {{ informacionPosicion.longitud }}
            </ATag>
            <ATag class="informacion-posicion" color="green">
                <i class="bx bx-search" />
                {{ informacionPosicion.zoom }}
            </ATag>
        </div>
    </LControl>
</template>

<script>
import { Tag } from 'ant-design-vue';
import { mapState } from 'vuex';
import { LControl } from 'vue2-leaflet';
export default {
    components: {
        ATag: Tag,
        LControl,
    },
    computed: {
        ...mapState('visor', ['informacionPosicion']),
    },
};
</script>

<style scoped>
.informacion-posicion {
    border-radius: 0;
}
</style>
