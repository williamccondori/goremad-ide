<script>
import L from 'leaflet';
import { findRealParent } from 'vue2-leaflet';
import 'leaflet.fullscreen';
import 'leaflet.fullscreen/Control.FullScreen.css';
export default {
  mounted() {
    this.$nextTick(() => {
      const mapa = findRealParent(this.$parent).mapObject;
      // Configuracion del control.
      mapa.addControl(
        L.control.fullscreen({
          title: 'Ir a pantalla completa',
          titleCancel: 'Salir de la pantalla completa',
          fullscreenElement:
            document.getElementsByClassName('pagina-principal')[0],
        })
      );
    });
  },
  render: () => ({}),
};
</script>
