<template>
    <a-modal
        :footer="null"
        :visible="estaAbiertoCompartirVistaModal"
        @cancel="cerrarCompartirVistaModal()"
    >
        <span slot="title">
            <b>Compartir</b>
        </span>
        <a-space direction="vertical" size="large" style="width: 100%">
            <a-form-model
                ref="referenciaFormulario"
                :model="formulario"
                @submit.prevent="compartir()"
            >
                <a-form-model-item label="Ruta" prop="url">
                    <a-input v-model="formulario.url" :read-only="true">
                        <a-icon slot="addonBefore" type="global" />
                    </a-input>
                </a-form-model-item>
                <a-form-model-item label="Insertar" prop="url">
                    <a-input
                        v-model="formulario.insertar"
                        :read-only="true"
                        type="textarea"
                    />
                </a-form-model-item>
                <a-button block html-type="submit" icon="copy" type="primary">
                    Copiar ruta y cerrar ventana
                </a-button>
            </a-form-model>
            <div>
                <a-button
                    class="facebook"
                    target="_blank"
                    title="Compartir en Facebook"
                    @click="compartirEnFacebook()"
                >
                    <i class="bx bxl-facebook-square" />
                </a-button>
                <a-button
                    class="linkedin"
                    target="_blank"
                    title="Compartir en LinkedIn"
                    @click="compartirEnLinkedIn()"
                >
                    <i class="bx bxl-linkedin-square" />
                </a-button>
                <a-button
                    class="twitter"
                    target="_blank"
                    title="Compartir en Twitter"
                    @click="compartirEnTwitter()"
                >
                    <i class="bx bxl-twitter" />
                </a-button>
            </div>
        </a-space>
    </a-modal>
</template>

<script>
import { mapState, mapActions } from 'vuex';

const formulario = {
    url: '',
    insertar: '',
};

export default {
    data() {
        return {
            formulario: { ...formulario },
        };
    },
    computed: {
        ...mapState('visor', [
            'estaAbiertoCompartirVistaModal',
            'informacionPosicion',
        ]),
    },
    watch: {
        estaAbiertoCompartirVistaModal(valor) {
            if (valor) {
                const urlBase = window.location.href.split('?')[0];
                const { latitud, longitud, zoom } = this.informacionPosicion;
                this.formulario.url = `${urlBase}?latitud=${latitud}&longitud=${longitud}&zoom=${zoom}`;
                this.formulario.insertar = `<iframe src="${this.formulario.url}" width="100%" height="500px"></iframe>`;
            }
        },
    },
    methods: {
        ...mapActions('visor', ['cerrarCompartirVistaModal']),
        compartir() {
            navigator.clipboard.writeText(this.formulario.url);
            this.cerrarCompartirVistaModal();
        },
        compartirEnFacebook() {
            const url = `https://www.facebook.com/sharer/sharer.php?u=${this.formulario.url}&src=sdkpreparse?title=GEOGOREMAD&summary=Visor de mapas&source=GEOGOREMAD`;
            window.open(url, 'Compartir en Facebook', 'width=600,height=450');
        },
        compartirEnLinkedIn() {
            const url = `https://www.linkedin.com/shareArticle?mini=true&url=${this.formulario.url}&title=GEOGOREMAD&summary=Visor de mapas&source=GEOGOREMAD`;
            window.open(url, 'Compartir en LinkedIn', 'width=600,height=450');
        },
        compartirEnTwitter() {
            const url = `https://twitter.com/intent/tweet?url=${this.formulario.url}&text=GEOGOREMAD&hashtags=GEOGOREMAD`;
            window.open(url, 'Compartir en Twitter', 'width=600,height=450');
        },
    },
};
</script>
