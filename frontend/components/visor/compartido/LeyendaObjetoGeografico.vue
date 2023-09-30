<template>
  <a-row align="middle" type="flex">
    <a-col :xs="3">
      <div
        v-if="estilo"
        :style="`width: 1.1rem;
                height: 1.1rem;
                border: ${estilo.weight}px ${estilo.color} solid;`"
      >
        <div
          :style="`width: 1rem;
                height: 1rem;
                background-color: ${estilo.fillColor};
                opacity: ${estilo.fillOpacity}`"
        />
      </div>
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
