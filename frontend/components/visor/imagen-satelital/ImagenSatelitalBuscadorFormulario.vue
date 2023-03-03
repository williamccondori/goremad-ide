<template>
  <ADrawer
    :width="esMovil ? '100%' : 400"
    :visible="estaAbiertoImagenSatelitalBuscadorFormularioVentana"
    @close="cerrarImagenSatelitalBuscadorFormularioVentana()"
  >
    <span slot="title" style="text-transform: uppercase">
      <b>Buscar imágenes satelitales</b>
    </span>
    <div class="app--contenedor-vertical">
      <AAlert show-icon message="Información">
        <span slot="description">
          Disponibles imágenes SENTINEL-2 MSI - Level-1A (10m) en sus
          composiciones: <ATag color="blue">RGB</ATag>
          <ATag color="blue">NDVI</ATag> <ATag color="blue">NDWI</ATag>.
        </span>
      </AAlert>
    </div>
  </ADrawer>
</template>

<script>
import { Drawer, Alert, Tag } from "ant-design-vue";
import { mapState, mapActions } from "vuex";
export default {
  components: {
    ADrawer: Drawer,
    AAlert: Alert,
    ATag: Tag,
  },
  computed: {
    ...mapState(["esMovil"]),
    ...mapState("visor", [
      "estaAbiertoImagenSatelitalBuscadorFormularioVentana",
    ]),
  },
  methods: {
    ...mapActions("visor", ["cerrarImagenSatelitalBuscadorFormularioVentana"]),
  },
};
</script>
