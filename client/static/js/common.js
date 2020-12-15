$(document).ready(function () {
    //检测ie 6789
    if (!(/msie [6|7|8|9]/i.test(navigator.userAgent))) {
        window.scrollReveal = new scrollReveal({
            reset: true
        });
    }
    // 弹窗回复评论
    var list = document.getElementsByClassName('replyComment');
    for (var i of list) {
        i.addEventListener("click", function (ev) {
            ev.preventDefault();
            var txt=  "请输入回复：";
            window.wxc.xcConfirm(txt, window.wxc.xcConfirm.typeEnum.input,{
                onOk:function(reply){
                    console.log(reply);
                }
            });
        }, false);
    }

    /*nav show or hide*/
    $('.nav>li').hover(function () {
        $(this).children('ul').stop(true, true).show(400);
    }, function () {
        $(this).children('ul').stop(true, true).hide(400);
    });
    /*search*/
    $('.search_ico').click(function () {
        $('.search_bar').toggleClass('search_open');
        if ($('#keyboard').val().length > 2) {
            $('#keyboard').val('');
            $('#searchform').submit();
        } else {
            return false;
        }
    });
    /*banner*/
    $('#banner').easyFader();

    /*topnav select*/
    var obj = null;
    var allMenu = document.getElementById('topnav').getElementsByTagName('a');
    // console.log(allMenu);
    obj = allMenu[0];
    for (i = 1; i < allMenu.length; i++) {
        if (window.location.href.indexOf(allMenu[i].href) >= 0) {
            obj = allMenu[i];
        }
    }
    obj.id = 'topnav_current';

    /*mnav dl open*/
    var oH2 = document.getElementsByTagName('h2')[0];
    var oUl = document.getElementsByTagName('dl')[0];
    oH2.onclick = function () {
        var style = oUl.style;
        style.display = style.display == 'block' ? 'none' : 'block';
        oH2.className = style.display == 'block' ? 'open' : '';
    };
    //菜单点击效果
    $('.list_dt').on('click', function () {
        $('.list_dd').stop();
        $(this).siblings('dt').removeAttr('id');
        if ($(this).attr('id') == 'open') {
            $(this).removeAttr('id').siblings('dd').slideUp();
        } else {
            $(this).attr('id', 'open').next().slideDown().siblings('dd').slideUp();
        }
    });

    //设置固定关注我们

    if ($('#follow-us')) {
        var followUsPosition = $('#follow-us').offset().top;
        window.onscroll = function () {
            var nowPosition = document.documentElement.scrollTop;
            if (nowPosition - followUsPosition > 0) {
                setTimeout(function () {
                    $('#follow-us').attr('class', 'guanzhu gd');
                }, 150);
            } else {
                $('#follow-us').attr('class', 'guanzhu');
            }
        };
    }


    //回到顶部
    // browser window scroll (in pixels) after which the "back to top" link is shown
    var offset = 300,
        //browser window scroll (in pixels) after which the "back to top" link opacity is reduced
        offset_opacity = 1200,
        //duration of the top scrolling animation (in ms)
        scroll_top_duration = 700,
        //grab the "back to top" link
        $back_to_top = $('.cd-top');

    //hide or show the "back to top" link
    $(window).scroll(function () {
        ($(this).scrollTop() > offset) ? $back_to_top.addClass('cd-is-visible'): $back_to_top.removeClass('cd-is-visible cd-fade-out');
        if ($(this).scrollTop() > offset_opacity) {
            $back_to_top.addClass('cd-fade-out');
        }
    });
    //smooth scroll to top
    $back_to_top.on('click', function (event) {
        event.preventDefault();
        $('body,html').animate({
            scrollTop: 0,
        }, scroll_top_duration);
    });

});


//function makeHeader(blog_username, username){
//    //blog_username 当前访问的博客的作者
//    //username   登陆的用户
//
//    var header_body = '';
//header_body += '<body>';
//header_body += '<div id="nav-bottom">';
//
//	header_body += '<div class="nav-top">';
//		header_body += '<div class="top">';
//			header_body += '<div class="py-container">';
//				header_body += '<div class="shortcut">';
//					header_body += '<ul class="fl">';
//						header_body += '<li class="f-item">趣书网欢迎您！</li>';
//						header_body += '<li class="f-item">请<a href="login.html" target="_blank">登录</a>　<span><a href="register.html" target="_blank">免费注册</a></span></li>';
//					header_body += '</ul>';
//					header_body += '<ul class="fr">';
//						header_body += '<li class="f-item">我的订单</li>';
//						header_body += '<li class="f-item space"></li>';
//						header_body += '<li class="f-item"><a href="home.html" target="_blank">我的趣书</a></li>';
//						header_body += '<li class="f-item space"></li>';
//						header_body += '<li class="f-item">趣书网会员</li>';
//						header_body += '<li class="f-item space"></li>';
//						header_body += '<li class="f-item">企业采购</li>';
//						header_body += '<li class="f-item space"></li>';
//						header_body += '<li class="f-item">关注趣书网</li>';
//						header_body += '<li class="f-item space"></li>';
//						header_body += '<li class="f-item" id="service">';
//							header_body += '<span>客户服务</span>';
//							header_body += '<ul class="service">';
//								header_body += '<li><a href="cooperation.html" target="_blank">合作招商</a></li>';
//								header_body += '<li><a href="shoplogin.html" target="_blank">商家后台</a></li>';
//								header_body += '<li><a href="cooperation.html" target="_blank">合作招商</a></li>';
//								header_body += '<li><a href="#">商家后台</a></li>';
//							header_body += '</ul>';
//						header_body += '</li>';
//						header_body += '<li class="f-item space"></li>';
//						header_body += '<li class="f-item">网站导航</li>';
//					header_body += '</ul>';
//				header_body += '</div></div></div>';
//
//
//		header_body += '<div class="header">';
//			header_body += '<div class="py-container">';
//				header_body += '<div class="yui3-g Logo">';
//					header_body += '<div class="yui3-u Left logoArea">';
//						header_body += '<a class="logo-bd" title="趣书网" href="JD-index.html" target="_blank"></a>';
//					header_body += '</div>';
//					header_body += '<div class="yui3-u Center searchArea">';
//						header_body += '<div class="search">';
//							header_body += '<form action="" class="sui-form form-inline">';
//
//								header_body += '<div class="input-append">';
//									header_body += '<input type="text" id="autocomplete" type="text" class="input-error input-xxlarge" />';
//									header_body += '<button class="sui-btn btn-xlarge btn-danger" type="button">搜索</button>';
//								header_body += '</div></form></div>';
//						header_body += '<div class="hotwords">';
//							header_body += '<ul>';
//								header_body += '<li class="f-item">趣书网首发</li>';
//								header_body += '<li class="f-item">亿元优惠</li>';
//								header_body += '<li class="f-item">9.9元团购</li>';
//								header_body += '<li class="f-item">每满99减30</li>';
//								header_body += '<li class="f-item">亿元优惠</li>';
//								header_body += '<li class="f-item">9.9元团购</li>';
//								header_body += '<li class="f-item">办公用品</li></ul></div></div>';
//					header_body += '<div class="yui3-u Right shopArea">';
//						header_body += '<div class="fr shopcar">';
//							header_body += '<div class="show-shopcar" id="shopcar">';
//								header_body += '<span class="car"></span>';
//								header_body += '<a class="sui-btn btn-default btn-xlarge" href="cart.html" target="_blank">';
//									header_body += '<span>我的购物车</span>';
//									header_body += '<i class="shopnum">0</i>';
//								header_body += '</a>';
//								header_body += '<div class="clearfix shopcarlist" id="shopcarlist" style="display:none">';
//									header_body += '<p>"啊哦，你的购物车还没有商品哦！"</p>';
//									header_body += '<p>"啊哦，你的购物车还没有商品哦！"</p></div></div></div></div></div>';
//
//				header_body += '<div class="yui3-g NavList">';
//					header_body += '<div class="yui3-u Left all-sort">';
//						header_body += '<h4>全部商品分类</h4>';
//					header_body += '</div>';
//					header_body += '<div class="yui3-u Center navArea">';
//						header_body += '<ul class="nav">';
//							header_body += '<li class="f-item">服装城</li>';
//							header_body += '<li class="f-item">美妆馆</li>';
//							header_body += '<li class="f-item">趣书超市</li>';
//							header_body += '<li class="f-item">全球购</li>';
//							header_body += '<li class="f-item">闪购</li>';
//							header_body += '<li class="f-item">团购</li>';
//							header_body += '<li class="f-item">有趣</li>';
//							header_body += '<li class="f-item"><a href="seckill-index.html" target="_blank">秒杀</a></li>';
//						header_body += '</ul></div><div class="yui3-u Right"></div></div></div></div></div></div>';
//
//
//
//
//
//header_body += '</body>';
//
//    header_body += '<div id="account">';
//        header_body += '<div class="py-container">';
//            header_body += '<div class="yui3-g home">';
//
//               header_body += ' <div class="yui3-u-1-6 list">';
//
//                   header_body += ' <div class="person-info">';
//                       header_body += ' <div class="person-photo"><img id="person-photo-img" height="48px" width="48px" src="/static/img/_/photo.png" alt=""></div>';
//                        header_body += '<div class="person-account">';
//                          header_body += '  <span class="person-name">Michelle</span>';
//                         header_body += '   <span class="safe">账户安全</span>';
//                        header_body += '</div>';
//                        header_body += '<div class="clearfix"></div>';
//                    header_body += '</div>';
//                   header_body += ' <div class="list-items">';
//                      header_body += '  <dl>';
//						header_body += '	<dt><i>·</i> 订单中心</dt>';
//						header_body += '	<dd ><a href="home-index.html"   >我的订单</a></dd>';
//						header_body += '	<dd><a href="home-order-pay.html" >待付款</a></dd>';
//						header_body += '	<dd><a href="home-order-send.html"  >待发货</a></dd>';
//						header_body += '	<dd><a href="home-order-receive.html" >待收货</a></dd>';
//						header_body += '	<dd><a href="home-order-evaluate.html" >待评价</a></dd>';
//						header_body += '</dl>';
//						header_body += '<dl>';
//						header_body += '	<dt><i>·</i> 我的中心</dt>';
//						header_body += '	<dd><a href="home-person-collect.html" >我的收藏</a></dd>';
//						header_body += '	<dd><a href="home-person-footmark.html" >我的足迹</a></dd></dl>';
//					header_body += '<dl><dt><i>·</i> 物流消息</dt></dl><dl>';
//							header_body += '<dt><i>·</i> 设置</dt>';
//							header_body += '<dd><a href="change_info" class="list-active">个人信息</a></dd>';
//							header_body += '<dd><a href="home-setting-address.html"  >地址管理</a></dd>';
//							header_body += '<dd><a href="password_info" >安全管理</a></dd>';
//						header_body += '</dl> </div></div></div> </div></div>';
//    //博客作者-用户信息url
////    var user_info_url = '/' + blog_username + '/' + 'info'
////    //登陆用户发博客url
////    if (username){
////        var topic_release_url = '/' + username + '/' + 'topics/release'
////    }else{
////        //没有登陆状态直接去登陆
////        var topic_release_url = '/login'
////    }
////
////    //访问博主的博客文章
////    var user_topics_url = '/' + blog_username + '/' + 'topics'
////
////    var header_body = ''
////    header_body += '<header id="header">';
////    header_body += '<div class="menu">';
////    header_body += ' <nav class="nav" id="topnav"> ';
////    header_body += '<h1 class="logo"><a href="/index"> ' + decodeURI(blog_username) + '的博客</a></h1>';
////    header_body += '<li><a href="/index">网站首页</a></li>';
////    header_body += '<li>';
////    header_body += '<a href=' + '"' + user_topics_url + '"' + '>文章列表</a>';
////    header_body += '<ul class="sub-nav">';
////    header_body += '<li><a href=' + '"' + user_topics_url + '?category=tec"' + '>技术</a></li>';
////    header_body += '<li><a href=' + '"' + user_topics_url + '?category=no-tec"' + '>非技术</a></li>';
////    header_body += '</ul>';
////    header_body += '</li>';
////    header_body += '<li><a href=/' + username + '/change_password>安全设置</a> </li>';
////    header_body += '<li><a href=' + '"' + user_info_url + '"' + '>关于我</a> </li>';
////    header_body += '<li><a href=' + '"' + topic_release_url + '"' + '>发表博客</a> </li>';
////    header_body += '</nav>';
////    header_body += '</div>';
////    if (username){
////        header_body += '<li><a href= /' + username + '/change_info id="change_info" target="_blank">编辑</a></li>';
////        //header_body += '<li><a href="/" id="login_out" target="_blank">登出</a></li>';
////        header_body += '<li><span id="login_out" target="_blank">登出</span></li>';
////    }else{
////        header_body += '<a href="/login" id="login" target="_blank">登陆</a>';
////        header_body += '<a href="register.html" id="register" target="_blank">注册</a>';
////    }
////    header_body += '</header>';
//
//    return header_body
//}




function loginOut(){

    $('#login_out').on('click', function(){

            if(confirm("确定登出吗？")){
                window.localStorage.removeItem('dnblog_token');
                window.localStorage.removeItem('dnblog_user');
                window.location.href= '/index';
            }
        }
    )

}
