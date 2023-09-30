<template>
  <a-drawer
    :mask="esMovil"
    :visible="estaAbiertoVentanaInformacionCapaWfs"
    :width="tamanioVentana"
    @close="cerrarVentana('InformacionCapaWfs')"
  >
    <span slot="title">
      <b>Información de la capa</b>
    </span>
    <a-space direction="vertical" size="middle" style="width: 100%">
      <a-descriptions
        v-if="informacionCapaGeojson"
        :bordered="true"
        :column="1"
        size="small"
        :title="informacionCapaGeojson.nombre"
      >
        <a-descriptions-item
          v-if="informacionCapaGeojson.codigo"
          label="Código:"
        >
          <a-tag color="purple">
            {{ informacionCapaGeojson.codigo }}
          </a-tag>
        </a-descriptions-item>
        <a-descriptions-item label="Nombre:">
          {{ informacionCapaGeojson.nombre }}
        </a-descriptions-item>
        <a-descriptions-item
          v-if="informacionCapaGeojson.descripcion"
          label="Descripción:"
        >
          {{ informacionCapaGeojson.descripcion }}
        </a-descriptions-item>
        <a-descriptions-item label="Estilos:">
          <LeyendaObjetoGeografico
            :estilo="informacionCapaGeojson.estilo"
            :nombre="informacionCapaGeojson.nombre"
          />
        </a-descriptions-item>
      </a-descriptions>
      <a-descriptions
        v-if="informacionCapaGeojson"
        :bordered="true"
        :column="1"
        size="small"
        title="Propiedades"
      >
        <a-descriptions-item
          v-for="(value, key) in informacionCapaGeojson.propiedades"
          :key="key"
        >
          <small slot="label"> {{ key }}: </small>
          <small>
            {{ value }}
          </small>
        </a-descriptions-item>
      </a-descriptions>
      <a-alert
        v-else
        message="No hay información disponible, debe seleccionar una geometría"
        type="info"
      />
    </a-space>
  </a-drawer>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import LeyendaObjetoGeografico from '../compartido/LeyendaObjetoGeografico.vue';
export default {
  components: { LeyendaObjetoGeografico },
  computed: {
    ...mapState(['tamanioVentana', 'esMovil']),
    ...mapState('visor', [
      'estaAbiertoVentanaInformacionCapaWfs',
      'informacionCapaGeojson',
    ]),
  },
  methods: {
    ...mapActions('visor', ['cerrarVentana']),
  },
};
</script>
