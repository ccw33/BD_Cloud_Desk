<template>
  <div class="container-fluid">
    <header class="w-100 position-relative">
      <h6 class="position-absolute">连接网络</h6>
      <div class="text-muted position-absolute"
           @click="$emit('cancel')">×
      </div>
    </header>
    <article>
      <div class="title">
        <div class="icon"></div>
        <div class="text">wifi网络 {{wifi.name}} 需要{{wifi.key_type}}密码</div>
      </div>
      <form action="">
        <section class="password">
          <label for="password">密码：</label>
          <input :type="password_type" class="form-control" id="password"
                 placeholder="Password">
        </section>

        <section class="checkboxs">
          <label>
            <input type="checkbox" v-model="pwd_is_show"> 显示密码
          </label>
          <label>
            <input type="checkbox" v-model="wifi.remember_pwd"> 记住该网络
          </label>
        </section>
      </form>
    </article>
    <footer>
      <button type="button" class="btn btn-default btn-sm" @click="$emit('cancel')"> 取消</button>
      <button type="button" class="btn btn-primary btn-sm" @click="submit"> 加入</button>
    </footer>
  </div>
</template>

<script>
  import v_tab from '@/components/v_tab';
  import utils from "../utils";

  export default {
    name: 'wifi_connect_win',
    components: {},
    prop: {
      prop_wifi: {
        type: Object,
        required: true,
        validator: function (value) {
          let template = {
            name: '别连我dsfasefwagewt',
            is_lock: true,
            key_type: 'WPA2',
            strength: 1,
            password: ''
          };
          return utils.validate_template(value, template, 'wifi');
        }
      },
    },
    data() {
      return {
        wifi: {
          name: '',
          is_lock: true,
          key_type: '',
          strength: 0,
          password: '',
          remember_pwd: false,
        },
        pwd_is_show: false,

        alert: {
          success: {
            message: '连接wifi成功',
            is_show: false,
          },
          fail: {
            message: '连接wifi失败',
            is_show: false,
          }
        }
      }
    },
    computed: {
      password_type() {
        return this.pwd_is_show ? 'text' : 'password'
      }
    },
    methods: {
      submit() {
        const vm = this;
        vm.wifi.password = $('#password').val();
        vm.$ajax.post(
          `${vm.host}/api/operation_system/connect_wifi`,
          vm.$qs.stringify(vm.wifi),
        ).then(resp => {
          vm.$root.alert.success.message = `连接wifi${vm.wifi.name}成功`;
          vm.$root.alert.success.is_show = true;
          vm.$emit('cancel');
        }).catch(error => {
          vm.$root.alert.fail.message = `连接wifi${vm.wifi.name}失败`;
          vm.$root.alert.fail.is_show = true;
        })
      }
    },
    mounted() {
      let vm = this;
      vm.wifi = vm.$attrs.prop_wifi;
    },
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  @import "../assets/sass/base";

  .container-fluid {
    font-size: 1rem;
    padding: 0 0 1em 0;
    width: 500px;
    /*height: 290px;*/
    margin-top: 15%;
    background: $color-withe;
    border-radius: 0.5em;

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
    article {
      .title {
        width: 100%;
        position: relative;
        height: 70px;
        .icon {
          position: absolute;
          left: 72px;
          top: 24px;
          width: 46px;
          height: 46px;
          background: {
            position: center;
            repeat: no-repeat;
            size: contain;
            image: url("/static/img/later-images-01/yzm_41.png");
          }
        }
        .text {
          position: absolute;
          top: 40px;
          left: 128px;
        }
      }

      form {
        .password {
          position: relative;
          width: 100%;
          height: 28px;
          margin-top: 22px;
          margin-bottom: 14px;
          label {
            position: absolute;
            top: 2px;
            right: 330px;
          }
          input {
            position: absolute;
            width: 230px;
            height: 28px;
            top: 0;
            right: 100px;
          }
        }
        .checkboxs {
          width: 100%;
          padding-left: 170px;
          text-align: left;
          label {
            margin-right: 1em;
          }
        }
      }

    }
    footer {
      margin-top: 2em;
      width: 100%;
      text-align: right;
      button {
        margin-right: 20px;
      }
    }
  }

</style>
