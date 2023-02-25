<template>
  <a-collapse expand-icon-position="right" :active-key="activeKey">
    <a-collapse-panel key="1">
      <span slot="header" class="titulo">
        <h1><i :class="`bx bx-${icon}`" /> {{ title }}</h1>
      </span>
      <slot />
    </a-collapse-panel>
  </a-collapse>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true,
    },
    icon: {
      type: String,
      required: true,
    },
    collapse: {
      type: Boolean,
      default: true,
    },
  },
  computed: {
    activeKey() {
      return this.collapse ? [] : ["1"];
    },
  },
};
</script>

<style scoped>
.titulo i {
  background-color: green;
  box-shadow: rgb(1 41 112 / 10%) 0px 2px 20px;
  color: white;
  height: 1.5rem;
  line-height: 1.5rem;
  margin-right: 0.5rem;
  text-align: center;
  width: 1.5rem;
}
.titulo h1 {
  font-size: 0.8rem;
  font-weight: bold;
  margin: 0;
  padding: 0;
}
</style>
