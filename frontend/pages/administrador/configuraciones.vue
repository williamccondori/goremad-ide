<template>
    <AdministracionPagina titulo="Configuraciones">
        <ATabs type="card">
            <ATabPane key="1" tab="Usuarios">
                <ASpace class="app--w-100" direction="vertical">
                    <AButton
                        icon="plus"
                        type="primary"
                        @click="abrirUsuarioFormularioVentana()"
                    >
                        Crear usuario
                    </AButton>
                    <UsuarioCatalogo />
                </ASpace>
                <UsuarioFormularioVentana />
            </ATabPane>
            <ATabPane key="2" tab="Roles">
                <RolCatalogo />
                <RolFormularioVentana />
            </ATabPane>
            <ATabPane key="3" tab="Variables">
                <VariableFormulario />
            </ATabPane>
        </ATabs>
    </AdministracionPagina>
</template>

<script>
import { Button, Space, Tabs } from 'ant-design-vue';
import { mapActions } from 'vuex';
import AdministracionPagina from '@/components/administrador/compartido/AdministracionPagina.vue';
import UsuarioCatalogo from '@/components/administrador/usuario/UsuarioCatalogo.vue';
import UsuarioFormularioVentana from '@/components/administrador/usuario/UsuarioFormularioVentana.vue';
import RolCatalogo from '@/components/administrador/rol/RolCatalogo.vue';
import RolFormularioVentana from '@/components/administrador/rol/RolFormularioVentana.vue';
import VariableFormulario from '~/components/administrador/variable/VariableFormulario.vue';
export default {
    components: {
        AButton: Button,
        ASpace: Space,
        ATabs: Tabs,
        ATabPane: Tabs.TabPane,
        AdministracionPagina,
        UsuarioCatalogo,
        UsuarioFormularioVentana,
        RolCatalogo,
        RolFormularioVentana,
        VariableFormulario,
    },
    layout: 'administrador',
    methods: {
        ...mapActions('administrador', ['abrirUsuarioFormularioVentana']),
    },
};
</script>
