<template>
  <div class="modal_background inline-row-center-center " :style="{ display:background_show }">
    <transition enter-active-class="animated fadeInDown" leave-active-class="animated fadeOutUp">
      <div class="inline-row-center-center w-100" v-if="my_modal_show">
        <slot></slot>
      </div>
    </transition>
  </div>

</template>

<script type="text/javascript">

  export default {
    name: 'my_modal',
    components: {},
    data() {
      return {
        modal_background_show: false,
        my_modal_show: false,
      };
    },
    created: function () {

    },
    computed: {
      background_show(){
        return this.modal_background_show?'':'none !important'
      }
    },
    methods: {
      show() {
        this.modal_background_show = true;
        this.my_modal_show = true;
      },
      hide() {
        this.my_modal_show = false;
        window.setTimeout(() => this.modal_background_show = false, 500)
      },
    },
    mounted() {
    }
  }
</script>

<style scoped lang="scss">
  @import "../assets/sass/base";

  .modal_background {
    width: 100%;
    height: 100%;
    background-color: rgba(0.3, 0.3, 0.3, 0.3);
    position: fixed;
    z-index: 999;
    left: 0;
    top: 0;
  }
</style>

