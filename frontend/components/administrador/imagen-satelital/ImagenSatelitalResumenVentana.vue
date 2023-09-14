<template>
  <ADrawer
    :mask-closable="false"
    :visible="estaAbiertoImagenSatelitalResumenVentana"
    :width="esMovil ? '100%' : 400"
    @close="cerrarImagenSatelitalResumenVentana()"
  >
    <span slot="title" style="text-transform: uppercase">
      <b> Detalles de la imagen satelital</b>
    </span>
    <ASpace v-if="imagenSatelital" class="app--w-100" direction="vertical">
      <ACard hoverable>
        <img
          slot="cover"
          alt="Imagen satelital"
          :src="imagenSatelital.imagenUrl"
        />
        <ACardMeta :title="imagenSatelital.identificador">
          <template slot="description">
            {{ imagenSatelital.descripcion }}
          </template>
        </ACardMeta>
      </ACard>
      <ADivider />
      <ADescriptions
        bordered
        :column="1"
        layout="vertical"
        size="small"
        title="Información general:"
      >
        <ADescriptionsItem label="Identificador:" style="word-wrap: break-word">
          {{ imagenSatelital.identificador }}
        </ADescriptionsItem>
        <ADescriptionsItem label="Identificador (Sentinel-Hub):">
          <ATag color="green">
            {{ imagenSatelital.identificadorSentinelHub }}
          </ATag>
        </ADescriptionsItem>
        <ADescriptionsItem label="Cobertura de nubosidad:">
          {{ imagenSatelital.coberturanubosidad }} (%)
        </ADescriptionsItem>
        <ADescriptionsItem label="Cobertura de vegetación:">
          {{ imagenSatelital.coberturavegetacion }} (%)
        </ADescriptionsItem>
        <ADescriptionsItem label="Cobertura de agua:">
          {{ imagenSatelital.coberturaagua }} (%)
        </ADescriptionsItem>
        <ADescriptionsItem label="Fecha y hora de descarga:">
          {{ imagenSatelital.fecha }}
        </ADescriptionsItem>
        <ADescriptionsItem label="Tamaño:">
          {{ imagenSatelital.tamanio }}
        </ADescriptionsItem>
        <ADescriptionsItem label="Variaciones:">
          <ASpace>
            <ATag color="purple"> RGB </ATag>
            <ATag color="purple"> NDVI </ATag>
            <ATag color="purple"> NDWI </ATag>
          </ASpace>
        </ADescriptionsItem>
      </ADescriptions>
      <ADescriptions
        bordered
        :column="1"
        layout="vertical"
        size="small"
        title="Metadatos:"
      >
        <ADescriptionsItem
          v-for="(value, key) in imagenSatelital.metadatos"
          :key="key"
          :label="key.toUpperCase() + ':'"
        >
          {{ value }}
        </ADescriptionsItem>
      </ADescriptions>
    </ASpace>
  </ADrawer>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import {
  Drawer,
  Card,
  Space,
  Descriptions,
  Tag,
  Divider,
} from 'ant-design-vue';
export default {
  components: {
    ADrawer: Drawer,
    ACard: Card,
    ACardMeta: Card.Meta,
    ASpace: Space,
    ADescriptions: Descriptions,
    ADescriptionsItem: Descriptions.Item,
    ATag: Tag,
    ADivider: Divider,
  },
  computed: {
    ...mapState(['esMovil']),
    ...mapState('administrador', [
      'estaAbiertoImagenSatelitalResumenVentana',
      'imagenSatelital',
    ]),
  },
  methods: {
    ...mapActions('administrador', ['cerrarImagenSatelitalResumenVentana']),
  },
};
</script>
