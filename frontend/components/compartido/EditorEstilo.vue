<template>
  <a-card size="small">
    <a-form-model>
      <a-row :gutter="[8, 8]">
        <a-col :lg="6" :md="8" :sm="12" :xs="24">
          <a-form-model-item label="Color de línea" prop="color">
            <a-input v-model="form.color" type="color" />
          </a-form-model-item>
        </a-col>
        <a-col :lg="6" :md="8" :sm="12" :xs="24">
          <a-form-model-item label="Color de fondo" prop="fillColor">
            <a-input v-model="form.fillColor" type="color" />
          </a-form-model-item>
        </a-col>
        <a-col :lg="6" :md="8" :sm="12" :xs="24">
          <a-form-model-item label="Transparencia (fondo)" prop="fillOpacity">
            <a-slider
              v-model="form.fillOpacity"
              :max="1"
              :min="0"
              :step="0.1"
            />
          </a-form-model-item>
        </a-col>
        <a-col :lg="6" :md="8" :sm="12" :xs="24">
          <a-form-model-item label="Ancho de linea" prop="weight">
            <a-slider v-model="form.weight" :max="10" :min="1" />
          </a-form-model-item>
        </a-col>
        <a-col :lg="6" :md="8" :sm="12" :xs="24">
          <a-form-model-item label="Transparencia" prop="opacity">
            <a-slider v-model="form.opacity" :max="1" :min="0" :step="0.1" />
          </a-form-model-item>
        </a-col>
        <a-col :lg="6" :md="8" :sm="12" :xs="24">
          <a-form-model-item label="Unión de línea" prop="lineJoin">
            <a-select v-model="form.lineJoin">
              <a-select-option value="round">Redondeada</a-select-option>
              <a-select-option value="miter">Miter</a-select-option>
              <a-select-option value="bevel">Bevel</a-select-option>
            </a-select>
          </a-form-model-item>
        </a-col>
        <a-col :lg="6" :md="8" :sm="12" :xs="24">
          <a-form-model-item label="Regla de relleno" prop="fillRule">
            <a-select v-model="form.fillRule">
              <a-select-option value="evenodd">EvenOdd</a-select-option>
              <a-select-option value="nonzero">NonZero</a-select-option>
            </a-select>
          </a-form-model-item>
        </a-col>
      </a-row>
    </a-form-model>
    <input type="textarea" :value="JSON.stringify(form)" />
  </a-card>
</template>

<script>
export default {
  data() {
    return {
      form: {
        color: '#000000',
        fillColor: '#000000',
        weight: 1,
        opacity: 1,
        fillOpacity: 1,
        lineJoin: 'round',
        fillRule: 'evenodd',
      },
    };
  },
};
</script>
