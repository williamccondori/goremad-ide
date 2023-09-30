<template>
  <ADrawer
    :visible="estaAbiertoImagenSatelitalCatalogoVentana"
    :width="esMovil ? '100%' : 400"
    @close="cerrarImagenSatelitalCatalogoVentana()"
  >
    <span slot="title" style="text-transform: uppercase">
      <b>Imágenes satelitales</b>
    </span>
    <ASpace class="app--w-100" direction="vertical">
      <AButton
        block
        icon="search"
        type="primary"
        @click="abrirImagenSatelitalBuscadorFormularioVentana()"
      >
        Buscar imágenes satelitales
      </AButton>
      <AAlert
        description="Para visualizar las imágenes satelitales disponibles habla clic en el botón (Buscar imágenes satelitales)."
        message="Información"
        show-icon
      />
      <AList :data-source="imagenesSatelitales">
        <AListItem
          slot="renderItem"
          slot-scope="imagenSatelital"
          class="elemento-lista"
        >
          <ASpace class="app--w-100" direction="vertical">
            <AListItemMeta
              :description="`Detalles: ${imagenSatelital.descripcion}`"
              :title="imagenSatelital.identificador"
            >
              <AAvatar
                slot="avatar"
                icon="picture"
                shape="square"
                :style="{
                  backgroundColor: '#87d068',
                }"
              />
            </AListItemMeta>
            <ASpace class="app--w-100">
              <AButton
                :icon="obtenerTipoIcono(imagenSatelital.rgb)"
                size="small"
                :type="obtenerTipoBoton(imagenSatelital.rgb)"
                @click="mostrarImagenSatelital(imagenSatelital.rgb)"
              >
                RGB
              </AButton>
              <AButton
                :icon="obtenerTipoIcono(imagenSatelital.ndvi)"
                size="small"
                :type="obtenerTipoBoton(imagenSatelital.ndvi)"
                @click="mostrarImagenSatelital(imagenSatelital.ndvi)"
              >
                NDVI
              </AButton>
              <AButton
                :icon="obtenerTipoIcono(imagenSatelital.ndwi)"
                size="small"
                :type="obtenerTipoBoton(imagenSatelital.ndwi)"
                @click="mostrarImagenSatelital(imagenSatelital.ndwi)"
              >
                NDWI
              </AButton>
            </ASpace>
          </ASpace>
        </AListItem>
      </AList>
    </ASpace>
    <ImagenSatelitalBuscadorFormulario />
  </ADrawer>
</template>

<script>
import { Drawer, Button, Alert, List, Avatar, Space } from 'ant-design-vue';
import { mapState, mapActions } from 'vuex';
import ImagenSatelitalBuscadorFormulario from '@/components/visor/imagen-satelital/ImagenSatelitalBuscadorFormulario.vue';
export default {
  components: {
    ADrawer: Drawer,
    AAlert: Alert,
    AButton: Button,
    AList: List,
    AListItem: List.Item,
    AListItemMeta: List.Item.Meta,
    AAvatar: Avatar,
    ASpace: Space,
    ImagenSatelitalBuscadorFormulario,
  },
  computed: {
    ...mapState(['esMovil']),
    ...mapState('visor', [
      'estaAbiertoImagenSatelitalCatalogoVentana',
      'imagenesSatelitales',
      'capas',
      'capasActivas',
    ]),
  },
  methods: {
    ...mapActions('visor', [
      'cerrarImagenSatelitalCatalogoVentana',
      'abrirImagenSatelitalBuscadorFormularioVentana',
      'establecerCapasWmsActivas',
    ]),
    mostrarImagenSatelital(imagenSatelitalId) {
      const existe = this.capasActivas.includes(imagenSatelitalId);
      if (existe) {
        this.establecerCapasWmsActivas(
          this.capasActivas.filter((id) => id !== imagenSatelitalId)
        );
      } else {
        this.establecerCapasWmsActivas([
          ...this.capasActivas,
          imagenSatelitalId,
        ]);
      }
    },
    obtenerTipoIcono(imagenSatelitalId) {
      return this.capasActivas.includes(imagenSatelitalId)
        ? 'eye-invisible'
        : 'eye';
    },
    obtenerTipoBoton(imagenSatelitalId) {
      return this.capasActivas.includes(imagenSatelitalId)
        ? 'danger'
        : 'dashed';
    },
  },
};
</script>

<style>
.elemento-lista {
  overflow-wrap: anywhere;
}
</style>
