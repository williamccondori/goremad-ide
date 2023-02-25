<template>
  <BaseColapsable title="Información geográfica" icon="hdd">
    <a-button
      html-type="button"
      type="dashed"
      block
      @click="abrirInformacionCapaVentana()"
    >
      Información de las capas
    </a-button>
    <InformacionCapaVentana />
  </BaseColapsable>
</template>

<script>
import { mapActions } from "vuex";
import BaseColapsable from "@/components/visor/BaseColapsable.vue";
import InformacionCapaVentana from "@/components/visor/InformacionCapaVentana.vue";
export default {
  components: { BaseColapsable, InformacionCapaVentana },
  methods: {
    ...mapActions("visor", ["abrirInformacionCapaVentana"]),
  },
};
</script>
