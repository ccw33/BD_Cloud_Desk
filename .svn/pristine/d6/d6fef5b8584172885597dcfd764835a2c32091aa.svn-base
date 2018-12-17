<template>
  <div class="ip-setting-container">
    <header class="w-100 position-relative">
      <h6 class="position-absolute" style="">网络设置</h6>
      <div class="text-muted position-absolute"
           @click="$emit('close_ip_setting')">×
      </div>
    </header>
    <div class="content">

      <b-nav tabs>
        <b-nav-item v-for="(item, index) in lans"
                    :key="item.lan"
                    @click="activate(index)"
                    :active="item.isActive">{{ item.lan }}</b-nav-item>
      </b-nav>
      <template v-for="(lan, index)  in lans">
        <!--<transition enter-active-class="animated bounce">-->
        <template v-if="lan.isActive">    <!-- 保证v_lan组件在获取lan_data之后再渲染 -->
          <!--<keep-alive>-->
          <ip_setting_tab :lan_data="lans[index]" :key="lan.id" :index="index"></ip_setting_tab>
          <!--</keep-alive>-->
        </template>
        <!--</transition>-->
      </template>
    </div>
  </div>
</template>

<script>
  import ip_setting_tab from '@/components/System/ip_setting_tab';
  import Vuex from 'vuex'

  const store = new Vuex.Store({
    state: {
      old_data_list: []
    },
    mutations: {
      initial_old_data(state, old_data_list) {
        state.old_data_list = old_data_list;
      }
    },
    getters: {
      get_old_data: (state) => (index) => state.old_data_list[index]
    }
  });

  export default {
    name: 'ip_setting',
    store: store,
    components: {ip_setting_tab},
    data() {
      return {
        lans: [
          {
            'lan': '',
            'isActive': true,
            'is_auto': false,
            'id': '',
            'ip': '',
            'subnet_mask': '',
            'gateway': '',
            'dns': '',
            'mac': ''
          },
          {
            'lan': '',
            'id': '',
            'isActive': false,
            'is_auto': false,
            'ip': '',
            'subnet_mask': '',
            'gateway': '',
            'dns': '',
            'mac': ''
          },
        ],
        alert: {
          success: {
            message: '',
            is_show: false,
          },
          fail: {
            message: '获取配置失败',
            is_show: false,
          }
        }
      }
    },
    methods: {
      activate(index) {
        this.lans.forEach((item, index, arr) => {
          item.isActive = false;
        });
        this.lans[index].isActive = true;
      },
    },
    beforeCreate() {
      let vm = this;
      vm.$ajax.get(`${vm.host}/api/operation_system/get_lans`)
        .then(resp => {
          vm.lans = resp.data.result;
          vm.$store.commit('initial_old_data', vm.utils.copy(vm.lans));
        }).catch(error => {
        vm.$root.alert.fail.message = '获取网络配置失败'
        vm.$root.alert.fail.is_show = true;
      });
    },
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  @import "../../assets/sass/base";

  .ip-setting-container {
    width: 100%;
    /*height: 100%;*/
    border-radius: 0.5em;
    background-color: $color-withe;

    header {
      height: 46px;
      h6 {
        line-height: 46px;
        top: 0;
        left: 1rem;
      }
      div {
        line-height: 46px;
        top: 0;
        right: 1rem;
        font-size: 2rem;
        color: $primary;
        &:hover {
          font-weight: bold;
          cursor: pointer;
        }
      }
    }
    .content {
      ul, li, a {
        height: 40px;
        a {
          /*width: 100px;*/
        }
      }

    }
  }

</style>
