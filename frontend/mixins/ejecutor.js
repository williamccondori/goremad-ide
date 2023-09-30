import { mapActions } from 'vuex';
import { notification } from 'ant-design-vue';
export default {
  methods: {
    ...mapActions(['establecerCargando']),
    $iniciarCarga() {
      this.establecerCargando(true);
    },
    $finalizarCarga() {
      this.establecerCargando(false);
    },
    $mostrarMensajeCorrecto(mensaje) {
      notification.success({
        message: 'Correcto',
        description: mensaje ?? 'El proceso se realizó correctamente',
      });
    },
    $mostrarMensajeAdvertencia(mensaje) {
      notification.warning({
        message: 'Advertencia',
        description: mensaje ?? 'El proceso se realizó con advertencias',
      });
    },
    $manejarError(error) {
      const contenido = error.response?.data;
      const codigoError = parseInt(error.response?.status ?? 500);
      if (codigoError === 500) {
        notification.error({
          message: 'Error',
          description: `Ocurrió un error inesperado: ${error}`,
        });
        return false;
      }
      const mensaje = this.obtenerMensajeError(contenido?.mensaje, codigoError);
      notification.error({
        message: `Error: ${codigoError}`,
        description: mensaje,
      });
    },
    obtenerMensajeError(mensaje, codigoError) {
      const errores = {
        400: 'Verifique los datos ingresados',
        401: 'Las credenciales proporcionadas no son válidas',
        404: 'El recurso solicitado no existe',
        422: 'Verifique los datos ingresados',
      };
      return mensaje ?? errores[codigoError] ?? 'Ocurrió un error inesperado';
    },
  },
};
