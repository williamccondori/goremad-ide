<template>
  <ADrawer
    :width="esMovil ? '100%' : 400"
    :visible="estaAbiertoImagenSatelitalBuscadorFormularioVentana"
    @close="cerrarImagenSatelitalBuscadorFormularioVentana()"
  >
    <span slot="title" style="text-transform: uppercase">
      <b>Buscar imágenes satelitales</b>
    </span>
    <div class="app--contenedor-vertical">
      <AAlert show-icon message="Información">
        <span slot="description">
          Disponibles imágenes SENTINEL-2 MSI - Level-1A (10m) en sus
          composiciones: <ATag color="blue">RGB</ATag>
          <ATag color="blue">NDVI</ATag> <ATag color="blue">NDWI</ATag>.
        </span>
      </AAlert>
      <AFormModel
        ref="referenciaFormulario"
        :model="formulario"
        @submit.prevent="buscar()"
      >
        <AFormModelItem
          prop="identificador"
          label="Identificador de la imágen satelital"
        >
          <AInput
            v-model="formulario.identificador"
            placeholder="Identificador de la imágen satelital"
          />
        </AFormModelItem>
        <div>
          <AButton html-type="submit" type="primary" icon="search" block>
            Buscar
          </AButton>
        </div>
        <ADivider />
        <ACollapse>
          <ACollapsePanel key="1" header="Búsqueda avanzada">
            <AFormModelItem prop="satelitle" label="Satélite">
              <ASelect
                v-model="formulario.satelitle"
                placeholder="Todos"
                disabled
              >
                <ASelectOption value="S2A">S2A</ASelectOption>
                <ASelectOption value="S2B">S2B</ASelectOption>
              </ASelect>
            </AFormModelItem>
            <AFormModelItem prop="fechas" label="Intérvalo de fechas">
              <ARangePicker
                v-model="formulario.fechas"
                format="DD/MM/YYYY"
                class="app--w-100"
              />
            </AFormModelItem>
          </ACollapsePanel>
        </ACollapse>
      </AFormModel>
      <ARow type="flex" justify="space-between" align="middle">
        <span>Todos los elementos:</span>
        <ATag color="green">
          {{ resultados.length }}
        </ATag>
      </ARow>
      <AList :data-source="resultados">
        <AListItem
          slot="renderItem"
          slot-scope="imagenSatelital"
          class="elemento-lista"
        >
          <ASpace direction="vertical" class="app--w-100">
            <AListItemMeta
              :title="imagenSatelital.identificador"
              :description="`Detalles: ${imagenSatelital.descripcion}`"
            >
              <AAvatar
                slot="avatar"
                shape="square"
                icon="picture"
                :style="{
                  backgroundColor: '#87d068',
                }"
              />
            </AListItemMeta>
            <ASpace class="app--w-100">
              <AButton
                type="dashed"
                icon="plus"
                size="small"
                @click="agregarAlCatalogo(imagenSatelital)"
              >
                Agregar al catálogo
              </AButton>
            </ASpace>
          </ASpace>
        </AListItem>
      </AList>
    </div>
  </ADrawer>
</template>

<script>
import {
  Drawer,
  Alert,
  Tag,
  FormModel,
  Input,
  Collapse,
  Select,
  DatePicker,
  Button,
  Divider,
  Row,
  List,
  Space,
  Avatar,
} from "ant-design-vue";
import { mapState, mapActions } from "vuex";

const formulario = {
  identificador: "",
  satelitle: undefined,
  fechas: [],
};

export default {
  components: {
    ADrawer: Drawer,
    AAlert: Alert,
    ATag: Tag,
    AFormModel: FormModel,
    AFormModelItem: FormModel.Item,
    AInput: Input,
    ACollapse: Collapse,
    ACollapsePanel: Collapse.Panel,
    ASelect: Select,
    ASelectOption: Select.Option,
    ARangePicker: DatePicker.RangePicker,
    AButton: Button,
    ADivider: Divider,
    ARow: Row,
    AList: List,
    AListItem: List.Item,
    AListItemMeta: List.Item.Meta,
    ASpace: Space,
    AAvatar: Avatar,
  },
  data() {
    return {
      formulario: { ...formulario },
      resultados: [],
    };
  },
  computed: {
    ...mapState(["esMovil"]),
    ...mapState("visor", [
      "estaAbiertoImagenSatelitalBuscadorFormularioVentana",
      "imagenesSatelitales",
    ]),
  },
  watch: {
    estaAbiertoImagenSatelitalBuscadorFormularioVentana() {
      if (!this.estaAbiertoImagenSatelitalBuscadorFormularioVentana) {
        this.formulario = { ...formulario };
        this.$refs.referenciaFormulario?.resetFields();
        this.resultados = [];
      }
    },
  },
  methods: {
    ...mapActions("visor", [
      "cerrarImagenSatelitalBuscadorFormularioVentana",
      "agregarImagenSatelital",
      "agregarCapas",
    ]),
    buscar() {
      this.$refs.referenciaFormulario?.validate(async (valid) => {
        if (valid) {
          try {
            this.$iniciarCarga();
            const fInicio =
              this.formulario.fechas[0] === ""
                ? undefined
                : this.formulario.fechas[0];
            const fFin =
              this.formulario.fechas[1] === ""
                ? undefined
                : this.formulario.fechas[1];
            const fechaInicio = fInicio ? new Date(fInicio) : undefined;
            const fechaFin = fFin ? new Date(fFin) : undefined;
            const { data } = await this.$axios.get(
              `/visor/imagenes-satelitales/busquedas/`,
              {
                params: {
                  identificador:
                    this.formulario.identificador === ""
                      ? undefined
                      : this.formulario.identificador,
                  satelitle: this.formulario.satelitle,
                  fechaInicio,
                  fechaFin,
                },
              }
            );
            this.resultados = data;
            this.$mostrarMensajeCorrecto(
              `Se encontraron ${data.length} imágenes`
            );
          } catch (error) {
            this.$manejarError(error);
          } finally {
            this.$finalizarCarga();
          }
        }
      });
    },
    async agregarAlCatalogo(imagenSatelital) {
      try {
        this.$iniciarCarga();
        // Se verifica que no exista la imagen satelital en el catalogo.
        const existe = this.imagenesSatelitales.find(
          (x) => x.identificador === imagenSatelital.identificador
        );
        if (!existe) {
          const { data } = await this.$axios.get(
            `/visor/imagenes-satelitales/capas/`,
            {
              params: {
                id: imagenSatelital.id,
              },
            }
          );
          this.agregarImagenSatelital(data.imagenSatelital);
          this.agregarCapas(data.capas);
        } else {
          this.$mostrarMensajeAdvertencia(
            `La imagen satelital ya existe en el catálogo`
          );
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
