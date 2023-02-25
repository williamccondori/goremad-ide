<template>
  <a-card hoverable size="small" @click="establecerCapaBaseActiva(capaBase.id)">
    <template #cover>
      <client-only>
        <LMap
          style="height: 5rem"
          :center="center"
          :zoom="1"
          :options="opciones"
        >
          <LTileLayer :url="capaBase.url" />
        </LMap>
      </client-only>
    </template>
    <a-card-meta :title="capaBase.nombre" :description="capaBase.atribucion" />
  </a-card>
</template>

<script>
import { mapActions } from "vuex";
import { LMap, LTileLayer } from "vue2-leaflet";
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
      },
    };
  },
  methods: {
    ...mapActions("visor", ["establecerCapaBaseActiva"]),
  },
};
</script>
