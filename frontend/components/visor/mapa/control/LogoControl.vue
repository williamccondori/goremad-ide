<template>
  <LControl position="bottomleft">
    <NuxtLink to="/">
      <img src="/logo.png" alt="logo" width="180" />
    </NuxtLink>
  </LControl>
</template>

<script>
import { LControl } from "vue2-leaflet";
export default {
  components: {
    LControl,
  },
};
</script>
