<template>
  <div class="alert-box">
    <template v-for="success,index in c_alert.success.messages">
      <transition leave-active-class="animated bounceOutRight">
        <div v-show="success.is_show" class="alert alert-success alert-dismissible animated bounceInRight" role="alert">
          <button type="button" class="close" aria-label="Close"><span @click="$emit('hide_success',index)"
                                                                       aria-hidden="true">&times;</span></button>
          <strong>Success!</strong>
          <hr>
          <p>{{ success.message }}</p>
        </div>
      </transition>
    </template>

    <template v-for="fail,index in c_alert.fail.messages" >
      <transition leave-active-class="animated bounceOutRight">
        <div v-show="fail.is_show" class="alert alert-danger alert-dismissible p-2 animated bounceInRight" role="alert">
          <button type="button" class="close" aria-label="Close"><span @click="$emit('hide_fail',index)"
                                                                       aria-hidden="true">&times;</span></button>
          <strong>Warning!</strong>
          <hr>
          <p>{{ fail.message }}</p>
        </div>
      </transition>
    </template>

  </div>
</template>

<script>
  import utils from "../utils";

  export default {
    name: "v_alert",
    props: {
      c_alert: {
        type: Object,
        required: true,
        validator(value) {
          let template = {
            success: {},
            fail: {}
          };
          return utils.validate_template(value, template, 'alert')
        }
      },
    },

  }
</script>

<style scoped lang="scss">
  .alert-box {
    position: absolute;
    right: 3rem;
    top: 10rem;
    z-index: 9999;
    min-width: 8rem;
    #get_setting_fail, #change_setting_failed, #change_setting_succeed {
      display: none;
    }
  }


</style>
