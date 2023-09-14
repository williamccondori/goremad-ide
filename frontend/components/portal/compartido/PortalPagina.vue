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
import { Card, Divider, PageHeader } from 'ant-design-vue';
export default {
  components: {
    ACard: Card,
    ADivider: Divider,
    APageHeader: PageHeader,
  },
  props: {
    titulo: {
      type: String,
      default: undefined,
    },
  },
};
</script>
