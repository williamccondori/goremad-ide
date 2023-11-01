<template>
    <ADrawer
        :mask-closable="false"
        :visible="estaAbiertoServicioExternoFormularioVentana"
        :width="esMovil ? '100%' : 400"
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
            <a-form-model-item
                label="URL:"
                prop="url"
                :rules="[
                    {
                        required: true,
                        message: 'Ingrese la URL del servicio externo',
                    },
                ]"
            >
                <a-input
                    v-model="formulario.url"
                    placeholder="Ingrese la URL del servicio externo"
                />
            </a-form-model-item>
            <a-form-model-item
                label="Nombre:"
                prop="nombre"
                :rules="[
                    {
                        required: true,
                        message: 'Ingrese el nombre del servicio externo',
                    },
                ]"
            >
                <a-input
                    v-model="formulario.nombre"
                    placeholder="Ingrese el nombre del servicio externo"
                />
            </a-form-model-item>
            <a-form-model-item label="Filtros CQL:" prop="filtros">
                <a-alert>
                    <div slot="message">
                        <div>
                            <b>Nota:</b> Los filtros CQL son opcionales. Si se
                            ingresan, se aplicarán a todas las capas del
                            servicio externo, por tanto, se recomienda aplicar a
                            servicios de. una sola capa.
                        </div>
                        <div>
                            <b>Importante!</b>
                            <ul>
                                <li>Separar los filtros por comas.</li>
                                <li>
                                    Los nombre de las columnas deben venir de la
                                    base de datos, no del alias.
                                </li>
                                <li>
                                    <i>
                                        Función experimental, puede no
                                        funcionar.
                                    </i>
                                </li>
                            </ul>
                        </div>
                    </div>
                </a-alert>
                <a-input
                    v-model="formulario.filtros"
                    placeholder="Ingrese filtros CQL"
                >
                    <span slot="addonAfter">
                        <a-tooltip placement="top" title="Ayuda">
                            <a-icon
                                type="question-circle"
                                style="cursor: pointer"
                                @click="openHelpWindow()"
                            />
                        </a-tooltip>
                    </span>
                </a-input>
            </a-form-model-item>
            <a-form-model-item
                label="Atribución:"
                prop="atribucion"
                :rules="[
                    {
                        required: true,
                        message: 'Ingrese la atribución del servicio externo',
                    },
                ]"
            >
                <a-input
                    v-model="formulario.atribucion"
                    placeholder="Ingrese la atribución del servicio externo"
                />
            </a-form-model-item>
            <a-form-model-item label="Grupo de capas:" prop="grupoCapaId">
                <a-select
                    v-model="formulario.grupoCapaId"
                    :allow-clear="true"
                    placeholder="Seleccione un grupo de capas"
                    style="width: 100%"
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
            <a-form-model-item label="¿Está habilitado?:" prop="estaHabilitado">
                <ACheckbox v-model="formulario.estaHabilitado" />
            </a-form-model-item>
            <div>
                <AButton block html-type="submit" icon="save" type="primary">
                    {{ titulo }}
                </AButton>
            </div>
        </a-form-model>
    </ADrawer>
</template>

<script>
import { mapActions, mapState } from 'vuex';

const formulario = {
    url: '',
    nombre: '',
    atribucion: '',
    filtros: '',
    grupoCapaId: undefined,
    estaHabilitado: true,
};

export default {
    data() {
        return {
            formulario: { ...formulario },
        };
    },
    async fetch() {
        try {
            this.$iniciarCarga();
            await this.obtenerGruposCapas();
        } catch (error) {
            this.$manejarError(error);
        } finally {
            this.$finalizarCarga();
        }
    },
    computed: {
        ...mapState(['esMovil']),
        ...mapState('administrador', [
            'estaAbiertoServicioExternoFormularioVentana',
            'gruposCapas',
            'servicioExterno',
        ]),
        esEdicion() {
            return this.servicioExterno !== undefined;
        },
        titulo() {
            return this.esEdicion
                ? 'Actualizar servicio externo'
                : 'Crear servicio externo';
        },
    },
    watch: {
        estaAbiertoServicioExternoFormularioVentana(value) {
            if (!value) {
                this.formulario = { ...formulario };
                this.$refs.referenciaFormulario?.resetFields();
            } else {
                if (this.esEdicion && this.servicioExterno) {
                    // Si el valor es null o vacio se convierte a undefined para que el formulario no lo tome como un valor.
                    const servicioExterno = { ...this.servicioExterno };
                    Object.keys(servicioExterno).forEach((key) => {
                        if (
                            servicioExterno[key] === null ||
                            servicioExterno[key] === ''
                        ) {
                            servicioExterno[key] = undefined;
                        }
                    });
                    this.formulario.nombre = servicioExterno.nombre;
                    this.formulario.url = servicioExterno.url;
                    this.formulario.filtros = servicioExterno.filtros;
                    this.formulario.atribucion = servicioExterno.atribucion;
                    this.formulario.grupoCapaId = servicioExterno.grupoCapaId;
                    this.formulario.estaHabilitado =
                        servicioExterno.estaHabilitado;
                }
            }
        },
    },
    methods: {
        ...mapActions('administrador', [
            'cerrarServicioExternoFormularioVentana',
            'obtenerGruposCapas',
            'obtenerServiciosExternos',
        ]),
        guardar() {
            this.$refs.referenciaFormulario?.validate(async (valid) => {
                if (valid) {
                    try {
                        this.$iniciarCarga();
                        // Se valida el contenido del grupo de capas.
                        if (
                            this.formulario.grupoCapaId === null ||
                            this.formulario.grupoCapaId === ''
                        ) {
                            this.formulario.grupoCapaId = undefined;
                        }
                        if (this.esEdicion) {
                            await this.$axios.put(
                                `/servicios-externos/${this.servicioExterno.id}/`,
                                {
                                    ...this.formulario,
                                }
                            );
                        } else {
                            await this.$axios.post('/servicios-externos/', {
                                ...this.formulario,
                            });
                        }
                        await this.obtenerServiciosExternos();
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
        openHelpWindow() {
            window.open(
                'https://docs.geoserver.org/2.23.x/en/user/tutorials/cql/cql_tutorial.html',
                '_blank'
            );
        },
    },
};
</script>
