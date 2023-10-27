<template>
    <LControl position="bottomleft">
        <NuxtLink to="/">
            <img alt="logo" src="/logo.png" width="180" />
        </NuxtLink>
    </LControl>
</template>
<script>
import { LControl } from 'vue2-leaflet';
export default {
    components: {
        LControl,
    },
};
</script>
