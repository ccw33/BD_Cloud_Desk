<template>
  <div class="node inline-row-start-start flex-nowrap">
    <div class="inline-row-start-start flex-nowrap">
      <div class="line"></div>
      <div class="self inline-column-start-center flex-nowrap"
           @click="$store.commit('node_focus',$attrs.self)">
        <div :class="snapshot_icon"></div>
        <div class="name text-center"
             :class="{'focus':$attrs.self.snapshot_id==$store.state.focus_node.snapshot_id}">{{ $attrs.self.name }}
        </div>
        <div class="descendant_line w-100"
             :style="{height:self_line_height+'rem'}"></div>
      </div>
    </div>
    <snapshot_children_nodes v-if="$attrs.self.snapshot_id in $store.state.node_tree"
                             :father_id="$attrs.self.snapshot_id"></snapshot_children_nodes>
  </div>
</template>

<script type="text/javascript">

  //因为是循环引用，所以father要动态引入children（其中一方动态引入）
  const snapshot_children_nodes = () => import('@/components/VM/snapshot_children_nodes');

  export default {
    name: 'snapshot_father_node',
    components: {snapshot_children_nodes},
    prop: {
      self: {
        type: Object,
        required: true,
      },
    },
    data() {
      return {};
    },
    computed: {
      snapshot_icon() {
        const vm = this;
        return vm.$attrs.self.is_current ? 'current' : 'not_current'
      },
      self_line_height() {
        const vm = this;
        if (!(vm.$attrs.self.snapshot_id in vm.$store.state.node_tree))
          return 0 // 叶子节点，没有儿子
        //递归求出所有叶子节点从而得出高度
        let descendant_len = 0;
        let append_decendant_len = (father_id) => {
          if (!(father_id in vm.$store.state.node_tree))
            return descendant_len++;
          vm.$store.state.node_tree[father_id].forEach((node, index, arr) => {
            append_decendant_len(node.snapshot_id)
          })
        }
        append_decendant_len(vm.$attrs.self.snapshot_id)
        return descendant_len > 1 ? (descendant_len - 1) * 4.5 - 2.8 : 0;
      }
    },
    created: function () {

    },
    methods: {},
    beforeCreate() {
      const vm = this;
    }
  }
</script>

<style scoped lang="scss">
  @import "../../assets/sass/base";
  @import "../../../node_modules/bootstrap/dist/css/bootstrap.css"; // todo ： 开发模式的时候引用一下才会有代码提示，但是生产模式要去掉
  .node {
    .line {
      margin-top: 1.3rem;
      width: 3rem;
      height: 0.4rem;
      background-color: #9AB2D3;
      /*border: {*/
      /*radius: 0.1rem;*/
      /*width: 0.1rem;*/
      /*style: solid;*/
      /*color: white;*/
      /*}*/
    }
    .self {
      &:hover {
        cursor: pointer;
      }
      .current, .not_current {
        width: 3rem;
        height: 3rem;
        background: {
          size: contain;
          position: center;
          repeat: no-repeat;
        }
      }
      .current {
        background-image: url("/static/img/icon/current_snapshot.png");
      }
      .not_current {
        background-image: url("/static/img/icon/snapshot.png");
      }
      .name {
        max-width: 3rem;
        height: 1.5rem;
        overflow: hidden;
      }
      .descendant_line {
        border-right: {
          style: solid;
          width: 0.4rem;
          color: #9AB2D3;
        }
      }
    }
    .focus {
      background-color: #4c9ddc;
    }
  }

</style>

