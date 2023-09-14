<template>
  <a-drawer
    :visible="estaAbiertoVentanaInformacionCapasOperables"
    :width="tamanioVentana"
    @close="cerrarVentana('InformacionCapasOperables')"
  >
    <span slot="title">
      <b>INFORMACIÓN DE LAS CAPAS</b>
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
      <div>
        <h1>
          <b>Formulario:</b>
        </h1>
        <a-form-model
          ref="formModel"
          :model="form"
          :rules="rules"
          @submit.prevent="consultarCapaGeografica()"
        >
          <a-form-model-item label="Temática" prop="tematica">
            <a-select
              v-model="form.tematica"
              placeholder="Seleccione una temática"
              @change="form.capaGeografica = undefined"
            >
              <a-select-option v-for="tematica in tematicas" :key="tematica.id">
                {{ tematica.nombre }}
              </a-select-option>
            </a-select>
          </a-form-model-item>
          <a-form-model-item label="Capa geográfica" prop="capaGeografica">
            <a-select
              v-model="form.capaGeografica"
              placeholder="Seleccione una capa geográfica"
            >
              <a-select-opt-group
                v-for="grupo in gruposDisponibles"
                :key="grupo.id"
                :label="grupo.nombre"
              >
                <a-select-option
                  v-for="capaGeografica in grupo.capasGeograficas"
                  :key="capaGeografica.id"
                >
                  {{ capaGeografica.nombre }}
                </a-select-option>
              </a-select-opt-group>
            </a-select>
          </a-form-model-item>
          <a-button block html-type="submit" type="primary">
            <a-icon type="search" />
            Consultar
          </a-button>
        </a-form-model>
      </div>
      <div v-if="capaGeograficaResultado">
        <h1>
          <b>Resultados de la búsqueda:</b>
        </h1>
        <a-space direction="vertical" style="width: 100%">
          <a-button block type="primary" @click="verInformacion()">
            <a-icon type="eye" />
            Ver la información de los
            {{ capaGeograficaResultado.total }} registros
          </a-button>
          <a-descriptions :bordered="true" :column="1" size="small">
            <a-descriptions-item label="Título">
              {{ capaGeograficaResultado.titulo }}
            </a-descriptions-item>
            <a-descriptions-item label="Nombre de la capa">
              {{ capaGeograficaResultado.nombre }}
            </a-descriptions-item>
            <a-descriptions-item label="Descripción">
              {{ capaGeograficaResultado.descripcion }}
            </a-descriptions-item>
            <a-descriptions-item label="Estilos">
              <div style="margin-bottom: 0.25rem">
                {{ capaGeograficaResultado.titulo }}
              </div>
              <div
                v-if="capaGeograficaResultado.tipoEstilo === 'poligono'"
                :style="`width: 1rem; height: 1rem;
                border: ${capaGeograficaResultado.estilos.weight}px ${capaGeograficaResultado.estilos.color} solid;
                background-color: ${capaGeograficaResultado.estilos.fillColor}
                background-transparency: ${capaGeograficaResultado.estilos.fillOpacity}`"
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
import { obtenerInformacionCapaGeografica } from '@/repositorios/CapaGeograficaRepositorio';
export default {
  data() {
    return {
      capaGeograficaResultado: undefined,
      form: {
        tematica: undefined,
        capaGeografica: undefined,
      },
      rules: {
        tematica: [{ required: true, message: 'Seleccione una temática' }],
        capaGeografica: [
          { required: true, message: 'Please select an option' },
        ],
      },
      tematicas: [
        {
          id: 'fundamental',
          nombre: 'Fundamentales',
          grupos: [],
        },
        {
          id: 'gestionForestal',
          nombre: 'Gestión forestal',
          grupos: [
            {
              id: 'autorizaciones',
              nombre: 'Modalidad de acceso / Autorizaciones',
              capasGeograficas: [
                {
                  id: 'Act_AutorizacionDes',
                  nombre: 'Autorización de desbosque',
                },
                {
                  id: 'Act_AutorizacionCamUsoActTieFinAgrPrePri',
                  nombre:
                    'Autorización de cambio de uso actual de las tierras a fines agropecuarios en predios privados',
                },
              ],
            },
            {
              id: 'concesion',
              nombre: 'Modalidad de acceso / Concesiones',
              capasGeograficas: [
                {
                  id: 'Con_ConcesionProForDifMad',
                  nombre:
                    'Concesión para productos forestales diferentes a la madera',
                },
                {
                  id: 'Con_ConcesionForFinMad',
                  nombre: 'Concesión forestal con fines maderables',
                },
                {
                  id: 'Con_ConcesionForRef',
                  nombre: 'Concesión para forestación y/o reforestación',
                },
              ],
            },
          ],
        },
      ],
    };
  },
  computed: {
    ...mapState(['tamanioVentana']),
    ...mapState('visor', ['estaAbiertoVentanaInformacionCapasOperables']),
    gruposDisponibles() {
      return (
        this.tematicas.find((tematica) => tematica.id === this.form.tematica)
          ?.grupos ?? []
      );
    },
  },
  methods: {
    ...mapActions('visor', [
      'cerrarVentana',
      'establecerInformacionCapaOperativa',
      'abrirVentana',
    ]),
    async validarFormulario() {
      try {
        await this.$refs.formModel.validate();
        return true;
      } catch (error) {
        this.$message.error('Los campos ingresados son inválidos');
        return false;
      }
    },
    async consultarCapaGeografica() {
      try {
        this.$iniciarCarga();
        this.capaGeografica = undefined;
        const formularioValido = await this.validarFormulario();
        if (!formularioValido) {
          return;
        }
        const informacionCapaGeografica =
          await obtenerInformacionCapaGeografica(this.form.capaGeografica);
        if (informacionCapaGeografica) {
          this.capaGeograficaResultado = {
            ...informacionCapaGeografica,
            columnas: undefined,
            registros: undefined,
          };
          this.establecerInformacionCapaOperativa(informacionCapaGeografica);
        }
      } catch (error) {
        this.$message.error(`Error inesperado: ${error}`);
      } finally {
        this.$finalizarCarga();
      }
    },
    verInformacion() {
      this.cerrarVentana('InformacionCapasOperables');
      this.abrirVentana('ResultadoInformacionCapasOperables');
    },
  },
};
</script>
