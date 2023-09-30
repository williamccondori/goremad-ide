<template>
  <a-drawer
    :visible="estaAbiertoVentanaInformacionCapasOperables"
    :width="tamanioVentana"
    @close="cerrarVentana('InformacionCapasOperables')"
  >
    <span slot="title">
      <b>Información de las capas</b>
    </span>
    <a-space direction="vertical" style="width: 100%">
      <div>
        <a-form-model
          ref="form"
          :model="form"
          @submit.prevent="consultarInformacionObjetoGeografico()"
        >
          <a-form-model-item
            label="Catálogo"
            prop="catalogoId"
            :rules="[{ required: true, message: 'Seleccione un catálogo' }]"
          >
            <a-select
              v-model="form.catalogoId"
              placeholder="Seleccione un catálogo"
              @change="
                form.temaId = undefined;
                form.grupoId = undefined;
                form.objetoGeograficoId = undefined;
              "
            >
              <a-select-option
                v-for="catalogo in catalogosDisponibles"
                :key="catalogo.id"
              >
                {{ catalogo.nombre }}
              </a-select-option>
            </a-select>
          </a-form-model-item>
          <a-form-model-item
            label="Tema"
            prop="temaId"
            :rules="[{ required: true, message: 'Seleccione un tema' }]"
          >
            <a-select
              v-model="form.temaId"
              placeholder="Seleccione una tema"
              @change="form.grupoId = undefined"
            >
              <a-select-option v-for="tema in temasDisponibles" :key="tema.id">
                {{ tema.nombre }}
              </a-select-option>
            </a-select>
          </a-form-model-item>
          <a-form-model-item
            label="Grupo"
            prop="grupoId"
            :rules="[{ required: true, message: 'Seleccione un grupo' }]"
          >
            <a-select
              v-model="form.grupoId"
              placeholder="Seleccione un grupo"
              @change="form.objetoGeograficoId = undefined"
            >
              <a-select-option
                v-for="grupo in gruposDisponibles"
                :key="grupo.id"
              >
                {{ grupo.nombre }}
              </a-select-option>
            </a-select>
          </a-form-model-item>
          <a-form-model-item
            label="Objeto geográfico"
            prop="objetoGeograficoId"
            :rules="[
              { required: true, message: 'Seleccione un objeto geográfico' },
            ]"
          >
            <a-select
              v-model="form.objetoGeograficoId"
              placeholder="Seleccione un objeto geográfico"
            >
              <a-select-option
                v-for="objetoGeografico in objetosGeograficosDisponibles"
                :key="objetoGeografico.id"
              >
                {{ objetoGeografico.nombre }}
              </a-select-option>
            </a-select>
          </a-form-model-item>
          <a-button block html-type="submit" type="primary">
            <a-icon type="search" />
            Consultar
          </a-button>
        </a-form-model>
      </div>
      <div v-if="informacionObjetoGeografico">
        <h1>
          <b>Resultados de la búsqueda:</b>
        </h1>
        <a-space direction="vertical" style="width: 100%">
          <a-button block type="primary" @click="verInformacion()">
            <a-icon type="eye" />
            Ver la información de los
            {{ informacionObjetoGeografico.total }} registros
          </a-button>
          <a-descriptions :bordered="true" :column="1" size="small">
            <a-descriptions-item label="Código:">
              <a-tag color="purple" style="font-size: x-small">
                {{ informacionObjetoGeografico.codigo }}
              </a-tag>
            </a-descriptions-item>
            <a-descriptions-item label="Título:">
              {{ informacionObjetoGeografico.nombre }}
            </a-descriptions-item>
            <a-descriptions-item label="Descripción:">
              {{ informacionObjetoGeografico.descripcion }}
            </a-descriptions-item>
            <a-descriptions-item label="Estilos:">
              <LeyendaObjetoGeografico
                :estilo="informacionObjetoGeografico.estilo"
                :nombre="informacionObjetoGeografico.nombre"
              />
            </a-descriptions-item>
          </a-descriptions>
        </a-space>
      </div>
    </a-space>
  </a-drawer>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import LeyendaObjetoGeografico from '../compartido/LeyendaObjetoGeografico.vue';
export default {
  components: { LeyendaObjetoGeografico },
  data() {
    return {
      form: {
        catalogoId: undefined,
        temaId: undefined,
        grupoId: undefined,
        objetoGeograficoId: undefined,
      },
      informacionObjetoGeografico: undefined,
    };
  },
  computed: {
    ...mapState(['tamanioVentana']),
    ...mapState('visor', [
      'estaAbiertoVentanaInformacionCapasOperables',
      'estructuraObjetosGeograficos',
    ]),
    catalogosDisponibles() {
      return this.estructuraObjetosGeograficos;
    },
    temasDisponibles() {
      return (
        this.catalogosDisponibles.find(
          (catalogo) => catalogo.id === this.form.catalogoId
        )?.temas ?? []
      );
    },
    gruposDisponibles() {
      return (
        this.temasDisponibles.find((tema) => tema.id === this.form.temaId)
          ?.grupos ?? []
      );
    },
    objetosGeograficosDisponibles() {
      return (
        this.gruposDisponibles.find((grupo) => grupo.id === this.form.grupoId)
          ?.objetos ?? []
      );
    },
  },
  methods: {
    ...mapActions('visor', [
      'cerrarVentana',
      'abrirVentana',
      'establecerInformacionObjetoGeografico',
    ]),
    async validarFormulario() {
      try {
        await this.$refs.form.validate();
        return true;
      } catch (error) {
        this.$message.error('Los campos ingresados son inválidos');
        return false;
      }
    },
    async consultarInformacionObjetoGeografico() {
      const formularioValido = await this.validarFormulario();
      if (!formularioValido) return;
      try {
        this.$iniciarCarga();
        const { data: informacionObjetoGeografico } = await this.$axios.get(
          `/visor/objetos-geograficos/${this.form.objetoGeograficoId}/informaciones/`
        );
        if (informacionObjetoGeografico) {
          this.informacionObjetoGeografico = {
            ...informacionObjetoGeografico,
            estilo: JSON.parse(informacionObjetoGeografico.estilo),
          };
        }
      } catch (error) {
        this.$manejarError(error);
      } finally {
        this.$finalizarCarga();
      }
    },
    verInformacion() {
      this.establecerInformacionObjetoGeografico(
        this.informacionObjetoGeografico
      );
      this.cerrarVentana('InformacionCapasOperables');
      this.abrirVentana('ResultadoInformacionCapasOperables');
    },
  },
};
</script>
