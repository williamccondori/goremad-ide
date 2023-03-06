<template>
  <ADrawer
    :width="esMovil ? '100%' : 400"
    :visible="estaAbiertoImagenSatelitalCatalogoVentana"
    @close="cerrarImagenSatelitalCatalogoVentana()"
  >
    <span slot="title" style="text-transform: uppercase">
      <b>Imágenes satelitales</b>
    </span>
    <ASpace direction="vertical" class="app--w-100">
      <AButton
        block
        type="primary"
        icon="search"
        @click="abrirImagenSatelitalBuscadorFormularioVentana()"
      >
        Buscar imágenes satelitales
      </AButton>
      <AAlert
        show-icon
        message="Información"
        description="Para visualizar las imágenes satelitales disponibles habla clic en el botón (Buscar imágenes satelitales)."
      />
      <AList :data-source="imagenesSatelitales">
        <AListItem
          slot="renderItem"
          slot-scope="imagenSatelital"
          class="elemento-lista"
        >
          <ASpace direction="vertical" class="app--w-100">
            <AListItemMeta
              :title="imagenSatelital.identificador"
              :description="`Detalles: ${imagenSatelital.descripcion}`"
            >
              <AAvatar
                slot="avatar"
                shape="square"
                icon="picture"
                :style="{
                  backgroundColor: '#87d068',
                }"
              />
            </AListItemMeta>
            <ASpace class="app--w-100">
              <AButton
                size="small"
                :icon="obtenerTipoIcono(imagenSatelital.rgb)"
                :type="obtenerTipoBoton(imagenSatelital.rgb)"
                @click="mostrarImagenSatelital(imagenSatelital.rgb)"
              >
                RGB
              </AButton>
              <AButton
                size="small"
                :icon="obtenerTipoIcono(imagenSatelital.ndvi)"
                :type="obtenerTipoBoton(imagenSatelital.ndvi)"
                @click="mostrarImagenSatelital(imagenSatelital.ndvi)"
              >
                NDVI
              </AButton>
              <AButton
                size="small"
                :icon="obtenerTipoIcono(imagenSatelital.ndwi)"
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
import { Drawer, Button, Alert, List, Avatar, Space } from "ant-design-vue";
import { mapState, mapActions } from "vuex";
import ImagenSatelitalBuscadorFormulario from "@/components/visor/imagen-satelital/ImagenSatelitalBuscadorFormulario.vue";
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
    ...mapState(["esMovil"]),
    ...mapState("visor", [
      "estaAbiertoImagenSatelitalCatalogoVentana",
      "imagenesSatelitales",
      "capas",
      "capasActivas",
    ]),
  },
  methods: {
    ...mapActions("visor", [
      "cerrarImagenSatelitalCatalogoVentana",
      "abrirImagenSatelitalBuscadorFormularioVentana",
      "establecerCapasActivas",
    ]),
    mostrarImagenSatelital(imagenSatelitalId) {
      const existe = this.capasActivas.includes(imagenSatelitalId);
      if (existe) {
        this.establecerCapasActivas(
          this.capasActivas.filter((id) => id !== imagenSatelitalId)
        );
      } else {
        this.establecerCapasActivas([...this.capasActivas, imagenSatelitalId]);
      }
    },
    obtenerTipoIcono(imagenSatelitalId) {
      return this.capasActivas.includes(imagenSatelitalId)
        ? "eye"
        : "eye-invisible";
    },
    obtenerTipoBoton(imagenSatelitalId) {
      return this.capasActivas.includes(imagenSatelitalId)
        ? "dashed"
        : "danger";
    },
  },
};
</script>

<style>
.elemento-lista {
  overflow-wrap: anywhere;
}
</style>
