<template>
  <!--<transition enter-active-class="animated fadeIn"-->
  <!--leave-active-class="animated fadeOut">-->
  <div v-if="is_loading" class="loading-container w-100 h-100 text-center">
    <slot>
      <h3 style="padding-top: 25%">{{ loading_text }}</h3>
      <slot name="after_spinner"></slot>
    </slot>
  </div>

  <!--</transition>-->
</template>

<script>
  import spinner from '@/common/spinner';
  // $('.carousel').carousel({
  //   pause:true,
  // });
  export default {
    name: 'loading',
    props: {
      is_loading: Boolean,
    },
    data() {
      return {
        init_loading_text: 'LOADING',
        loading_text: 'LOADING',
      }
    },
    components: {spinner},
    methods: {},
    mounted() {
      const vm = this;
      let i = 0;
      window.setInterval(() => {
        if (i < 3) {
          vm.loading_text = vm.loading_text + '.'
          i++;
        } else {
          vm.loading_text = vm.init_loading_text;
          i = 0;
        }

      }, 1000)
    },
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

  .loading-container {
    background-color: rgba(0.3, 0.3, 0.3, 0.3);
    /*width: 10em;*/
    /*height: 4em;*/
    position: fixed;
    z-index: 9999;
    left: 0;
    top: 0;
    color: $color-withe-gray;
  }


</style>
