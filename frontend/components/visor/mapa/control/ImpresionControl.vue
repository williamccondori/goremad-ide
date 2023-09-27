<template>
  <LControl
    style="
      background-color: rgba(255, 255, 255, 0.55);
      border-radius: 0.25rem;
      padding: 0.25rem;
    "
  >
    <a-tooltip placement="left" title="Imprimir">
      <a-button shape="circle" type="primary" @click="abrirVentanaImpresion()">
        <i class="bx bx-printer" />
      </a-button>
    </a-tooltip>
    <a-drawer
      :visible="ventanaImpresionAbierto"
      :width="tamanioVentana"
      @close="cerrarVentanaImpresion()"
    >
      <span slot="title">
        <b>Imprimir</b>
      </span>
      <a-space direction="vertical" style="width: 100%">
        <a-form-model ref="form" :model="form" @submit.prevent="imprimirMapa()">
          <a-form-model-item
            label="Titulo:"
            prop="titulo"
            :rules="{
              required: true,
              message: 'Ingrese el título',
            }"
          >
            <a-input v-model="form.titulo" placeholder="Ingrese el título" />
          </a-form-model-item>
          <a-form-model-item>
            <a-select
              v-model="form.disposicion"
              placeholder="Seleccione una disposición"
            >
              <a-select-option value="CurrentSize">
                Tamaño actual
              </a-select-option>
              <a-select-option value="A4Portrait">
                Tamaño A4 vertical
              </a-select-option>
              <a-select-option value="A4Landscape">
                Tamaño A4 horizontal
              </a-select-option>
            </a-select>
          </a-form-model-item>
          <a-button block html-type="submit" type="primary">
            <a-icon type="printer" /> Imprimir
          </a-button>
        </a-form-model>
      </a-space>
    </a-drawer>
  </LControl>
</template>
<script>
import L from 'leaflet';
import { findRealParent, LControl } from 'vue2-leaflet';
import { mapState } from 'vuex';
import 'leaflet-easyprint';

export default {
  components: {
    LControl,
  },
  data() {
    return {
      ventanaImpresionAbierto: false,
      form: {
        titulo: '',
        disposicion: 'CurrentSize',
      },
    };
  },
  computed: {
    ...mapState(['tamanioVentana']),
  },
  mounted() {
    this.$nextTick(() => {
      const mapa = findRealParent(this.$parent).mapObject;
      this.easyPrintPlugin = L.easyPrint({
        hidden: true,
        exportOnly: true,
        sizeModes: ['CurrentSize', 'A4Portrait', 'A4Landscape'],
      });
      mapa.addControl(this.easyPrintPlugin);
    });
  },
  methods: {
    abrirVentanaImpresion() {
      this.ventanaImpresionAbierto = true;
    },
    cerrarVentanaImpresion() {
      this.ventanaImpresionAbierto = false;
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
    async imprimirMapa() {
      const formularioValido = await this.validarFormulario();
      if (!formularioValido) return;
      this.easyPrintPlugin.printMap(this.form.disposicion, this.form.titulo);
      this.form = {
        titulo: '',
        disposicion: 'CurrentSize',
      };
      this.$refs.form.resetFields();
    },
  },
};
</script>
