<template>
  <div class="content inline-column-center-center bg-white">
    <header class="w-100 inline-row-center-baseline justify-content-between">
      <div class="title">虚机快照管理</div>
      <div class="cancel" @click="$emit('close')">×</div>
    </header>
    <article class="w-100 bd_scroll text-left">
      <snapshot_father_node
        :self="$store.state.node_tree.root[0]"></snapshot_father_node>
    </article>
    <footer class="w-100 inline-row-center-baseline justify-content-between">
      <section class="left">
        <div class="line">
          <label class="col-4">创建时间：</label>
          <div class="text col-8 text-left">{{ $store.state.focus_node.created_at }}</div>
        </div>
        <div class="line">
          <label for="name" class="col-4">名称：</label>
          <input type="text" id="name" class="form-control-sm col-8"
                 :value="$store.state.focus_node.name"
                 @change="$store.commit('modify_node',
                     {'node':$store.state.focus_node,'attr':'name','val':$event.target.value}
                     )">
        </div>
        <div class="line">
          <label for="description" class="col-4">描述：</label>
          <textarea id="description" class="form-control col-8"
                    rows="3">{{ $store.state.focus_node.description }}</textarea>
        </div>
      </section>

      <section class="right inline-column-end-start">
        <button type="button" class="btn btn-sm btn-primary" @click="$refs.create_snapshot.show()">拍摄快照</button>
        <button type="button" class="btn btn-sm btn-primary mt-2" @click="delete_snapshot">删除快照</button>
        <button type="button" class="btn btn-sm btn-primary mt-2" @click="go_to_snapshot">转到快照</button>
      </section>
    </footer>

    <my_modal ref="create_snapshot">
      <div class="create_snapshot inline-column-center-center">
        <div class="head inline-row-start-center  flex-nowrap w-100">
          <div class="image"></div>
          <h5 class="text-left m-0">创建快照</h5>
          <div class="cancel ml-auto" @click="$refs.create_snapshot.hide()">×</div>
        </div>
        <div class="center inline-column-start-start w-100">
          <div class="line">
            <label class="col-4 text-right">名称：</label>
            <input type="text" class="form-control-sm col-8" v-model="new_snapshot.name">
          </div>
          <div class="line">
            <label class="col-4">描述：</label>
            <textarea class="form-control col-8" rows="3" v-model="new_snapshot.description"></textarea>
          </div>
        </div>
        <div class="foot w-100 inline-row-end-baseline">
          <button type="button" class="btn btn-sm btn-primary" @click="create_snapshot">拍摄快照</button>
          <button type="button" class="btn btn-sm btn-secondary ml-1" @click="$refs.create_snapshot.hide()">取消</button>
        </div>
      </div>
    </my_modal>
  </div>
</template>

<script type="text/javascript">

  import snapshot_father_node from '@/components/VM/snapshot_father_node';
  import snapshot_children_nodes from '@/components/VM/snapshot_children_nodes';


  export default {
    name: 'snapshot',
    components: {snapshot_father_node, snapshot_children_nodes},
    prop: {
      vm: {
        type: Object,
        required: true,
      }
    },
    data() {
      return {
        modal_background_show: false,
        my_modal_show: false,
        new_snapshot: {
          name: '',
          description: '',
        }
      };
    },
    computed: {},
    methods: {
      create_snapshot() {
        const vm = this;
        vm.$ajax.get('/api/operation_system/snapshot_operation/snapshot', {
          params: {
            config_id: vm.$attrs.vm.configId,
            snapshot_name: vm.new_snapshot.name,
            description: vm.new_snapshot.description,
          },
        }).then(resp => {
          //显示创建成功
          vm.$root.alert.success.push('创建快照成功')

          //重新获取虚机快照
          vm.$emit('load_snapshot');
        }).catch(error => {
          if (error && error.response && error.response.status == 401)
            return
          vm.$root.alert.fail.push(`创建快照失败：${error.response.data.content}`)

        }).finally(() => vm.$refs.create_snapshot.hide());
      },
      delete_snapshot() {
        const vm = this;
        if(vm.$store.state.focus_node.snapshot_id == vm.$store.getters.current_snapshot.snapshot_id){
          vm.$root.alert.fail.push(`不能删除正在使用的快照`)

          return
        }
        vm.$ajax.get('/api/operation_system/snapshot_operation/snapshot_delete', {
          params: {
            snapshot_id: vm.$store.state.focus_node.snapshot_id,
          },
        }).then(resp => {
          //重新获取虚机快照
          vm.$emit('load_snapshot');
        }).catch(error => {
          if (error && error.response && error.response.status == 401)
            return
          vm.$root.alert.fail.push(`删除快照失败：${error.response.data.content}`)

        }).finally();
      },
      go_to_snapshot() {
        const vm = this;
        vm.$ajax.get('/api/operation_system/snapshot_operation/rollback_snapshot', {
          params: {
            vm_id: vm.$attrs.vm.configId,
            current_snapshot: vm.$store.getters.current_snapshot.snapshot_id,
            dest_snapshot: vm.$store.state.focus_node.snapshot_id,
          },
        }).then(resp => {
          //显示转到成功
          //重新获取虚机快照
          vm.$emit('load_snapshot');
        }).catch(error => {
          if (error && error.response && error.response.status == 401)
            return
          vm.$root.alert.fail.push(`转到快照失败：${error.response.data.content}`)

        }).finally();
      }
    },
    beforeCreate() {
      const vm = this;

    }
  }
</script>

<style scoped lang="scss">
  @import "../../assets/sass/base";
  @import "../../../node_modules/bootstrap/dist/css/bootstrap.css"; // todo ： 开发模式的时候引用一下才会有代码提示，但是生产模式要去掉
  .content {
    width: 75%;
    border-radius: 0.3rem;
    padding: 1rem;

    header {
      border-style: solid;
      border-width: 0;
      border-bottom: {
        width: 1px;
        color: #e1e1e1;
      }
      .cancel {
        font-size: 1.5rem;
        &:hover {
          cursor: pointer;
        }
      }
    }

    article {
      margin: 1rem 0;
      padding: 1rem;
      height: 15rem;
      overflow: auto;
      border: {
        radius: 0.3rem;
        style: solid;
        width: 1px;
        color: #e1e1e1;
      }
      background: white;

      .node {
        .self {
          width: 5rem;
          height: 5rem;
          .img {
            width: 3rem;
            height: 3rem;
          }
        }
      }
    }

    footer {
      padding: 1rem 0;
      border: {
        style: solid;
        width: 1px;
        color: #e1e1e1;
      }
      background: #f9f9f9;
      section.left {
        width: 70%;
        .line {
          @extend .inline-row-start-baseline;
          width: 100%;
          label {
            text-align: right;
          }
        }
      }
      section.right {
        width: 30%;
        padding-left: 2rem;
      }
    }

    .create_snapshot {
      padding: 1rem;
      border-radius: 0.3rem;
      width: 20rem;
      background-color: white;
      .head {
        border-style: solid;
        border-width: 0;
        border-bottom: {
          width: 1px;
          color: #e1e1e1;
        }
        .image {
          width: 2rem;
          height: 2rem;
          background: {
            size: contain;
            position: center;
            repeat: no-repeat;
            image: url("/static/img/icon/snapshot.png");
          }
        }
        .cancel {
          font-size: 1.5rem;
          &:hover {
            cursor: pointer;
          }
        }
      }
      .center {
        padding: 1rem 0;
        border-style: solid;
        border-width: 0;
        border-bottom: {
          width: 1px;
          color: #e1e1e1;
        }
        .line {
          @extend .inline-row-start-baseline;
          width: 100%;
          label {
            text-align: right;
          }
        }
      }
      .foot {
        padding-top: 1rem;

      }
    }

  }

</style>

