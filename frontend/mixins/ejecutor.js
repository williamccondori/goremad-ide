import { mapActions } from "vuex";
import { notification } from "ant-design-vue";

export default {
  methods: {
    ...mapActions(["establecerCargando"]),
    /**
     * Muestra el indicador de carga en la interfaz.
     */
    $iniciarCarga() {
      this.establecerCargando(true);
    },
    /**
     * Oculta el indicador de carga en la interfaz.
     */
    $finalizarCarga() {
      this.establecerCargando(false);
    },
    /**
     * Muestra un mensaje correcto en la interfaz.
     * @param {Sring} mensaje
     */
    $mostrarMensajeCorrecto(mensaje) {
      notification.success({
        message: "Correcto",
        description: mensaje ?? "El proceso se realizó correctamente",
      });
    },
    $mostrarMensajeAdvertencia(mensaje) {
      notification.warning({
        message: "Advertencia",
        description: mensaje ?? "El proceso se realizó con advertencias",
      });
    },
    /**
     * Maneja los errores de la aplicación y muestra un mensaje de error.
     * @param {Error} error
     */
    $manejarError(error) {
      const contenido = error.response?.data;
      const codigoError = parseInt(error.response?.status ?? 500);
      if (codigoError === 500) {
        throw contenido?.mensaje ?? error.message;
      }
      const mensaje = this.obtenerMensajeError(contenido?.mensaje, codigoError);
      notification.error({
        message: `Error: ${codigoError}`,
        description: mensaje,
      });
    },
    /**
     * Obtiene el mensaje de error a mostrar.
     * @param {String} mensaje
     * @param {Number} codigoError
     * @returns {String} Mensaje de error.
     */
    obtenerMensajeError(mensaje, codigoError) {
      const errores = {
        400: "Verifique los datos ingresados",
        401: "Las credenciales proporcionadas no son válidas",
        404: "El recurso solicitado no existe",
        422: "Verifique los datos ingresados",
      };
      return mensaje ?? errores[codigoError] ?? "Ocurrió un error inesperado";
    },
  },
};
