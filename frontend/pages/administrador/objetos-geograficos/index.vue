<template>
  <AdministracionPagina titulo="Objetos geográficos">
    <a-space direction="vertical" style="width: 100%">
      <a-row :gutter="[8, 8]">
        <a-col :lg="6" :md="8" :sm="12" :xs="24">
          <a-card size="small">
            <NuxtLink to="/administrador/objetos-geograficos/catalogos">
              <a-icon type="link" /> Catálogos
            </NuxtLink>
          </a-card>
        </a-col>
        <a-col :lg="6" :md="8" :sm="12" :xs="24">
          <a-card size="small">
            <NuxtLink to="/administrador/objetos-geograficos/temas">
              <a-icon type="link" /> Temas
            </NuxtLink>
          </a-card>
        </a-col>
        <a-col :lg="6" :md="8" :sm="12" :xs="24">
          <a-card size="small">
            <NuxtLink to="/administrador/objetos-geograficos/grupos">
              <a-icon type="link" /> Grupos
            </NuxtLink>
          </a-card>
        </a-col>
      </a-row>
      <a-collapse v-model="collapseActivo">
        <a-collapse-panel key="formularioPanel" :header="tituloFormulario">
          <a-form-model ref="form" :model="form" @submit.prevent="guardar()">
            <a-row :gutter="[8, 8]">
              <a-col :lg="6" :md="12" :sm="12" :xs="24">
                <a-form-model-item
                  label="Grupo"
                  prop="grupoId"
                  :rules="{
                    required: true,
                    message: 'Seleccione el grupo',
                  }"
                >
                  <a-select
                    v-model="form.grupoId"
                    placeholder="Seleccione el grupo"
                  >
                    <a-select-option v-for="grupo in grupos" :key="grupo.id">
                      {{ grupo.nombre }}
                    </a-select-option>
                  </a-select>
                </a-form-model-item>
              </a-col>
              <a-col :lg="6" :md="12" :sm="12" :xs="24">
                <a-form-model-item
                  label="Código"
                  prop="codigo"
                  :rules="{
                    required: true,
                    message: 'Ingrese el código',
                  }"
                >
                  <a-input
                    v-model="form.codigo"
                    placeholder="Ingrese el código"
                  />
                </a-form-model-item>
              </a-col>
              <a-col :lg="6" :md="12" :sm="12" :xs="24">
                <a-form-model-item
                  label="Nombre"
                  prop="nombre"
                  :rules="{
                    required: true,
                    message: 'Ingrese el nombre',
                  }"
                >
                  <a-input
                    v-model="form.nombre"
                    placeholder="Ingrese el nombre"
                  />
                </a-form-model-item>
              </a-col>
              <a-col :lg="6" :md="12" :sm="12" :xs="24">
                <a-form-model-item
                  label="Base de datos"
                  prop="nombreBaseDatos"
                  :rules="{
                    required: true,
                    message: 'Ingrese la tabla',
                  }"
                >
                  <a-input
                    v-model="form.nombreBaseDatos"
                    placeholder="Ingrese la base de datos"
                  />
                </a-form-model-item>
              </a-col>
              <a-col :lg="6" :md="12" :sm="12" :xs="24">
                <a-form-model-item
                  label="Esquema"
                  prop="nombreEsquema"
                  :rules="{
                    required: true,
                    message: 'Ingrese el esquema',
                  }"
                >
                  <a-input
                    v-model="form.nombreEsquema"
                    placeholder="Ingrese el esquema"
                  />
                </a-form-model-item>
              </a-col>
              <a-col :lg="6" :md="12" :sm="12" :xs="24">
                <a-form-model-item
                  label="Tabla"
                  prop="nombreTabla"
                  :rules="{
                    required: true,
                    message: 'Ingrese la tabla',
                  }"
                >
                  <a-input
                    v-model="form.nombreTabla"
                    placeholder="Ingrese la tabla"
                  />
                </a-form-model-item>
              </a-col>
              <a-col :lg="6" :md="12" :sm="12" :xs="24">
                <a-form-model-item
                  label="¿Está habilitado?"
                  prop="estaHabilitado"
                >
                  <a-switch v-model="form.estaHabilitado" />
                </a-form-model-item>
              </a-col>
              <a-col :lg="24" :md="24" :sm="24" :xs="24">
                <a-form-model-item label="Descripción" prop="descripcion">
                  <a-input
                    v-model="form.descripcion"
                    placeholder="Ingrese la descripción"
                    type="textarea"
                  />
                </a-form-model-item>
              </a-col>
              <a-col :lg="24" :md="24" :sm="24" :xs="24">
                <a-form-model-item label="Estilo" prop="estilo">
                  <EditorEstilo v-model="form.estilo" />
                </a-form-model-item>
              </a-col>
            </a-row>
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
            title: 'Código',
            dataIndex: 'codigo',
            key: 'codigo',
            scopedSlots: { customRender: 'codigo' },
          },
          {
            title: 'Grupo',
            dataIndex: 'grupoNombre',
            key: 'grupoNombre',
          },
          {
            title: 'Nombre',
            dataIndex: 'nombre',
            key: 'nombre',
          },
          {
            title: 'Acciones',
            key: 'acciones',
            scopedSlots: { customRender: 'acciones' },
          },
        ]"
        :data-source="objetosGeograficos"
        row-key="id"
        size="small"
      >
        <div slot="codigo" slot-scope="text">
          <a-tag color="purple">{{ text }}</a-tag>
        </div>
        <div slot="acciones" slot-scope="text, record">
          <a-button type="dashed" @click="editar(record)">
            <a-icon type="edit" />
          </a-button>
          <a-button type="dashed" @click="eliminar(record)">
            <a-icon type="delete" />
          </a-button>
        </div>
      </a-table>
    </a-space>
  </AdministracionPagina>
</template>

<script>
import AdministracionPagina from '@/components/administrador/compartido/AdministracionPagina.vue';
import EditorEstilo from '~/components/compartido/EditorEstilo.vue';
export default {
  components: {
    AdministracionPagina,
    EditorEstilo,
  },
  layout: 'administrador',
  data() {
    return {
      collapseActivo: undefined,
      tituloFormulario: 'Agregar registro',
      form: {
        id: undefined,
        codigo: '',
        nombre: '',
        nombreBaseDatos: 'CatalogoObjetosGestionForestalDistribucion',
        nombreEsquema: 'public',
        nombreTabla: '',
        descripcion: '',
        estilo: '',
        estaHabilitado: true,
        grupoId: undefined,
      },
      grupos: [],
      objetosGeograficos: [],
    };
  },
  async fetch() {
    await this.obtenerObjetosGeograficos();
    await this.obtenerGrupos();
  },
  methods: {
    async obtenerObjetosGeograficos() {
      try {
        this.$iniciarCarga();
        const { data } = await this.$axios.get('/objetos-geograficos/');
        this.objetosGeograficos = data;
      } catch (error) {
        this.$manejarError(error);
      } finally {
        this.$finalizarCarga();
      }
    },
    async obtenerGrupos() {
      try {
        this.$iniciarCarga();
        const { data } = await this.$axios.get('/grupos/');
        this.grupos = data;
      } catch (error) {
        this.$manejarError(error);
      } finally {
        this.$finalizarCarga();
      }
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
    async guardar() {
      const formularioValido = await this.validarFormulario();
      if (!formularioValido) return;
      try {
        this.$iniciarCarga();
        if (this.form.id) {
          await this.$axios.put(
            `/objetos-geograficos/${this.form.id}/`,
            this.form
          );
        } else {
          await this.$axios.post('/objetos-geograficos/', this.form);
        }
        await this.obtenerObjetosGeograficos();
        this.limpiar();
        this.$mostrarMensajeCorrecto();
      } catch (error) {
        this.$manejarError(error);
      } finally {
        this.$finalizarCarga();
      }
    },
    editar(record) {
      this.form = {
        id: record.id,
        codigo: record.codigo,
        nombre: record.nombre,
        nombreBaseDatos: record.nombreBaseDatos,
        nombreEsquema: record.nombreEsquema,
        nombreTabla: record.nombreTabla,
        descripcion: record.descripcion,
        estilo: record.estilo,
        estaHabilitado: record.estaHabilitado,
        grupoId: record.grupoId,
      };
      this.tituloFormulario = 'Editar registro';
      this.collapseActivo = 'formularioPanel';
    },
    eliminar(record) {
      this.$confirm({
        title: '¿Está seguro de eliminar el objeto geográfico?',
        content: 'Esta acción no se puede revertir',
        okText: 'Sí',
        okType: 'danger',
        cancelText: 'No',
        onOk: async () => {
          try {
            this.$iniciarCarga();
            await this.$axios.delete(`/objetos-geograficos/${record.id}/`);
            await this.obtenerObjetosGeograficos();
            this.$mostrarMensajeCorrecto();
          } catch (error) {
            this.$manejarError(error);
          } finally {
            this.$finalizarCarga();
          }
        },
      });
    },
    limpiar() {
      this.form = {
        id: undefined,
        codigo: '',
        nombre: '',
        nombreBaseDatos: 'CatalogoObjetosGestionForestalDistribucion',
        nombreEsquema: 'public',
        nombreTabla: '',
        descripcion: '',
        estilo: '',
        estaHabilitado: true,
        grupoId: undefined,
      };
      this.collapseActivo = undefined;
      this.tituloFormulario = 'Agregar registro';
      this.$refs.form.resetFields();
    },
  },
};
</script>
