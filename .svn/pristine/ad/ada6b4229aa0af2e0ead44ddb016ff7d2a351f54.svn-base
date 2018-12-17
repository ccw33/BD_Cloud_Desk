(function ($) {
$(document).ready(function () {

//左菜单开始
    $(".menu>ul li a ").click(function() {
        $(".menu>ul li a p").removeClass("aselec");
        $(".sel").removeClass()
        $(this).children("p").addClass("aselec");
    })
    $(".menu ul li ul ").each(function() {
        $(this).first('li').css("border-top","none")
    });
    $(".menu ul li:has(ul)").find("ul").hide();
    $(".menu ul li:has(ul) a").click(function(){
        if($(this).siblings().is(':hidden')){
            $(this).children('.menu_s').css("background-position","0px -8px");
            $(this).children('.menu_s').css("width","7px");
            $(this).children('.menu_s').css("height","4px");
            $(this).siblings().show()
        }else{
            $(this).children('.menu_s').css("background-position","0px 0px");
            $(this).children('.menu_s').css("width","4px");
            $(this).children('.menu_s').css("height","7px");
            $(this).siblings().hide()

        }
    });
    $(".menu>ul>li>ul>li").hover(function(){
        $(this).siblings().removeClass("twoli");
        $(this).toggleClass("twoli");
    });

    $(".menu>ul>li>ul>li>ul").hover(function(){
        $(this).parents("li").toggleClass("twoli");
        $(this).parents("li").toggleClass("hower");
        $(this).siblings("a").removeClass("sel");
    });
    $(".menu ul li ul li a").click(function(){
        $(".sel").removeClass();
        $(".hower").removeClass();
        $(this).addClass("sel").parents().siblings().removeClass("sel");
    });

//隐藏显示左菜单
    $(".l_icon").click(function(){
        //隐藏左菜单
        if($(".menu").is(":visible")){
            $(".menu").hide()
            $(".menu").css("left","-200px")
            $(".left_h").css("left","2px")
            $(".content").css("left","10px")
            $(".hidden_i").removeClass()
            $(this).addClass("display_i");
            $(this).addClass("l_icon")
        }else{   //显示左菜单
            $(".menu").show()
            $(".menu").css("left","0px")
            $(".left_h").css("left","222px")
            $(".content").css("left","230px")
            $(".display_i").removeClass()
            $(this).addClass("hidden_i");
            $(this).addClass("l_icon")
        }
    });

//隐藏显示右上角菜单（告警、主页、账户）
    $(".xxts").hide();
    $(".warning").click(function(){
        if($(this).hasClass("minM_sel_w")){
            $(this).addClass("warning");
        }else{
            $(this).removeClass("warning");
        }
        $(this).toggleClass("minM_sel_w");
        $("#user").hide();
        $("#warnning").toggle();
        $(".minM_sel_u").removeClass().addClass("user");
        $(".minM_sel_h").removeClass().addClass("home");

    });

    $(".user").click(function(){
        if($(this).hasClass("minM_sel_u")){
            $(this).addClass("user");
        }else{
            $(this).removeClass("user");
        }
        $(this).toggleClass("minM_sel_u");

        $("#warnning").hide();
        $("#user").toggle();
        $(".minM_sel_w").removeClass().addClass("warning");
        $(".minM_sel_h").removeClass().addClass("home");
    });

    $(".home").click(function(){
        if($(this).hasClass("minM_sel_h")){
            $(this).addClass("home");
        }else{
            $(this).removeClass("home");
        }
        $(this).toggleClass("minM_sel_h");

        addTab($(this).children('a'));
        $("#warnning").hide();
        $("#user").hide();
        $(".minM_sel_w").removeClass().addClass("warning");
        $(".minM_sel_u").removeClass().addClass("user");
    });

    $(".xxts li").click(function(){
        addTab($(this).children('a'));
        $(".xxts").hide();
        $(".minM_sel_w").removeClass().addClass("warning");
        $(".minM_sel_u").removeClass().addClass("user");

    })

    //function Al(content){
    //    $.Layer.notice({
    //        content:'测试测试',
    //        time:3
    //    })
    //}
    function Al(content){
        $.ajax({
            url: $.PhpUrl('Alertlog/Screenalert'),
            type: 'POST',
            dataType: 'json',
            //data: {id: data.id, istatus: data.istatus},
            success:function(json){
                if(json.msg==1){
                    $.Layer.notice({
                        content:'新增高级风险日志'+json.high+'条<br/>'+'新增中级风险日志'+json.middle+'条<br/>'+'新增低级风险日志'+json.low+'条',
                        time:10,
                        cancelVal : null,
                        close:function(a,b,c){
                            console.log(a,b,c);return;
                            $.ajax({
                                url: $.PhpUrl('Alertlog/Delscreeninfo'),
                                type: 'POST'
                            });
                        }
                    })
                }
                //grid.loadData();
            }
        });
    }
    //setTimeout(Al,1000);
    //setInterval(Al,3000);

	//退出系统
	$('.bigmenu').delegate('.cExitSys', 'click', function () {
		var url = $(this).attr("link");
		$.Layer.confirm({
			msg: '是否要退出系统？', fn: function () {
				$.ajax({
					url: url,
					dataType: 'json',
					success: function (d) {
						if (d.success == false) {
							$.Layer.alert({title: '系统友情提示', msg: d.msg, fn: function () {

							}});
						} else {

							window.location.reload();
						}

					}
				});

			}
		});

	});

    $('.btn_group').delegate('.cExitSys', 'click', function () {
        var url = $(this).attr("link");
        $.Layer.confirm({
            msg: '是否要退出系统？', fn: function () {
                $.ajax({
                    url: url,
                    dataType: 'json',
                    success: function (d) {
                        if (d.success == false) {
                            $.Layer.alert({title: '系统友情提示', msg: d.msg, fn: function () {
                            }});
                        } else {
                            window.location.reload();
                        }
                    }
                });
            }
        });
    });

})
})(jQuery);