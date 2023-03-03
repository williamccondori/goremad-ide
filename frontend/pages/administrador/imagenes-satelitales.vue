<template>
  <AdministracionPagina titulo="Imágenes satelitales">
    <ASpace direction="vertical" class="app--w-100">
      <APopconfirm
        title="Este proceso puede tardar varios minutos y ralentizar el sistema, ¿Está de ejecutarlo ahora?"
        @confirm="programarDescarga()"
      >
        <AButton type="primary" icon="plus"> Programar descarga </AButton>
      </APopconfirm>
      <ImagenSatelitalCatalogo />
      <ImagenSatelitalResumenVentana />
    </ASpace>
  </AdministracionPagina>
</template>

<script>
import { Button, Space, Popconfirm } from "ant-design-vue";
import AdministracionPagina from "@/components/administrador/compartido/AdministracionPagina.vue";
import ImagenSatelitalCatalogo from "@/components/administrador/imagen-satelital/ImagenSatelitalCatalogo.vue";
import ImagenSatelitalResumenVentana from "@/components/administrador/imagen-satelital/ImagenSatelitalResumenVentana.vue";
export default {
  components: {
    AButton: Button,
    ASpace: Space,
    APopconfirm: Popconfirm,
    AdministracionPagina,
    ImagenSatelitalCatalogo,
    ImagenSatelitalResumenVentana,
  },
  layout: "administrador",
  methods: {
    async programarDescarga() {
      try {
        this.$iniciarCarga();
        await this.$axios.$post("/imagenes-satelitales/descargas/");
        this.$notification.success({
          message: "Correcto",
          description: "Se ha programado la descarga de imágenes satelitales",
        });
      } catch (error) {
        this.$manejarError(error);
      } finally {
        this.$finalizarCarga();
      }
    },
  },
};
</script>
