<template>
  <div class="inline-column-start-start flex-nowrap">
        <snapshot_father_node v-for="child in children" :key="child.snapshot_id"
                              :self="child"></snapshot_father_node>
  </div>
</template>

<script type="text/javascript">
  import snapshot_father_node from '@/components/VM/snapshot_father_node';

  export default {
    name: 'snapshot_children_nodes',
    components: {snapshot_father_node},
    prop: {
      father_id: {
        type: String,
        required: true,
      },
      // node_tree: {
      //   type: Object,
      //   required: true,
      // }
    },
    data() {
      return {};
    },
    computed: {
      children() {
        const vm = this;
        return vm.$store.state.node_tree[vm.$attrs.father_id]
      }
    },
    methods: {},
  }
</script>

<style scoped lang="scss">
  @import "../../assets/sass/base";
  @import "../../../node_modules/bootstrap/dist/css/bootstrap.css"; // todo ： 开发模式的时候引用一下才会有代码提示，但是生产模式要去掉

</style>

