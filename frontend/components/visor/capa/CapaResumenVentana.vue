<template>
  <ADrawer
    :mask="false"
    :width="esMovil ? '100%' : 400"
    :visible="estaAbiertoCapaResumenVentana"
    @close="cerrarCapaResumenVentana()"
  >
    <span slot="title" style="text-transform: uppercase">
      <b>Información de las capas activas</b>
    </span>
    <AFormModel ref="referenciaFormulario" :model="formulario">
      <AFormModelItem label="Capa activa">
        <ASelect
          v-model="formulario.elementoActivoId"
          placeholder="Seleccione"
          :allow-clear="true"
          @change="cambiarElementoActivoId"
        >
          <ASelectOption
            v-for="elemento in elementosActivos"
            :key="elemento.id"
            :value="elemento.id"
          >
            {{ elemento.titulo }}
          </ASelectOption>
        </ASelect>
      </AFormModelItem>
    </AFormModel>
    <div v-if="elementoActivo" class="app--contenedor-vertical-pequenio">
      <ADescriptions
        bordered
        size="small"
        :column="1"
        :title="elementoActivo.titulo"
      >
        <ADescriptionsItem label="Servicio:">
          {{ elementoActivo.servicioTitulo }}
        </ADescriptionsItem>
        <ADescriptionsItem label="Autor:">
          {{ elementoActivo.atribucion }}
        </ADescriptionsItem>
        <ADescriptionsItem label="Título:">
          {{ elementoActivo.titulo }}
        </ADescriptionsItem>
        <ADescriptionsItem label="Nombre:">
          <ATag size="small"> {{ elementoActivo.nombre }}</ATag>
        </ADescriptionsItem>
        <ADescriptionsItem label="Leyenda:">
          <img :src="elementoActivo.urlLeyenda" alt="Leyenda" />
        </ADescriptionsItem>
      </ADescriptions>
      <ACard size="small">
        <span>Transparencia:</span>
        <ASlider v-model="transparencia" :step="0.1" :min="0" :max="1" />
      </ACard>
      <ACard size="small">
        <AButton block icon="upload" @click="traerAlFrente(elementoActivo.id)">
          Traer al frente
        </AButton>
        <ADivider />
        <AButton
          block
          icon="search"
          @click="verAreaCobertura(elementoActivo.cuadroDelimitador)"
        >
          Zoom a la capa
        </AButton>
        <ADivider />
        <AButton
          block
          type="danger"
          icon="delete"
          @click="eliminarCapaActivaYCerrar(elementoActivo.id)"
        >
          Remover capa del mapa
        </AButton>
      </ACard>
    </div>
  </ADrawer>
</template>

<script>
import {
  Drawer,
  Select,
  FormModel,
  Button,
  Card,
  Slider,
  Divider,
  Descriptions,
  Tag,
} from "ant-design-vue";
import { mapState, mapActions } from "vuex";

const formulario = {
  elementoActivoId: undefined,
};

export default {
  components: {
    ADrawer: Drawer,
    ASelect: Select,
    ASelectOption: Select.Option,
    AFormModel: FormModel,
    AFormModelItem: FormModel.Item,
    AButton: Button,
    ACard: Card,
    ASlider: Slider,
    ADivider: Divider,
    ADescriptions: Descriptions,
    ADescriptionsItem: Descriptions.Item,
    ATag: Tag,
  },
  data() {
    return {
      formulario: { ...formulario },
      elementoActivo: undefined,
    };
  },
  computed: {
    ...mapState(["esMovil"]),
    ...mapState("visor", [
      "estaAbiertoCapaResumenVentana",
      "capasActivas",
      "capas",
    ]),
    elementosActivos() {
      const elementosActivos = this.capas.filter((capa) => {
        return this.capasActivas.includes(capa.id);
      });
      return elementosActivos;
    },
    transparencia: {
      get() {
        return this.elementoActivo.transparencia ?? 1;
      },
      set(transparencia) {
        this.establecerCapaTransparencia({
          id: this.elementoActivo.id,
          transparencia,
        });
      },
    },
  },
  watch: {
    estaAbiertoCapaResumenVentana(valor) {
      if (valor) {
        this.formulario = { ...formulario };
        this.elementoActivo = undefined;
      }
    },
  },
  methods: {
    ...mapActions("visor", [
      "cerrarCapaResumenVentana",
      "establecerCapaTransparencia",
      "establecerCapaSuperior",
      "establecerBounds",
      "eliminarCapaActiva",
    ]),
    cambiarElementoActivoId(capaActivaId) {
      this.elementoActivo = this.elementosActivos.find(
        (elemento) => elemento.id === capaActivaId
      );
    },
    traerAlFrente(capaId) {
      this.establecerCapaSuperior(capaId);
    },
    verAreaCobertura(cuadroDelimitador) {
      const bounds = [
        [cuadroDelimitador[1], cuadroDelimitador[0]],
        [cuadroDelimitador[3], cuadroDelimitador[2]],
      ];
      this.establecerBounds(bounds);
    },
    eliminarCapaActivaYCerrar(id) {
      this.eliminarCapaActiva(id);
      this.establecerCapaTransparencia({ id, transparencia: 1 });
      this.cerrarCapaResumenVentana();
    },
  },
};
</script>
