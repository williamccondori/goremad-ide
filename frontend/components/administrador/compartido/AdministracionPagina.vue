<template>
    <a-card class="app--altura-100">
        <div v-if="titulo">
            <a-page-header :title="titulo" @back="() => $router.back()" />
            <a-divider />
        </div>
        <slot />
    </a-card>
</template>

<script>
export default {
    props: {
        titulo: {
            type: String,
            default: undefined,
        },
    },
};
</script>
