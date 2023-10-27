<template>
    <AFormModel
        ref="referenciaFormulario"
        :model="formulario"
        @submit.prevent="guardar"
    >
        <ARow :gutter="16" justify="center" type="flex">
            <ACol :md="12" :xs="24" :xxl="6">
                <AFormModelItem
                    label="Nombre de la empresa:"
                    prop="nombreEmpresa"
                    :rules="[
                        {
                            required: true,
                            message: 'Ingrese el nombre de la empresa',
                        },
                    ]"
                >
                    <AInput
                        v-model="formulario.nombreEmpresa"
                        placeholder="Ingrese el nombre de la empresa"
                    />
                </AFormModelItem>
                <AFormModelItem
                    label="Latitud inicial:"
                    prop="latitudInicial"
                    :rules="[
                        {
                            required: true,
                            message: 'Ingrese la latitud inicial',
                        },
                    ]"
                >
                    <AInputNumber
                        v-model="formulario.latitudInicial"
                        class="app--w-100"
                        :max="180"
                        :min="-180"
                        :precision="6"
                        :step="0.000001"
                    />
                </AFormModelItem>
                <AFormModelItem
                    label="Longitud inicial:"
                    prop="longitudInicial"
                    :rules="[
                        {
                            required: true,
                            message: 'Ingrese la longitud inicial',
                        },
                    ]"
                >
                    <AInputNumber
                        v-model="formulario.longitudInicial"
                        class="app--w-100"
                        :max="180"
                        :min="-180"
                        :precision="6"
                        :step="0.000001"
                    />
                </AFormModelItem>
            </ACol>
            <ACol :md="12" :xs="24" :xxl="6">
                <AFormModelItem
                    label="Zoom inicial:"
                    prop="zoomInicial"
                    :rules="[
                        {
                            required: true,
                            message: 'Ingrese el zoom inicial',
                        },
                    ]"
                >
                    <AInputNumber
                        v-model="formulario.zoomInicial"
                        class="app--w-100"
                        :max="18"
                        :min="0"
                        placeholder="Zoom inicial"
                    />
                </AFormModelItem>
                <AFormModelItem
                    label="Capa base inicial:"
                    prop="capaBaseInicialId"
                >
                    <ASelect
                        v-model="formulario.capaBaseInicialId"
                        :allow-clear="true"
                        placeholder="Seleccione una capa base"
                    >
                        <ASelectOption
                            v-for="elemento in capasBase"
                            :key="elemento.id"
                            :value="elemento.id"
                        >
                            {{ elemento.nombre }}
                        </ASelectOption>
                    </ASelect>
                </AFormModelItem>
                <AFormModelItem
                    label="Servicios externos activos:"
                    prop="serviciosExternosActivosIds"
                >
                    <ASelect
                        v-model="formulario.serviciosExternosActivos"
                        mode="multiple"
                        placeholder="Seleccione uno o más servicios externos"
                    >
                        <ASelectOption
                            v-for="elemento in serviciosExternos"
                            :key="elemento.id"
                            :value="elemento.id"
                        >
                            {{ elemento.nombre }}
                        </ASelectOption>
                    </ASelect>
                </AFormModelItem>
            </ACol>
        </ARow>
        <ARow justify="center" type="flex">
            <ACol :xs="24" :xxl="12">
                <div>
                    <AButton
                        block
                        html-type="submit"
                        icon="save"
                        type="primary"
                    >
                        Actualizar variables
                    </AButton>
                </div>
            </ACol>
        </ARow>
    </AFormModel>
</template>

<script>
import {
    FormModel,
    Input,
    InputNumber,
    Select,
    Button,
    Row,
    Col,
} from 'ant-design-vue';
import { mapState, mapActions } from 'vuex';

const formulario = {
    nombreEmpresa: '',
    latitudInicial: 0,
    longitudInicial: 0,
    zoomInicial: 0,
    capaBaseInicialId: undefined,
    serviciosExternosActivos: [],
};

export default {
    components: {
        AFormModel: FormModel,
        AFormModelItem: FormModel.Item,
        AInput: Input,
        AInputNumber: InputNumber,
        ASelect: Select,
        ASelectOption: Select.Option,
        AButton: Button,
        ARow: Row,
        ACol: Col,
    },
    data() {
        return {
            formulario: { ...formulario },
        };
    },
    async fetch() {
        try {
            this.$iniciarCarga();
            await this.obtenerCapasBase();
            await this.obtenerServiciosExternos(true);
            await this.actualizarFormulario();
        } catch (error) {
            this.$manejarError(error);
        } finally {
            this.$finalizarCarga();
        }
    },
    computed: {
        ...mapState(['esMovil']),
        ...mapState('administrador', [
            'capasBase',
            'configuraciones',
            'serviciosExternos',
        ]),
    },
    methods: {
        ...mapActions('administrador', [
            'obtenerCapasBase',
            'obtenerConfiguraciones',
            'obtenerServiciosExternos',
        ]),
        async actualizarFormulario() {
            await this.obtenerConfiguraciones();
            // Si el valor es null o vacio se convierte a undefined para que el formulario no lo tome como un valor.
            const configuraciones = this.configuraciones.map(
                (configuracion) => ({
                    ...configuracion,
                })
            );
            configuraciones.forEach((configuracion) => {
                if (
                    configuracion.valor === null ||
                    configuracion.valor === ''
                ) {
                    configuracion.valor = undefined;
                }
            });
            const nombreEmpresa = configuraciones.find(
                (configuracion) => configuracion.nombre === 'nombre_empresa'
            )?.valor;
            const latitudInicial = configuraciones.find(
                (configuracion) => configuracion.nombre === 'latitud_inicial'
            )?.valor;
            const longitudInicial = configuraciones.find(
                (configuracion) => configuracion.nombre === 'longitud_inicial'
            )?.valor;
            const zoomInicial = configuraciones.find(
                (configuracion) => configuracion.nombre === 'zoom_inicial'
            )?.valor;
            const capaBaseInicialId = configuraciones.find(
                (configuracion) =>
                    configuracion.nombre === 'capa_base_incial_id'
            )?.valor;
            this.formulario.nombreEmpresa = nombreEmpresa;
            this.formulario.latitudInicial = latitudInicial;
            this.formulario.longitudInicial = longitudInicial;
            this.formulario.zoomInicial = zoomInicial;
            this.formulario.capaBaseInicialId = capaBaseInicialId;
            // Los servicios externos manejan un tratamiento especial.
            const serviciosExternosActivos = this.configuraciones.find(
                (configuracion) =>
                    configuracion.nombre === 'servicios_externos_activos'
            )?.valor;
            this.formulario.serviciosExternosActivos =
                serviciosExternosActivos?.split(',') ?? [];
        },
        guardar() {
            this.$refs.referenciaFormulario?.validate(async (valid) => {
                if (valid) {
                    try {
                        this.$iniciarCarga();
                        // Se valida el contenido de las capas base.
                        if (
                            this.formulario.capaBaseInicialId === null ||
                            this.formulario.capaBaseInicialId === ''
                        ) {
                            this.formulario.capaBaseInicialId = undefined;
                        }
                        // Se valida el contenido de los servicios externos.
                        if (
                            this.formulario.serviciosExternosActivos.length ===
                            0
                        ) {
                            this.formulario.serviciosExternosActivos =
                                undefined;
                        } else {
                            this.formulario.serviciosExternosActivos =
                                this.formulario.serviciosExternosActivos.join(
                                    ','
                                );
                        }
                        await this.$axios.put(`/configuraciones/`, {
                            ...this.formulario,
                        });
                        await this.actualizarFormulario();
                        this.$mostrarMensajeCorrecto();
                    } catch (error) {
                        this.$manejarError(error);
                    } finally {
                        this.$finalizarCarga();
                    }
                }
            });
        },
    },
};
</script>
