<template>
  <div>
    <LWMSTileLayer
      v-for="elemento in elementosActivos"
      :key="elemento.id"
      :attribution="elemento.atribucion"
      :base-url="elemento.url"
      :layers="elemento.nombre"
      :name="elemento.titulo"
      :opacity="elemento.transparencia"
      :transparent="true"
      :visible="true"
      :z-index="1"
      format="image/png"
      layer-type="layer"
    />
  </div>
</template>

<script>
import { mapState } from "vuex";
import { LWMSTileLayer } from "vue2-leaflet";
export default {
  components: {
    LWMSTileLayer,
  },
  computed: {
    ...mapState("visor", ["capas", "capasActivas", "capaSuperior"]),
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
