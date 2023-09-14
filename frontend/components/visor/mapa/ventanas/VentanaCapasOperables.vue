<template>
  <a-drawer
    :visible="estaAbiertoVentanaCapasOperables"
    :width="tamanioVentana"
    @close="cerrarVentana('CapasOperables')"
  >
    <span slot="title">
      <b>CAPAS</b>
    </span>
    <a-space direction="vertical" style="width: 100%">
      <a-alert type="error">
        <span slot="message">
          <b>Funcionalidad en desarrollo</b>
        </span>
        <span slot="description">
          El comportamiento y la información mostrada por esta funcionalidad se
          encuentran en proceso de desarrollo/pruebas, por lo que pueden
          presentarse errores.
        </span>
      </a-alert>
      <a-collapse expand-icon-position="right">
        <a-collapse-panel key="1">
          <span slot="header"> <b>🌍 Fundamentales</b> </span>
        </a-collapse-panel>
        <a-collapse-panel key="2" class="collapsePanelSinBordes">
          <span slot="header"> <b>🌳 Gestión forestal</b> </span>
          <a-collapse :bordered="false" expand-icon-position="right">
            <a-collapse-panel key="2-1">
              <span slot="header">
                <b>📂 Modalidad de acceso</b>
              </span>
              <p><b>📄 Concesiones</b></p>
              <div>
                <a-switch
                  size="small"
                  @change="
                    (e) =>
                      cambiarEstadoVisualizacion('Con_ConcesionProForDifMad', e)
                  "
                />
                Concesión para productos forestales diferentes a la madera
              </div>
            </a-collapse-panel>
          </a-collapse>
        </a-collapse-panel>
      </a-collapse>
    </a-space>
  </a-drawer>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import { obtenerGeometria } from '@/repositorios/CapaGeograficaRepositorio';
export default {
  computed: {
    ...mapState(['tamanioVentana']),
    ...mapState('visor', ['estaAbiertoVentanaCapasOperables']),
  },
  methods: {
    ...mapActions('visor', [
      'cerrarVentana',
      'agregarCapaOperativa',
      'eliminarCapaOperativa',
    ]),
    async cambiarEstadoVisualizacion(nombreCapaOperativa, estado) {
      try {
        this.$iniciarCarga();
        if (estado) {
          const capaGeografica = await obtenerGeometria(nombreCapaOperativa);
          if (capaGeografica) {
            this.agregarCapaOperativa(capaGeografica);
          }
        } else {
          this.eliminarCapaOperativa(nombreCapaOperativa);
        }
      } catch (error) {
        this.$message.error(`Error inesperado: ${error}`);
      } finally {
        this.$finalizarCarga();
      }
    },
  },
};
</script>
