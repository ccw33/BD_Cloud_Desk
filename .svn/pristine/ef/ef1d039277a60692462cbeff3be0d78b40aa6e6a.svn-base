<template>
  <div class="container-fluid">
    <section class="w-75 inline-row-start-end">
      <i class="fa fa-wifi fa-5x"></i>
      <div class="text">wifi网络 {{wifi.name}} 需要{{wifi.key_type}}密码</div>
    </section>

    <section class="w-75 inline-row-start-baseline mt-3">
      <label for="password" class="w-25">密码：</label>
      <input :type="password_type" class="form-control w-75" id="password"
             placeholder="Password">
    </section>

    <section class="w-75 inline-row-center-baseline justify-content-around mt-3 checkbox">
      <label>
        <input type="checkbox" v-model="pwd_is_show"> 显示密码
      </label>
      <label>
        <input type="checkbox" v-model="wifi.remember_pwd"> 记住该网络
      </label>
    </section>
    <section class="w-75 inline-row-center-baseline justify-content-around mt-3">
      <button type="button" class="btn btn-default btn-xs"> 取消</button>
      <button type="button" class="btn btn-primary btn-xs" @click="submit"> 加入</button>
    </section>
  </div>
</template>

<script>
  import v_tab from '@/components/v_tab';

  export default {
    name: 'wifi_connect_win',
    components: {},
    // prop: {
    //   wifi: {
    //     type: Object,
    //     required: true,
    //     validator: function (value) {
    //       let template = {
    //         name: '别连我dsfasefwagewt',
    //         is_lock: true,
    //         key_type: 'WPA2',
    //         strength: 1,
    //         password: ''};
    //       return utils.validate_template(value,template,'wifi');
    //     }
    //   },
    // },
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
          vm.$root.alert.success.is_show = true;
        }).catch(error => {
          vm.$root.alert.fail.is_show = true;
        })
      }
    },
    mounted() {
      let vm = this;
      // // $.get(`${vm.host}/api/operation_system/get_lans`,
      // //   function (resp) {
      // //     vm.lans = resp;
      // //     vm.lan_data = vm.lans[0];
      // //   });
      //
      // vm.$ajax.get(`${vm.host}/api/operation_system/get_lans`)
      //   .then(resp => {
      //     vm.lans = resp.data;
      //   }).catch(error => {
      //   $('.alert-danger').show();
      // }).finally(() => {
      //   vm.lan_data = vm.lans[0];
      // });
      let kv_list = window.location.search.replace('?', '').split('&');
      for (let index in kv_list) {
        let k = kv_list[index].split('=')[0];
        let v = kv_list[index].split('=')[1];
        if (k == 'is_lock' || k == 'strength' || k == 'remember_pwd') {
          v = JSON.parse(v);
        }
        if (k == 'name') {
          v = decodeURI(v)
        }
        vm.wifi[k] = v;
      }
      if (vm.wifi.remember_pwd) {
        $('#password').val(vm.wifi.password);
      }
    },
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  @import "../assets/sass/base";

  .container-fluid {
    padding: ;
    width: 500px;
    height: 290px;
    margin-top: 15%;
    background: $color-withe;
  }

</style>
