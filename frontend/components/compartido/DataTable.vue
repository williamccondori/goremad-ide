<template>
  <a-table
    :row-key="tableId"
    :columns="headers"
    :data-source="data"
    size="middle"
    class="tabla"
    bordered
  >
    <template slot="label" slot-scope="value">
      <a-tag color="purple"> {{ value }}</a-tag>
    </template>
    <template slot="boolean" slot-scope="value">
      <a-tag :color="value ? 'green' : 'red'">
        {{ value ? "SI" : "NO" }}
      </a-tag>
    </template>
    <template slot="actions" slot-scope="id">
      <a-button
        v-if="showEdit"
        type="dashed"
        size="small"
        @click="onLocalEdit(id)"
      >
        <a-icon type="edit" />
      </a-button>
      <slot :id="id" name="actions" />
      <a-popconfirm
        v-if="showDelete"
        title="¿Está seguro que desea eliminar este registro?"
        @confirm="onLocalDelete(id)"
      >
        <a-button type="dashed" size="small">
          <a-icon type="delete" />
        </a-button>
      </a-popconfirm>
    </template>
  </a-table>
</template>

<script>
export default {
  props: {
    data: {
      type: Array,
      default: () => [],
    },
    columns: {
      type: Object,
      required: true,
    },
    showEdit: {
      type: Boolean,
      default: true,
    },
    showDelete: {
      type: Boolean,
      default: true,
    },
  },
  data() {
    return {
      tableId: "id",
    };
  },
  computed: {
    headers() {
      const { labels, booleans, ...columns } = this.columns;
      return Object.keys(columns).map((key) => {
        const columnDefinition = {
          title: this.columns[key],
          dataIndex: key,
          key,
        };

        // Add actions slot if it's defined
        if (key === "actions") {
          columnDefinition.dataIndex = this.tableId;
          columnDefinition.scopedSlots = {
            customRender: "actions",
          };
        } else {
          columnDefinition.sorter = (a, b) => {
            if (a[key] < b[key]) {
              return -1;
            }
            if (a[key] > b[key]) {
              return 1;
            }
            return 0;
          };
        }

        // If it's a label, add a custom render.
        if (labels && labels.includes(key)) {
          columnDefinition.scopedSlots = {
            customRender: "label",
          };
        }

        // If it's a boolean column, add a custom render.
        if (booleans && booleans.includes(key)) {
          columnDefinition.scopedSlots = {
            customRender: "boolean",
          };
        }

        return columnDefinition;
      });
    },
  },
  methods: {
    onLocalEdit(id) {
      this.$emit("onEdit", id);
    },
    onLocalDelete(id) {
      this.$emit("onDelete", id);
    },
  },
};
</script>

<style scoped>
.tabla td {
  padding: 0px !important;
}
</style>
