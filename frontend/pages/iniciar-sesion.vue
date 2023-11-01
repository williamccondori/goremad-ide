<template>
    <div
        style="
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        "
    >
        <a-card shadow="never" :style="{ width: esMovil ? '100%' : '400px' }">
            <div style="text-align: center">
                <img alt="logo" src="/logo.png" width="50%" />
            </div>
            <a-divider />
            <InicioSesionFormulario />
        </a-card>
    </div>
</template>

<script>
import { mapState } from 'vuex';
import InicioSesionFormulario from '@/components/administrador/inicio-sesion/InicioSesionFormulario.vue';

export default {
    components: { InicioSesionFormulario },
    layout: 'administrador',
    computed: {
        ...mapState(['esMovil']),
    },
};
</script>
