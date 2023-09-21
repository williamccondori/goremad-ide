<template>
  <a-drawer
    :visible="estaAbiertoVentanaDescargarInformacion"
    :width="tamanioVentana"
    @close="cerrarVentana('DescargarInformacion')"
  >
    <span slot="title">
      <b>Descargar información</b>
    </span>
    <a-space direction="vertical" style="width: 100%">
      <a-tabs default-active-key="capasOperables" type="card">
        <a-tab-pane key="capasOperables" tab="Capas">
          <a-form-model
            :model="form"
            :rules="rules"
            @submit.prevent="descargarInformacionCapas()"
          >
            <a-form-model-item label="Temática" prop="tematica">
              <a-select
                v-model="form.tematica"
                placeholder="Seleccione una temática"
                @change="form.capaGeografica = undefined"
              >
                <a-select-option
                  v-for="tematica in tematicas"
                  :key="tematica.id"
                >
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
            <a-form-model-item label="Formato" prop="formato">
              <a-select
                v-model="form.formato"
                placeholder="Seleccione un formato"
              >
                <a-select-option v-for="formato in formatos" :key="formato.id">
                  {{ formato.nombre }}
                </a-select-option>
              </a-select>
            </a-form-model-item>
            <a-button block html-type="submit" type="primary">
              <a-icon type="download" />
              Descargar
            </a-button>
          </a-form-model>
        </a-tab-pane>
        <a-tab-pane key="dibujos" tab="Dibujos">
          Aquí de podrá descargar dibujos
        </a-tab-pane>
      </a-tabs>
    </a-space>
  </a-drawer>
</template>

<script>
import { mapState, mapActions } from 'vuex';
export default {
  data() {
    return {
      form: {
        tematica: undefined,
        capaGeografica: undefined,
        formato: undefined,
      },
      tematicas: [],
      formatos: [],
      gruposDiponibles: [],
    };
  },
  computed: {
    ...mapState(['tamanioVentana']),
    ...mapState('visor', ['estaAbiertoVentanaDescargarInformacion']),
  },
  methods: {
    ...mapActions('visor', ['cerrarVentana']),
    descargarInformacionCapas() {},
  },
};
</script>
