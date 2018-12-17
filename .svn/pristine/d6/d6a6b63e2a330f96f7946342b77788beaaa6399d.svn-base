<template>
  <div class="alert-box">
    <transition enter-active-class="animated bounceInRight"
                leave-active-class="animated bounceOutRight">
      <div v-show="c_alert.success.is_show" class="alert alert-success alert-dismissible" role="alert">
        <button type="button" class="close" aria-label="Close"><span @click="$emit('hide_success')"
                                                                     aria-hidden="true">&times;</span></button>
        <strong>Success!</strong>
        <hr>
        <p>{{c_alert.success.message}}</p>
      </div>
    </transition>

    <transition enter-active-class="animated bounceInRight"
                leave-active-class="animated bounceOutRight">
      <div v-show="c_alert.fail.is_show" class="alert alert-danger alert-dismissible p-2" role="alert">
        <button type="button" class="close" aria-label="Close"><span @click="$emit('hide_fail')"
                                                                     aria-hidden="true">&times;</span></button>
        <strong>Warning!</strong>
        <hr>
        <p>{{c_alert.fail.message}}</p>
      </div>
    </transition>

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
            success: {
              message: '修改配置成功',
              is_show: false,
            },
            fail: {
              message: '修改配置失败',
              is_show: false,
            }
          };
          return utils.validate_template(value,template,'alert')
        }
      },
    },
    data() {
      return {
        success: this.c_alert.success,
        fail: this.c_alert.fail
      }
    }

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
