<template>
  <ACard hoverable size="small" @click="establecerCapaBaseActiva(capaBase.id)">
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
    <ACardMeta :title="capaBase.nombre" :description="capaBase.atribucion" />
  </ACard>
</template>

<script>
import { Card } from "ant-design-vue";
import { mapActions } from "vuex";
import { LMap, LTileLayer } from "vue2-leaflet";
export default {
  components: {
    ACard: Card,
    ACardMeta: Card.Meta,
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
