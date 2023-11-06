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
                    <a-collapse expand-icon-position="right">
                        <a-collapse-panel
                            v-for="catalogo in estructuraObjetosGeograficos"
                            :key="catalogo.id"
                            class="ant-collapse-fluid"
                        >
                            <span slot="header">
                                <b>{{ catalogo.nombre }}</b>
                            </span>
                            <a-collapse
                                :bordered="false"
                                expand-icon-position="right"
                            >
                                <a-collapse-panel
                                    v-for="tema in catalogo.temas"
                                    :key="tema.id"
                                >
                                    <span slot="header">
                                        <b>{{ tema.nombre }}</b>
                                    </span>
                                    <div
                                        v-for="grupo in tema.grupos"
                                        :key="grupo.id"
                                    >
                                        <p>
                                            <b>{{ grupo.nombre }}</b>
                                        </p>
                                        <div
                                            v-for="objeto in grupo.objetos"
                                            :key="objeto.id"
                                        >
                                            {{ objeto.nombre }}
                                        </div>
                                    </div>
                                </a-collapse-panel>
                            </a-collapse>
                        </a-collapse-panel>
                    </a-collapse>
                </a-tab-pane>
            </a-tabs>
        </a-space>
    </a-drawer>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
    computed: {
        ...mapState(['tamanioVentana']),
        ...mapState('visor', [
            'estaAbiertoVentanaDescargarInformacion',
            'estructuraObjetosGeograficos',
        ]),
    },
    methods: {
        ...mapActions('visor', ['cerrarVentana']),
    },
};
</script>
