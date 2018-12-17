<template>
  <div class="my-container w-100 d-inline-flex flex-column justify-content-center align-items-center">
    <h2 class="title">创建{{ conf.logo_name }}账号</h2>
    <form class="d-inline-flex flex-column justify-content-center align-items-center">
      <div id="account" class="form-group">
        <label>用户名：</label>
        <input type="text" class="form-control"
               :class="{'is-invalid':form.account.is_invalid}"
               placeholder="请输入用户名" v-model="form.account.val"
               required>
        <div class="invalid-feedback">
          {{ form.account.help_text }}
        </div>
      </div>
      <div id="password" class="form-group">
        <label>密码：</label>
        <input type="password" class="form-control"
               :class="{'is-invalid':form.password.is_invalid}"
               placeholder="请输入6位以上包含英文字符与数字的密码" v-model="form.password.val"
               required>
        <div class="invalid-feedback">
          {{ form.password.help_text }}
        </div>
      </div>
      <div id="re_password" class="form-group">
        <label>重输密码：</label>
        <input type="password" class="form-control"
               :class="{'is-invalid':form.re_password.is_invalid}"
               placeholder="请重新输入密码" v-model="form.re_password.val"
               required>
        <div class="invalid-feedback">
          {{ form.re_password.help_text }}
        </div>
      </div>
      <div id="email" class="form-group">
        <label>邮箱：</label>
        <input type="text" class="form-control"
               :class="{'is-invalid':form.email.is_invalid}"
               placeholder="请输入邮箱" v-model="form.email.val"
               required>
        <div class="invalid-feedback">
          {{ form.email.help_text }}
        </div>
      </div>
    </form>
    <button id="submit" type="button" class="btn-info">注册</button>
  </div>
</template>

<script>

  // $('.carousel').carousel({
  //   pause:true,
  // });
  export default {
    name: 'SignIn',
    components: {},
    data() {
      return {
        form: {
          account: {
            val: '',
            type: 'account',
            is_invalid: false,
            help_text: '此用户名已被使用',
          },
          password: {
            val: '',
            is_invalid: false,
            help_text: '请输入6位以上包含英文字符与数字的密码',
          },
          re_password: {
            val: '',
            is_invalid: false,
            help_text: '密码不相同',
          },
          email: {
            val: '',
            is_invalid: false,
            help_text: '邮箱格式不正确',
          }
        }
      }
    },
    computed: {},
    methods: {},
    beforeCreate() {
      let vm = this;
      // // $.get(`${vm.host}/get_lans`,
      // //   function (resp) {
      // //     vm.lans = resp;
      // //     vm.lan_data = vm.lans[0];
      // //   });
      //
      // vm.$ajax.get(`${vm.host}/get_lans`)
      //   .then(resp => {
      //     vm.lans = resp.data;
      //   }).catch(error => {
      //   $('.alert-danger').show();
      // }).finally(() => {
      //   vm.lan_data = vm.lans[0];
      // });
    },
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  @import "../../assets/sass/base";

  .my-container {
    /*font-family: 'HanyiSentyChalk';*/
    font-size: 1.3rem;
    @media all and (max-width: $phone-max-portrait-width) {
      font-size: 1rem;
    }
    .title {
      margin: 1.5em 0;
    }
    form {
      label, input {
        margin-right: 0.5em;
      }
      label {
        width: 6em;
        text-align: right;
      }
      input {
        width: 25em;
        @media all and (max-width: $phone-max-portrait-width) {
          width: 10em;
        }
      }
      .invalid-feedback {
        width: 10em;
      }
      .form-group {
        @extend .d-inline-flex;
        @extend .flex-row;
        @extend .justify-content-center;
        @extend .align-items-baseline;
        @extend .flex-wrap;
        margin: 0.3em 0;
        .invalid-feedback {
          font-size: 0.6em;
        }
      }
    }

    #submit {
      width: 25em;
      margin-left: 2em;
      @media all and (max-width: $phone-max-portrait-width) {
        margin-left: 0;
        width: 15em;
      }
      margin-top: 1em;
      -webkit-border-radius: 0.2em;
      -moz-border-radius: 0.2em;
      border-radius: 0.2em;
    }

  }


</style>
