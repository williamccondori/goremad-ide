<template>
  <a-descriptions
    bordered
    :column="1"
    :title="servicioExterno.titulo"
    size="small"
  >
    <a-descriptions-item label="Título:">
      {{ servicioExterno.titulo }}
    </a-descriptions-item>
    <a-descriptions-item label="Nombre:">
      {{ servicioExterno.nombre }}
    </a-descriptions-item>
    <a-descriptions-item label="Versión:">
      {{ servicioExterno.version }}
    </a-descriptions-item>
    <a-descriptions-item label="Descripción:">
      {{ servicioExterno.descripcion }}
    </a-descriptions-item>
    <a-descriptions-item label="URL:">
      <span style="line-break: anywhere">
        {{ servicioExterno.url }}
      </span>
    </a-descriptions-item>
    <a-descriptions-item label="Palabras clave:">
      <a-tag
        v-for="palabraClave in servicioExterno.palabrasClave"
        :key="palabraClave"
        color="purple"
      >
        {{ palabraClave }}
      </a-tag>
    </a-descriptions-item>
    <a-descriptions-item label="Operaciones:">
      <div class="app--contenedor-vertical-pequenio" style="overflow: hidden">
        <div v-for="operacion in servicioExterno.operaciones" :key="operacion">
          <a-tag color="purple">
            {{ operacion }}
          </a-tag>
        </div>
      </div>
    </a-descriptions-item>
  </a-descriptions>
</template>

<script>
export default {
  props: {
    servicioExterno: {
      type: Object,
      required: true,
    },
  },
};
</script>
