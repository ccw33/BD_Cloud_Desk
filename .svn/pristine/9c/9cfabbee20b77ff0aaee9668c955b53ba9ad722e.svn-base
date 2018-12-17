<template>
  <header class="w-100 d-inline-flex flex-row justify-content-between align-items-baseline flex-nowrap">
    <logo class="logo"></logo>
    <div class="link">
      <router-link :to="{name:'Login' }">登录</router-link>
      <router-link :to="{name:'SignIn'}">注册</router-link>
    </div>
  </header>
</template>

<script>
  import logo from '@/common/logo';

  // $('.carousel').carousel({
  //   pause:true,
  // });
  export default {
    name: 'my-header',
    components: {logo},
    data() {
      return {}
    },
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
  @import "../assets/sass/base";

  header {
    font-size: 1rem;

    .logo {
      font-size: 2em;
    }
    .link {
      font-family: $font-family-base;
      a {
        margin-right: 1em;
        color: $color-complement-3;
      }
    }
  }

</style>
