<template>
  <div>
    <LWMSTileLayer
      v-for="elemento in elementosActivos"
      :key="elemento.id"
      :attribution="elemento.atribucion"
      :base-url="elemento.url"
      :layers="elemento.capa"
      :name="elemento.titulo"
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
  props: {
    configuracionInicial: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      map: undefined,
    };
  },
  computed: {
    ...mapState("visor", ["capasActivas"]),
    elementosActivos() {
      return this.configuracionInicial.serviciosExternos.filter((elemento) =>
        this.capasActivas.includes(elemento.id)
      );
    },
  },
};
</script>
