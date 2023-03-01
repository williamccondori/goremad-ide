<template>
  <div>
    <a-tree
      :tree-data="estructuraGruposCapas"
      :replace-fields="{
        key: 'id',
        title: 'label',
      }"
      :selectable="false"
      :default-expand-all="true"
    >
      <template #title="{ id, label }">
        <a-dropdown :trigger="['contextmenu']">
          <span>{{ label }}</span>
          <template #overlay>
            <a-menu @click="({ key: menuId }) => seleccionar(id, menuId)">
              <a-menu-item key="crear">Crear</a-menu-item>
              <a-menu-item v-if="id !== 'root'" key="actualizar">
                Actualizar
              </a-menu-item>
              <a-menu-item v-if="id !== 'root'" key="eliminar">
                Eliminar
              </a-menu-item>
            </a-menu>
          </template>
        </a-dropdown>
      </template>
    </a-tree>
    <ADrawer
      :width="esMovil ? '100%' : 400"
      :mask-closable="false"
      :visible="estaAbiertoGrupoCapaFormularioVentana"
      @close="cerrarServicioExternoFormularioVentana()"
    >
      <span slot="title" style="text-transform: uppercase">
        <b>{{ titulo }}</b>
      </span>
      <a-form-model
        ref="referenciaFormulario"
        :model="formulario"
        @submit.prevent="guardar()"
      >
        <a-form-model-item prop="grupoCapaId" label="Grupo de capas:">
          <a-select
            v-model="formulario.grupoCapaId"
            :allow-clear="true"
            :disabled="!esEdicion"
            placeholder="Todos los elementos"
          >
            <a-select-option
              v-for="elemento in gruposCapas"
              :key="elemento.id"
              :value="elemento.id"
            >
              {{ elemento.nombre }}
            </a-select-option>
          </a-select>
        </a-form-model-item>
        <a-form-model-item
          prop="nombre"
          label="Nombre:"
          :rules="[
            {
              required: true,
              message: 'Ingrese el nombre de la capa base',
            },
          ]"
        >
          <a-input
            v-model="formulario.nombre"
            placeholder="Ingrese el nombre de la capa base"
          />
        </a-form-model-item>
        <a-form-model-item prop="estaHabilitado" label="¿Está habilitado?:">
          <a-checkbox v-model="formulario.estaHabilitado" />
        </a-form-model-item>
        <div>
          <a-button block html-type="submit" type="primary" icon="save">
            {{ titulo }}
          </a-button>
        </div>
      </a-form-model>
    </ADrawer>
  </div>
</template>

<script>
import { Drawer } from "ant-design-vue";
import { mapState, mapActions } from "vuex";

const formulario = {
  nombre: "",
  grupoCapaId: undefined,
  estaHabilitado: true,
};

export default {
  components: {
    ADrawer: Drawer,
  },
  data() {
    return {
      formulario: { ...formulario },
      esEdicion: false,
      grupoCapaId: undefined,
      estaAbiertoGrupoCapaFormularioVentana: false,
    };
  },
  async fetch() {
    try {
      this.$iniciarCarga();
      await this.obtenerGruposCapasEstructura();
      await this.obtenerGruposCapas();
    } catch (error) {
      this.$manejarError(error);
    } finally {
      this.$finalizarCarga();
    }
  },
  computed: {
    ...mapState(["esMovil"]),
    ...mapState("administrador", ["gruposCapas", "estructuraGruposCapas"]),
    titulo() {
      return this.esEdicion
        ? "Actualizar servicio externo"
        : "Crear grupo de capas";
    },
  },
  methods: {
    ...mapActions("administrador", [
      "obtenerGruposCapas",
      "obtenerGruposCapasEstructura",
    ]),
    async seleccionar(grupoCapaId, menuId) {
      switch (menuId) {
        case "crear":
          this.crear(grupoCapaId);
          break;
        case "actualizar":
          await this.actualizar(grupoCapaId);
          break;
        case "eliminar":
          await this.eliminar(grupoCapaId);
          break;
        default:
          break;
      }
    },
    crear(grupoCapaId) {
      this.formulario.grupoCapaId =
        grupoCapaId === "root" ? undefined : grupoCapaId;
      this.esEdicion = false;
      this.grupoCapaId = undefined;
      this.estaAbiertoGrupoCapaFormularioVentana = true;
    },
    async actualizar(grupoCapaId) {
      try {
        this.$iniciarCarga();
        const { data } = await this.$axios.get(`/grupos-capas/${grupoCapaId}/`);
        this.formulario = { ...data };
        if (data.grupoCapaId === null) {
          this.formulario.grupoCapaId = undefined;
        }
        this.esEdicion = true;
        this.grupoCapaId = grupoCapaId;
        this.estaAbiertoGrupoCapaFormularioVentana = true;
      } catch (error) {
        this.$manejarError(error);
      } finally {
        this.$finalizarCarga();
      }
    },
    async eliminar(grupoCapaId) {
      try {
        this.$iniciarCarga();
        await this.$axios.delete(`/grupos-capas/${grupoCapaId}/`);
        await this.obtenerGruposCapasEstructura();
        await this.obtenerGruposCapas();
        this.$mostrarMensajeCorrecto();
      } catch (error) {
        this.$manejarError(error);
      } finally {
        this.$finalizarCarga();
      }
    },
    guardar() {
      this.$refs.referenciaFormulario?.validate(async (valid) => {
        if (valid) {
          try {
            this.$iniciarCarga();
            this.formulario.grupoCapaId =
              this.formulario.grupoCapaId === "root"
                ? undefined
                : this.formulario.grupoCapaId;

            if (this.esEdicion) {
              await this.$axios.put(`/grupos-capas/${this.grupoCapaId}/`, {
                ...this.formulario,
              });
            } else {
              await this.$axios.post("/grupos-capas/", { ...this.formulario });
            }
            await this.obtenerGruposCapasEstructura();
            await this.obtenerGruposCapas();
            this.cerrarServicioExternoFormularioVentana();
            this.$mostrarMensajeCorrecto();
          } catch (error) {
            this.$manejarError(error);
          } finally {
            this.$finalizarCarga();
          }
        }
      });
    },
    cerrarServicioExternoFormularioVentana() {
      this.formulario = { ...formulario };
      this.$refs.referenciaFormulario?.resetFields();
      this.estaAbiertoGrupoCapaFormularioVentana = false;
    },
  },
};
</script>
