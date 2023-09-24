<template>
  <a-row align="middle" type="flex">
    <a-col :xs="3">
      <div
        v-if="estilo"
        :style="`width: 1rem; height: 1rem;
                border: ${estilo.weight}px ${estilo.color} solid;
                background-color: ${estilo.fillColor}
                background-transparency: ${estilo.fillOpacity}`"
      />
    </a-col>
    <a-col v-if="nombre" :xs="21">
      <small>
        <b>{{ nombre }}</b>
      </small>
    </a-col>
  </a-row>
</template>

<script>
export default {
  props: {
    estilo: {
      type: Object,
      required: true,
    },
    nombre: {
      type: String,
      required: false,
      default: undefined,
    },
  },
};
</script>
