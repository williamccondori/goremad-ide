<template>
    <div>
        <LWMSTileLayer
            v-for="element in elementosActivos"
            :key="element.id"
            :attribution="element.atribucion"
            :base-url="element.url"
            format="image/png"
            layer-type="layer"
            :layers="element.nombre"
            :name="element.titulo"
            :opacity="element.transparencia"
            :transparent="true"
            :visible="true"
            :z-index="1"
        />
    </div>
</template>

<script>
// noinspection NpmUsedModulesInstalled
import { mapState } from 'vuex';
import { LWMSTileLayer } from 'vue2-leaflet';

export default {
    components: {
        LWMSTileLayer,
    },
    computed: {
        ...mapState('visor', ['capas', 'capasActivas', 'capaSuperior']),
        elementosActivos() {
            return this.capas.filter((elemento) =>
                this.capasActivas.includes(elemento.id)
            );
        },
    },
    watch: {
        capaSuperior(valor) {
            this.$children.forEach((elemento) => {
                if (elemento.$vnode.key === valor) {
                    const capa = elemento.mapObject;
                    capa.bringToFront();
                }
            });
        },
    },
};
</script>
