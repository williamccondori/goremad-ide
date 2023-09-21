<template>
  <a-drawer
    :visible="estaAbiertoVentanaCapasOperables"
    :width="tamanioVentana"
    @close="cerrarVentana('CapasOperables')"
  >
    <span slot="title">
      <b>Capas</b>
    </span>
    <a-space direction="vertical" style="width: 100%">
      <a-collapse expand-icon-position="right">
        <a-collapse-panel
          v-for="catalogo in estructuraObjetosGeograficos"
          :key="catalogo.id"
          class="collapsePanelSinBordes"
        >
          <span slot="header">
            <b>{{ catalogo.nombre }}</b>
          </span>
          <a-collapse :bordered="false" expand-icon-position="right">
            <a-collapse-panel v-for="tema in catalogo.temas" :key="tema.id">
              <span slot="header">
                <b>{{ tema.nombre }}</b>
              </span>
              <div v-for="grupo in tema.grupos" :key="grupo.id">
                <p>
                  <b>{{ grupo.nombre }}</b>
                </p>
                <div v-for="objeto in grupo.objetos" :key="objeto.id">
                  <a-switch
                    size="small"
                    @change="(e) => cambiarEstadoVisualizacion(objeto.id, e)"
                  />
                  {{ objeto.nombre }}
                </div>
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
export default {
  computed: {
    ...mapState(['tamanioVentana']),
    ...mapState('visor', [
      'estaAbiertoVentanaCapasOperables',
      'estructuraObjetosGeograficos',
    ]),
  },
  methods: {
    ...mapActions('visor', [
      'cerrarVentana',
      'agregarCapaOperativa',
      'eliminarCapaOperativa',
    ]),
    async cambiarEstadoVisualizacion(objetoGeograficoId, estado) {
      try {
        this.$iniciarCarga();
        if (estado) {
          const { data } = await this.$axios.get(
            `/visor/objetos-geograficos/${objetoGeograficoId}/geometrias`
          );
          if (data) {
            this.agregarCapaOperativa({
              ...data,
              geometria: JSON.parse(data.geometria),
              estilo: JSON.parse(data.estilo),
            });
          }
        } else {
          this.eliminarCapaOperativa(objetoGeograficoId);
        }
      } catch (error) {
        this.$manejarError(error);
      } finally {
        this.$finalizarCarga();
      }
    },
  },
};
</script>
