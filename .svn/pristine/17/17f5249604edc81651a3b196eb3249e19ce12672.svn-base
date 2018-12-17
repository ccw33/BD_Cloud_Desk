(function ($) {
    var tabs = {},tabsId=[];
    $(document).ready(function () {
        
        $('.menu').delegate('li a', 'click', function () {
			if (!$(this).attr("link")) {
				return false;
			} else {

				addTab({//调用addTab函数，传title和url的参数
					title: $(this).text(),

					url: $(this).attr('link')
				});
			}
           

        });

		/**点击头部导航菜单显示左侧二级菜单**/
		$('.bigmenu ul li').click(function(){
			var _index = $(this).index();
			$('.bigmenu ul li a').removeClass('curent');
			$(this).children().addClass('curent');
			//$('.menu').addClass('show-second-menu');
			$('.menu ul').removeClass('second-menu');
			if((_index-1 >= 0) && ($('.menu>ul>li').eq(_index-1).children('ul').length > 0)){
				$('.container').removeClass('hide-left-menu');
				$('.menu>ul>li').eq(_index-1).children('ul').addClass('second-menu');

				$('.second-menu li a').each(function () {
					if ($(this).attr('link')) {
						addTab({//调用addTab函数，传title和url的参数
							title: $(this).text(),
							url: $(this).attr('link')
						});
						return false;
					}
					addScroll();
				});
			}else{
				$('.container').addClass('hide-left-menu');
			}

		});


		$('.font-weight td a').click(function(){
			 
			if (!$(this).attr("link")) {
				return false;
			} else {
				
				parent.addTab({//调用addTab函数，传title和url的参数
					title: $(this).text(),

					url: $(this).attr('link')
				});
				
			}
        });
		
		$('.m_title a').click(function(){
			 
			if (!$(this).attr("link")) {
				return false;
			} else {
				
				parent.addTab({//调用addTab函数，传title和url的参数
					title: $(this).text(),

					url: $(this).attr('link')
				});
				
			}
        });
		

        $('#tabs').delegate('a.tab', 'click', function (e) {
            // 隐藏所有tab和iframe
            $("#tabs li").removeClass("current");
            $("#content iframe").hide();

            // 显示点击的tab及iframe
            $(this).parent().addClass("current");
            var contentname = $(this).attr("id") + "_content";
            $("#" + contentname).show();
			$("#" + contentname).attr('src', $("#" + contentname).attr('src'));
            

        });
        $('#tabs').delegate('a.remove', 'click', function (e) {
            var me = e.currentTarget;
            var id = $(me).attr('pid');
            var src = $("#" + id + "_content").attr('src');
            delete tabs[src];
            var cur = $('#' + id).parent().prev();
            $('#' + id).parent().remove();

            if ($("#tabs li.current").length == 0 && $("#tabs li").length > 0) {

                cur.addClass("current");
                var hid = cur.find('a.tab').attr('id');
                $("#" + hid + "_content").show();
            }
        });

		addTab({
            title: '系统主页',
            close: false,
            url: $('body').attr('sUrl')
        });
		


    });
	//防火墙接口
	function showErerima(obj,a,b,c){
			$(".ererima_img").remove();
			var _imgLeft = obj.offset().left-77;
			var _imgTop = obj.offset().top;
			var _bodyWd =parseInt($(document.body).width());
			var _height,h1,_imgRight;
			//alert(_imgTop);
			/*var _html = '';
			_html+='<div class="ererima_img">';
			_html+='<table width="100%" height="30" border="0" cellspacing="0" cellpadding="0">';
			_html+='<tr>';
			_html+='<th>网口</th>';
			_html+='<td>'+wk+'</td>';
			_html+='</tr>';
			_html+='<tr>';
			_html+='<th>状态</th>';
			_html+='<td class="green">'+zt+'</td>';
			_html+='</tr>';
			_html+='<tr>';
			_html+='<th>IP地址</th>';
			_html+='<td>'+ip+'</td>';
			_html+='</tr>';
			_html+='<tr>';
			_html+='<th>掩码</th>';
			_html+='<td>'+yan+'</td>';
			_html+='</tr>';
			_html+='</table>';
			_html+='</div>';*/
			var _html = '';
			_html+='<div class="ererima_img">';
			_html+='<table width="100%" height="30" border="0" cellspacing="0" cellpadding="0">';
			_html+='<tr>';
			_html+='<th>网口：</th>';
			_html+='<td>'+a+'</td>';
			_html+='</tr>';
			_html+='<tr>';
			_html+='<th>IP地址：</th>';
			_html+='<td>'+b+'</td>';
			_html+='</tr>';
			_html+='<tr>';
			_html+='<th>掩码：</th>';
			_html+='<td>'+c+'</td>';
			_html+='</tr>';
			_html+='</table>';
			_html+='<div class="arrow"></div>';
			_html+='</div>';
			$(document.body).append(_html);
			h1 = parseInt($(".ererima_img").height());
			_height = _imgTop-h1 -4;
			_imgRight = _bodyWd - _imgLeft;
			if(_imgRight<160){
				$(".ererima_img").css({top:_height+"px",right:0+"px"});
			}else{
				$(".ererima_img").css({top:_height+"px",left:_imgLeft+"px"});	
			}
			
	}

    function addTab(obj) {
        // hide other tabs

        var iframeId = tabs[obj.url];
        if (iframeId) {
            $("#tabs li").removeClass("current");
            $("#content iframe").hide();
            $("#" + iframeId).parent().addClass("current");
            $("#" + iframeId+'_content').show();
			$("#" + iframeId+'_content').attr('src', $("#" + iframeId+'_content').attr('src'));
            return
        }
        var tabs_num = $("#tabs li").length;
        if (tabs_num > 7) {
          //清掉第二个tab
            var sendTab = tabsId.splice(1,1);
           var id = sendTab[0];
            var src = $("#" + id + "_content").attr('src');
            delete tabs[src];
            var cur = $('#' + id).parent().prev();
            $('#' + id).parent().remove();
        }
		
        $("#tabs li").removeClass("current");
        $("#content iframe").hide();

            var tick = new Date().getTime(), close = '';
            obj.close = obj.close !== false ? true : false;
            // add new tab and related content
            if (obj.close) {
                close = "<a href='javascript:void(0)' class='remove' pid='tab_" + tick + "'></a>";
            }
            $("#tabs").append("<li class='current'><a class='tab' id='tab_" + tick + "' href='javascript:void(0)'>" + obj.title +
            "</a>" + close + "</li>");

            tabs[obj.url] = 'tab_' + tick;
            $("#content").append("<iframe  id='tab_" + tick + "_content' name='right' frameborder='0' src='" + obj.url + "'  scrolling='auto' ></iframe>");
            // set the newly added tab as current
            $("#tab_" + tick + "_content").show();
        tabsId.push('tab_' + tick );
		//console.log(iframeId)
		parent.addTab=addTab

    }
})(jQuery);