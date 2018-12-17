<template>
  <div class="my-container w-100">
    <!--<header class="w-100 d-inline-flex flex-row justify-content-between align-items-baseline flex-nowrap">-->
      <!--<logo class="logo"></logo>-->
      <!--<div class="link">-->
        <!--<router-link :to="{name:'Login',params:{type:'login'}}">登录</router-link>-->
        <!--<router-link :to="{name:'SignIn'}">注册</router-link>-->
      <!--</div>-->
    <!--</header>-->
    <my_header></my_header>

    <section class="content">
      <router-view></router-view>
    </section>
    <footer class="w-100"></footer>

  </div>
</template>

<script>

  // import logo from '@/common/logo';
  import my_header from '@/common/my_header';

  export default {
    name: 'Account',
    components: {my_header},
    data() {
      return {
        lans: [
          {
            'lan': '',
            'isActive': true,
            'is_auto': false,
            'ip': '',
            'subnet_mask': '',
            'gateway': '',
            'DNS': ''
          },
        ],
        lan_data: ''
      }
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
  @import "../../assets/sass/base";
  .my-container {
    font-size: 1rem;
/*    header {
      .logo {
        font-size: 2em;
      }
      .link {
        a {
          margin-right: 1em;
          color: $color-complement-3;
        }
      }
    }*/
    section.content{
      margin:2em 0;
    }

  }

</style>
