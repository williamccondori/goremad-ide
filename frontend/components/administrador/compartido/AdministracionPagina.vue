<template>
  <ACard class="app--altura-100">
    <div v-if="titulo">
      <APageHeader :title="titulo" @back="() => $router.back()" />
      <ADivider />
    </div>
    <slot />
  </ACard>
</template>

<script>
import { Card, PageHeader, Divider } from "ant-design-vue";
export default {
  components: {
    ACard: Card,
    APageHeader: PageHeader,
    ADivider: Divider,
  },
  props: {
    titulo: {
      type: String,
      default: undefined,
    },
  },
};
</script>
