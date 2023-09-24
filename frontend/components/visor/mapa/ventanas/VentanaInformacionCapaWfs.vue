<template>
  <a-drawer
    :mask="false"
    :visible="estaAbiertoVentanaInformacionCapaWfs"
    :width="tamanioVentana"
    @close="cerrarVentana('InformacionCapaWfs')"
  >
    <span slot="title">
      <b>Información de la capa</b>
    </span>
    <a-space direction="vertical" size="middle" style="width: 100%">
      <a-descriptions
        v-if="informacionCapaWfs"
        :bordered="true"
        :column="1"
        size="small"
        :title="informacionCapaWfs.nombre"
      >
        <a-descriptions-item label="Nombre:">
          {{ informacionCapaWfs.nombre }}
        </a-descriptions-item>
      </a-descriptions>
      <a-descriptions
        v-if="informacionCapaWfs"
        :bordered="true"
        :column="1"
        size="small"
        title="Propiedades"
      >
        <a-descriptions-item
          v-for="(value, key) in informacionCapaWfs.propiedades"
          :key="key"
        >
          <small slot="label"> {{ key }}: </small>
          <small>
            {{ value }}
          </small>
        </a-descriptions-item>
      </a-descriptions>
    </a-space>
  </a-drawer>
</template>

<script>
import { mapState, mapActions } from 'vuex';
export default {
  computed: {
    ...mapState(['tamanioVentana']),
    ...mapState('visor', [
      'estaAbiertoVentanaInformacionCapaWfs',
      'informacionCapaWfs',
    ]),
  },
  methods: {
    ...mapActions('visor', ['cerrarVentana']),
  },
};
</script>
