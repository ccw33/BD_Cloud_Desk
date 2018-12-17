export default {
  validate_template(value, template, name = 'object') {
    for (let key in template) {
      if (value.hasOwnProperty(key)) {
        //如果是一个对象则递归验证
        if (typeof(template[key]) === 'object') {
          if (!this.validate_template(value[key], template[key], `${name}.${key}`)) {
            return false
          }
        } else {
          //判断是不是对应的类型
          if (!(typeof(value[key]) === typeof(template[key]))) {
            console.error(`${name}.${key} 的类型应该是 ${typeof(template[key])} 而不是 ${typeof(value[key])} `);
            return false
          }
        }
      } else {
        console.error(`缺少 ${name}.${key} `);
        return false;
      }
    }
    return true;
  },


  // 对象复制方法，包括数组
  copy(obj) {
    if (!(obj instanceof Object)) {
      return obj;
    }
    if (obj instanceof Array) {
      let newobj = Array(obj.length);
      for (let index in obj) {
        newobj[index] = this.copy(obj[index])
      }
      return newobj;
    } else {
      let newobj = {};
      for (var attr in obj) {
        newobj[attr] = this.copy(obj[attr]);
      }
      return newobj;
    }
  },

  //页面缓慢移动到指定位置
  slowly_scroll_to(selector, time = 800) {
    $('html,body').animate({scrollTop: $(selector).offset().top}, time)
  },

//写cookies

  setCookie(name, value) {
    var Days = 30;
    var exp = new Date();
    exp.setTime(exp.getTime() + Days * 24 * 60 * 60 * 1000);
    document.cookie = name + "=" + escape(value) + ";expires=" + exp.toGMTString();
  },

//读取cookies
  getCookie(name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");

    if (arr = document.cookie.match(reg))

      return unescape(arr[2]);
    else
      return null;
  },

//删除cookies
  delCookie(name) {
    var exp = new Date();
    exp.setTime(exp.getTime() - 1);
    var cval = getCookie(name);
    if (cval != null)
      document.cookie = name + "=" + cval + ";expires=" + exp.toGMTString();
  },

  get_system_type() {
    let ua = navigator.userAgent;
    if (ua.match('Windows'))
      return 'windows'
    if (ua.match('Linux'))
      return 'linux'
    if (ua.match('iPhone'))
      return 'iphone'
    if (ua.match('Mac'))
      return 'ios'
    if (ua.match('Android'))
      return 'android'
  }
  ,


//---------------项目特有-----------------
  get_system_typenum() {
    let ua = navigator.userAgent;
    if (ua.match('Windows'))
      return 3
    if (ua.match('Linux'))
      return 2
    if (ua.match('iPhone') || ua.match('Mac'))
      return 'iphone'
    if (ua.match('Mac'))
      return 4
    if (ua.match('Android'))
      return 5
  }
  ,

}
