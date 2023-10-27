<template>
    <a-modal
        :closable="false"
        :footer="null"
        :title="null"
        :visible="estaAbiertoBienvenidaModal"
    >
        <div style="text-align: center">
            <Titulo />
        </div>
        <a-divider />
        <div style="text-align: justify">
            <p>
                Bienvenidos al <b>GEOGOREMAD</b>, la Infraestructura de Datos
                Espaciales (IDE) diseñada para fortalecer el desarrollo
                territorial de Madre de Dios. Esta plataforma es el resultado de
                una integración armoniosa de políticas, estándares, entidades
                colaboradoras, talento humano y tecnologías avanzadas. Su
                propósito es facilitar el intercambio, producción, adquisición,
                y acceso a información geoespacial tanto a nivel regional como
                nacional, optimizando así la toma de decisiones informadas. Vale
                destacar que <b>GEOGOREMAD</b> está en evolución constante,
                actualizándose ya sea por la incorporación de nuevos estudios o
                por la revisión y corrección de datos.
            </p>
        </div>
        <a-checkbox v-model="terminosAceptados">
            Acepto los términos y condiciones de uso.
        </a-checkbox>
        <a-divider />
        <a-button
            block
            :disabled="!terminosAceptados"
            html-type="button"
            type="primary"
            @click="cerrarModal()"
        >
            Ingresar
        </a-button>
    </a-modal>
</template>
<script>
import Titulo from '../compartido/Titulo.vue';
export default {
    components: { Titulo },
    data() {
        return {
            terminosAceptados: false,
            estaAbiertoBienvenidaModal: true,
        };
    },
    methods: {
        cerrarModal() {
            this.estaAbiertoBienvenidaModal = false;
        },
    },
};
</script>
