<template>
  <div class="w-100 h-100 p-3 my-container">
    <bd_head
      :show_switch_type="c_offline_show" @switch_type="offline_show=!offline_show" :switch_type_text="offline_show?'所有虚机':'本地虚机'"
      :show_reload_vm_list="c_vm_show" @reload_vm_list="$refs.vm_list.reload($refs.vm_list)"
      :show_computer_setting="c_vm_show" @computer_setting="vm_show=false"
      :show_reset_pass="true"
      :show_exit="true"
      :show_back="!c_vm_show" @back="vm_show=true"
      :show_shutdown="true"
    ></bd_head>
    <article class="w-100 text-center">
      <h1 class="w-100 text-center">蓝盾云桌面管理系统</h1>
      <computer_setting :button_homes="button_homes"></computer_setting>


      <div class="buttons-vm bd_scroll" v-show="vm_show">
        <div v-show="offline_show">
          <offline style="margin-top: 3rem;"></offline>
        </div>
        <div v-show="!offline_show">
          <vm_list ref="vm_list" v-show="$root.can_connect_network"></vm_list>
          <offline style="margin-top: 3rem;" v-show="!$root.can_connect_network"></offline>
        </div>
      </div>


    </article>
    <bd_foot></bd_foot>


  </div>
</template>

<script>
  import bd_head from '@/common/bd_head';
  import bd_foot from '@/common/bd_foot';
  import computer_setting from '@/common/computer_setting';
  import vm_list from '@/components/VM/vm_list';
  import offline from '@/components/VM/offline';


  export default {
    name: 'HomePage',
    components: {bd_head, bd_foot, computer_setting, vm_list, offline},
    data() {
      return {
        // time: '',
        vm_show: true,
        offline_show:false,
      }
    },
    computed: {
      systemType() {
        this.utils.get_system_typenum()
      },
      button_homes() {
        return !this.vm_show;
      },
      c_vm_show() {
        return this.vm_show;
      },
      c_modalShow() {
        return this.modalShow;
      },
      c_offline_show(){
        return this.vm_show;
      }
    },
    methods: {},
    beforeCreate() {
      const vm = this;
      //获取虚机列表判断能否上网
      vm.$ajax.get('/api/operation_system/can_connect_vm_server', {
        params: {},
      }).then(resp => {
        //能上网
        vm.$root.can_connect_network = true
      }).catch(error => {
        if (error && error.response && error.response.status == 401)
          return
        if (error && error.response && error.response.status == 408) {
          vm.$root.can_connect_network = false;
        }
      });

    },
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  @import "../../assets/sass/base";

  .my-container {
    font-size: 1rem;
    background: {
      image: url("/static/img/HomePage/bg.jpg");
      position: center;
      size: cover;
    }
    header {
      $height: 4em;
      .logo {
        top: 0;
        left: 1em;
        width: $height*2;
        height: $height;
        background: {
          image: url("/static/img/logo/new_logo.png");
          position: center;
          repeat: no-repeat;
          size: contain;
        }
      }
      .buttons {
        top: 0;
        right: 1em;
        //width: $height*0.8*2+3em;
        text-align: right;
        .button {
          display: inline-block;
          width: $height;
          text-align: center;
          .icon {
            width: $height;
            height: $height*0.8;
            margin: 0;
            background: {
              position: center;
              repeat: no-repeat;
              size: contain;
            }
          }
          .text-primary {
            width: 100%;
          }
          &:hover {
            .text-primary {
              color: $color-withe !important;
            }
          }
        }
        .refresh {
          .icon {
            background: {
              image: url("/static/img/later-images-01/yzm_10_01.png");
            }
          }
          &:hover {
            .icon {
              background-image: url("/static/img/later-images-01/yzm_10_02.png");
            }
          }
        }
        .setting {
          .icon {
            background: {
              image: url("/static/img/later-images-01/yzm_06_01.png");
            }
          }
          &:hover {
            .icon {
              background-image: url("/static/img/later-images-01/yzm_06_02.png");
            }
          }
        }
        .reset_pass {
          .icon {
            background: {
              image: url("/static/img/icon/icon_setting.png");
            }
          }
          &:hover {
            .icon {
              background-image: url("/static/img/icon/icon_setting_hover.png");
            }
          }
        }
        .exit {
          .icon {
            background: {
              image: url("/static/img/icon/icon_exit.png");
            }
          }
          &:hover {
            .icon {
              background-image: url("/static/img/icon/icon_exit_hover.png");
            }
          }
        }
        .back {
          .icon {
            background: {
              image: url("/static/img/later-images-01/yzm_07_01.png");
            }
          }
          &:hover {
            .icon {
              background-image: url("/static/img/later-images-01/yzm_07_02.png");
            }
          }
        }
        .shutdown {
          .icon {
            background: {
              image: url("/static/img/later-images-01/yzm_09_01.png");
            }
          }
          &:hover {
            .icon {
              background-image: url("/static/img/later-images-01/yzm_09_02.png");
            }
          }
        }
      }
    }

    article {
      height: 75%;
      h1 {
        margin-top: 1em;
        color: $color-withe-gray;
      }

      .buttons-vm {
        margin: 0 10%;
        height: 90%;
        overflow-y: auto;
        overflow-x: hidden;
      }

    }

  }

</style>
