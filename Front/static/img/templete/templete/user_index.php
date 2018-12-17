<!DOCTYPE html>
<html lang="en">
<head>
<!-- <title><?= Yii::app()->params->user_index_logo ?></title> -->
<meta charset="utf-8">
<meta name="renderer" content="webkit">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<!--可以在收藏夹中显示出图标-->
<link rel="Bookmark" href="favicon.ico" type="image/x-icon"/>
<!--可以在地址栏中显示出图标-->
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon"/>
<link rel="icon" href="favicon.ico" type="image/x-icon"/>
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="renderer" content="webkit|ie-comp|ie-stand">
<link rel="stylesheet" href="public.css"/>
<link rel="stylesheet"  href="dialog.css"/>

<script src="jquery.artDialog.source.js"></script>
<script src="iframeTools.source.js"></script>

<script src="tab.js"></script>
<script src="main.js"></script>

<script src="flexible.debug.js"></script>
<script src="flexible_css.debug.js"></script>

<!--[if lt IE 9]>
<script src="js/html5shiv.min.js"></script>
<script src="js/respond.min.js"></script>
<![endif]-->
</head>

<body>
<div class="page_bg">
<!-- header start-->
<header class="main-header">
    <div class="logo"></div>
    <div class="btn_group">
        <button id="editPassword" type="button" class="btn_operate btn_exit editPassword" link="" action=""><i class="icon_public icon_setting"></i><span>设置</span></button>
        <button type="button" class="btn_operate btn_exit exit cExitSys" link=""><i class="icon_public icon_exit"></i><span>退出</span></button>
    </div>
</header>
<!-- header end-->
<!-- container start-->
<div class="container">
    <div class="l-grid-loading">正在启动中...</div>
    <div class="webname-box"><span class="webname">云桌面</span></div>
    <div class="vm-wrap clearfix" style="display: flex;">
		<ul class="vmlist" style="margin-left: auto;margin-right: auto;">

            <!-- 这里的config_id是接口的configId type是指 这是一个虚拟机还是这个是一个远程桌面 --!>
			<li class="vmlist-item" config_id="" type="">

            <!-- 这里的src是图标路径 -->
                <i class="icon_vmbg"><img class="vmimg" src="" title="" alt="虚拟机" /></i><span class="vm-name"></span>
                <span class="vm-ip"></span>
            </li>         
        </ul>
    </div>

</div>
<!-- container end-->

<div class="editPasswordContainer" style="display:none;"></div>

<!-- footer start-->
<footer class="footer posfix">
    <div class="footer_intro">
        <p>蓝盾信息安全技术股份有限公司&nbsp;&nbsp;版权所有&nbsp;&nbsp;Copyright © 1998-<?= date('Y',time()) ?> Bluedon.All Rights Reserved</p>
    </div>
</footer>
<!-- footer end-->
</div>
<script type="text/javascript">
(function ($) {
    $(document).ready(function() {
        $('.vm-wrap').removeClass('clearfix');

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

        $('.btn_group').delegate('.editPassword', 'click', function () {
            var url = $(this).attr("link");
            $.ajax({
                url:url,
                success:function(re){
                    $('.editPasswordContainer').css('display','block');
                    $('.editPasswordContainer').html(re);
                },
            });

        });

        function timeout(){
            $('.l-grid-loading').css('display','none');
            $.Layer.confirm({
                msg:'登陆已超时,点击确定后自动刷新页面',
                fn:function(){
                    location.reload();
                }
            });
        }

		var is_loading = false;
		function openDesktop(configId) {
			if (!is_loading)
			{
				is_loading = true;
				// 展现动画
                $('.l-grid-loading').html("链接中...");
				$('.l-grid-loading').css('display','block');
                
				var fun = function() {
						// 这里的post第一个参数是终端定义的一个地址
					$.post("",{configId:configId},function(data){
						if(data.sFLgSessionTimeOut !== undefined && data.sFLgSessionTimeOut === true) {
							// 调用接口失败
                            is_loading = false;
                            $('.l-grid-loading').css('display','none');
                            alert('会话超时,请重新登陆');
						} else {
                            /**
                             * 从 OpenStack/GetDesktopInfo 返回的结构为
                             * {
                             *     "errorInfo":"", 错误提示,没有错误就返回success
                             *     "status":"", 虚拟机的状态
                             *     "status_zh":"", 虚拟机的状态的中文解释
                             *     "console":"" 虚拟机的地址
                             * }
                             * 下面的代码的意思为
                             * 如果errorInfo   出现错误信息,就弹框报错
                             *                 不为错误信息,就进入流程
                             * 如果status_zh   ACTIVE 活动中,根据console打开新页面
                             *                 ERROR 虚拟机发生错误,弹框报错
                             *                 BUILD 虚拟机正在启动,提示第一次启动,程序进入递归等待
                             *                 以下这些出现这个最有可能是
                             *                 虚拟机出现资源冲突 或者 没有权限去使用这个虚拟机
                             *                 REBUILD 虚拟机正在重建中, 页面程序进入递归等待
                             *                 SHUTOFF 虚拟机处于关闭状态, 页面程序进入递归等待
                             *                 PAUSED 虚拟机处于暂停状态, 页面程序进入递归等待
                             *                 REBOOT 虚拟机处于重启状态, 页面程序进入递归等待
                             *                 HARD_REBOOT 虚拟机处于硬重启状态, 页面程序进入递归等待
                             */
                            if (data.errorInfo == 'success') {
                                if (data.status == 'BACKUP') {
                                    is_loading =false;
                                    $('.l-grid-loading').html('虚拟机正在做成快照或备份');
                                    setTimeout(function(){
                                        //is_loading = false;
                                        $('.l-grid-loading').css('display','none');
                                    },2000);
                                } else if (data.status != 'ACTIVE' && data.status != 'ERROR') {
                                    var message = {
                                        'BUILD'         : '第一次启动，正在准备桌面...',
                                        'REBUILD'       : '虚拟机正在重建中...',
                                        'SHUTOFF'       : '虚拟机处于关闭状态, 正在启动中...',
                                        'PAUSED'        : '虚拟机处于暂停状态, 正在恢复中...',
                                        'REBOOT'        : '虚拟机正在重启中...',
                                        'HARD_REBOOT'   : '虚拟机正在硬重启中...',
                                    };
                                    $('.l-grid-loading').css('display','block');
                                    $('.l-grid-loading').html(message[data.status]);
                                    setTimeout(fun, 500);
                                } else {
                                    // 隐藏动画
                                    is_loading = false;
                                    if (data.status == 'ACTIVE') {
                                        $('.l-grid-loading').html("准备打开桌面...");
                                        $('.l-grid-loading').css('display','none');
                                        var win = window.open("../" + data.console, "desktop" + configId);
                                        // win.focus();
                                    } else {
                                        alert("启动桌面失败"+"status:"+data.status+"/status_zh:"+data.status_zh);
                                    }
                                    $('.l-grid-loading').css('display','none');
                                }
						    } else {
                                is_loading = false;
                                $('.l-grid-loading').html(data.errorInfo + '...');
                                setTimeout(function(){
                                    //is_loading = false;
                                    $('.l-grid-loading').css('display','none');
                                },2000);
                            }
                        }
					},'json');
				};
				fun();
			}
		}

        var elements = document.getElementsByClassName('vmlist-item');
        for (var i = 0; i < elements.length; i++) {
            var limit = false
            elements[i].ondblclick = function(){
                    // // 限制:不能同时开启两个虚机
				var configId = $(this).attr('config_id');
                var type = $(this).attr('type');

                if(type == <?= TbGroupVm::TYPE['CONFIG'] ?>){
                    openDesktop(configId);
                }else if(type == <?= TbGroupVm::TYPE['REMOTE_DESKTOP'] ?>){
                    $('.l-grid-loading').html("准备连接远程桌面");
                    $('.l-grid-loading').css('display','block');
                    $.post("<?= $this->createUrl('OpenStack/GetRemoteDesktop') ?>",{configId:configId},function(data){
                        if(data.status == true){
                            $('.l-grid-loading').html('正在打开远程桌面');
                            $('.l-grid-loading').css('display','none');
                            window.open('../' + data.console,'remote_desktop' + configId);
                        }else{
                            $('.l-grid-loading').html('打开远程桌面失败');
                            $('.l-grid-loading').css('display','none');
                            alert(data.message);
                        }
                    },'json');
                }
					
				return;
            };
            
        }
    });

})(jQuery);
</script>
</body>
</html>
