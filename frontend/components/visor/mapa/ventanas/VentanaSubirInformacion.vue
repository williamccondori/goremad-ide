<template>
  <a-drawer
    :visible="estaAbiertoVentanaSubirInformacion"
    :width="tamanioVentana"
    @close="cerrarVentana('SubirInformacion')"
  >
    <span slot="title">
      <b>Subir información</b>
    </span>
    <a-space direction="vertical" style="width: 100%">
      <a-collapse v-model="collapseActivo">
        <a-collapse-panel key="formularioPanel" :header="tituloFormulario">
          <a-form-model ref="form" :model="form" @submit.prevent="subir()">
            <a-form-model-item
              label="Nombre"
              prop="nombre"
              :rules="{
                required: true,
                message: 'Ingrese el nombre',
              }"
            >
              <a-input v-model="form.nombre" placeholder="Ingrese el nombre" />
            </a-form-model-item>
            <a-form-model-item
              v-if="form.id === undefined"
              label="Archivo"
              prop="archivo"
              :rules="{
                required: form.id === undefined,
                message: 'Seleccione el archivo',
              }"
            >
              <a-upload-dragger
                :before-upload="validarArchivo"
                :file-list="listaArchivos"
                :multiple="false"
                :remove="eliminarArchivos"
              >
                <div>
                  <p class="ant-upload-drag-icon">
                    <a-icon type="inbox" />
                  </p>
                  <p class="ant-upload-text">
                    Haga clic o arrastre un archivo a esta área para cargarlo
                  </p>
                </div>
              </a-upload-dragger>
            </a-form-model-item>
            <a-button html-type="submit" type="primary">
              <a-icon type="save" /> Guardar
            </a-button>
            <a-button type="danger" @click="limpiar()">
              <a-icon type="redo" />
              Limpiar
            </a-button>
          </a-form-model>
        </a-collapse-panel>
      </a-collapse>
      <a-table
        bordered
        :columns="[
          {
            title: 'Nombre',
            dataIndex: 'nombre',
            key: 'nombre',
          },
          {
            title: 'Geometría',
            dataIndex: 'tipoGeometria',
            key: 'tipoGeometria',
          },
          {
            title: 'Registros',
            dataIndex: 'cantidadRegistros',
            key: 'cantidadRegistros',
          },
          {
            title: 'Acciones',
            key: 'acciones',
            scopedSlots: { customRender: 'acciones' },
          },
        ]"
        :data-source="cargas"
        row-key="id"
        size="small"
      >
        <div slot="acciones" slot-scope="text, record">
          <a-button type="dashed" @click="editar(record)">
            <a-icon type="edit" />
          </a-button>
          <a-button type="dashed" @click="eliminar(record)">
            <a-icon type="delete" />
          </a-button>
          <a-button type="dashed" @click="verGeometria(record)">
            <a-icon type="eye" />
          </a-button>
        </div>
      </a-table>
    </a-space>
  </a-drawer>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import { v4 as uuidv4 } from 'uuid';
export default {
  data() {
    return {
      collapseActivo: undefined,
      tituloFormulario: 'Subir información',
      form: {
        id: undefined,
        nombre: '',
        archivo: undefined,
      },
      cargas: [],
      listaArchivos: [],
    };
  },
  computed: {
    ...mapState(['tamanioVentana']),
    ...mapState('visor', ['estaAbiertoVentanaSubirInformacion']),
  },
  methods: {
    ...mapActions('visor', [
      'cerrarVentana',
      'agregarCapaEnMapa',
      'elimnarCapaEnMapa',
    ]),
    limpiar() {
      this.form = {
        id: undefined,
        nombre: '',
        archivo: undefined,
      };
      this.listaArchivos = [];
      this.collapseActivo = undefined;
      this.tituloFormulario = 'Subir información';
      this.$refs.form.resetFields();
    },
    validarArchivo(file) {
      const esTamanioValido = file.size / 1024 / 1024 < 5;
      const extensionesAceptadas = ['.zip', '.kml', '.kmz', '.geojson'];
      const fileExtension = '.' + file.name.split('.').pop().toLowerCase();

      if (!esTamanioValido) {
        this.$message.error('El archivo debe ser menor a 3MB');
        return false;
      }

      if (!extensionesAceptadas.includes(fileExtension)) {
        this.$message.error(
          'El archivo debe ser de tipo SHP (ZIP), KML, KMZ o GeoJSON'
        );
        return false;
      }

      this.form.archivo = file;
      this.listaArchivos = [file];

      return false;
    },
    eliminarArchivos() {
      this.form.archivo = undefined;
      this.listaArchivos = [];
    },
    async validarFormulario() {
      try {
        await this.$refs.form.validate();
        return true;
      } catch (error) {
        this.$message.error('Los campos ingresados son inválidos');
        return false;
      }
    },
    async subir() {
      const formularioValido = await this.validarFormulario();
      if (!formularioValido) return;
      try {
        this.$iniciarCarga();
        if (this.form.id) {
          const carga = this.cargas.find((c) => c.id === this.form.id);
          if (carga) {
            carga.nombre = this.form.nombre;
            this.cargas = [...this.cargas];
          }
        } else {
          const formData = new FormData();
          formData.append('archivo', this.form.archivo);
          const { data } = await this.$axios.post(
            '/visor/cargas/geometrias/',
            formData
          );
          this.cargas.push({
            id: uuidv4(),
            cantidadRegistros: data.cantidadRegistros,
            nombre: this.form.nombre,
            tipoGeometria: data.tipoGeometria,
            geojson: data.geojson,
          });
        }
        this.limpiar();
        this.$mostrarMensajeCorrecto();
      } catch (error) {
        this.$manejarError(error);
      } finally {
        this.$finalizarCarga();
      }
    },
    eliminar(record) {
      this.$confirm({
        title: '¿Está seguro de eliminar la carga?',
        content: 'Esta acción no se puede revertir',
        okText: 'Sí',
        okType: 'danger',
        cancelText: 'No',
        onOk: async () => {
          try {
            this.$iniciarCarga();
            this.cargas = this.cargas.filter((c) => c.id !== record.id);
            this.$mostrarMensajeCorrecto();
          } catch (error) {
            this.$manejarError(error);
          } finally {
            this.$finalizarCarga();
          }
        },
      });
    },
    editar(registro) {
      this.form = {
        id: registro.id,
        cantidadRegistros: registro.cantidadRegistros,
        nombre: registro.nombre,
        tipoGeometria: registro.tipoGeometria,
        geojson: registro.geojson,
      };
      this.tituloFormulario = 'Editar registro';
      this.collapseActivo = 'formularioPanel';
    },
    verGeometria(registro) {
      this.agregarCapaEnMapa({
        id: registro.id,
        esVectorial: true,
        wfs: {
          nombre: registro.nombre,
          geometria: JSON.parse(registro.geojson),
          estilo: {
            color: '#000000',
            fillColor: '#333333',
            fillOpacity: 0.5,
          },
          transparencia: 1,
        },
      });
    },
  },
};
</script>
