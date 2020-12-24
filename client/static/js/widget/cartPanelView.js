var cartPanelView = {

    cartCellTemplate : "",

    // 初始化
    setup : function (callback) {

        $('.tbar-cart-item').hover(function (){ $(this).find('.p-del').show(); },function(){ $(this).find('.p-del').hide(); });
        $('.jth-item').hover(function (){ $(this).find('.add-cart-button').show(); },function(){ $(this).find('.add-cart-button').hide(); });

        // 悬浮按钮
        $('.toolbar-tab').hover(function (){
            $(this).find('.tab-text').html($(this).attr("data"));
            $(this).find('.tab-text').addClass("tbar-tab-hover");
            $(this).find('.footer-tab-text').addClass("tbar-tab-footer-hover");
            $(this).addClass("tbar-tab-selected");
        },function(){
            $(this).find('.tab-text').removeClass("tbar-tab-hover");
            $(this).find('.footer-tab-text').removeClass("tbar-tab-footer-hover");
            $(this).removeClass("tbar-tab-selected");
        });

        cartPanelView.cartCellTemplate = $("#tbar-cart-item-template").html();

        callback();
    },

    // 侧栏按钮点击
    tabItemClick : function (typeName) {
        if($('.toolbar-wrap').hasClass('toolbar-open')){
            cartPanelView.tbar_panel_close(typeName);
        }else{
            cartPanelView.tbar_panel_show(typeName);
        }
    },

	// 面板显示
	tbar_panel_show : function(panelName) {

		// 悬浮按钮
		$('.toolbar-tab').removeClass('tbar-tab-click-selected');
        $('.tbar-tab-'+panelName).addClass('tbar-tab-click-selected');
        $('.tbar-tab-'+panelName).find('.tab-text').remove();

		// 面板内容
		$('.toolbar-panel').css('visibility','hidden');
		$('.tbar-panel-'+panelName).css({'visibility':"visible","z-index":"1"});

		// 面板显示
		$('.toolbar-wrap').addClass('toolbar-open'); 
	},

	// 关闭面板
	tbar_panel_close : function(panelName) {

		if($('.tbar-tab-'+panelName).find('.tab-text').length > 0){
			$('.toolbar-tab').each(function(i){
				var tagValue = $(this).attr("tag");
				if((tagValue != panelName)&&(tagValue != undefined)){
					var info = "<em class='tab-text '>"+$(this).attr('data')+"</em>";
					$(this).append(info);
					$(this).removeClass('tbar-tab-click-selected');
					$('.tbar-panel-'+$(this).attr('tag')).css({'visibility':"hidden","z-index":"-1"});
				}
			});
			$('.tbar-tab-'+panelName).addClass('tbar-tab-click-selected');
			$('.tbar-tab-'+panelName).find('.tab-text').remove();
			$('.tbar-panel-'+panelName).css({'visibility':"visible","z-index":"1"});
		}else{
			$('.toolbar-wrap').removeClass('toolbar-open');
			var info = "<em class='tab-text '>"+$('.tbar-tab-'+panelName).attr("data")+"</em>";
			$('.tbar-tab-'+panelName).append(info);
			$('.tbar-tab-'+panelName).removeClass('tbar-tab-click-selected');
			$('.tbar-panel-'+panelName).css({'visibility':"hidden","z-index":"-1"});
		}
	},

    // 填充购物车数据
    fillCart : function(dataJSON) {
        // 购物车列表
        var rowsHtml = "";
        for(var i = 0; i < dataJSON.orders.length ; i++){
            var shops = dataJSON.orders[i];
            for(var x = 0; x < shops.orderItems.length ; x++){
                var it = shops.orderItems[x];
                rowsHtml += String.format(
                    cartPanelView.cartCellTemplate,
                    it.pid,
                    it.title,
                    it.image,
                    it.unitPrice*it.quantity,
                    it.quantity
                );
            }
        }
        $("#cart-list").html(rowsHtml);
        // 购物车小计
        $("#cart-number").html(dataJSON.totalQuantity);
        $("#cart-sum").html(String.format("¥{0}",dataJSON.totalPrices));
        // 侧栏 购物件数
        $("#tab-sub-cart-count").html(dataJSON.totalQuantity);
    }
};

$(function() {

    // 初始购物车侧边栏
    cartPanelView.setup(function(){
        // 载入购物车列表
        cartPanelView.fillCart(orderData);
    });

});



var orderData = {
  "totalQuantity":2,
  "totalPrices":8998,
  "orders":[
    {
      "shop":"领导力就是不装",
      "orderItems":[
        {
          "pid":"10803521657",
          "image":"http://img3m6.ddimg.cn/49/32/29159806-1_u_5.jpg",
          "title":"领导力就是不装 领导力就是不装 领导力就是不装 领导力就是不装 15.领导力就是不装",
          "color":"黑色",
          "size":"500+128",
          "unitPrice":49,
          "quantity":1,
          "gift":[
            {
              "pid":"10633272618",
              "title":"【炫龙】领导力就是不装 龙魂机甲"
            },
            {
              "pid":"10629228032",
              "title":"【炫龙】领导力就是不装 领导力就是不装 领导力就是不装 领导力就是不装"
            }
          ]
        },
        {
          "pid":"10803521657",
          "image":"http://img3m6.ddimg.cn/49/32/29159806-1_u_5.jpg",
          "title":"领导力就是不装 领导力就是不装 领导力就是不装 领导力就是不装 15.领导力就是不装",
          "color":"黑色",
          "size":"500+128",
          "unitPrice":49,
          "quantity":1,
          "gift":[
            {
              "pid":"10633272618",
              "title":"【炫龙】领导力就是不装 龙魂机甲"
            },
            {
              "pid":"10629228032",
              "title":"【炫龙】领导力就是不装 领导力就是不装 领导力就是不装 领导力就是不装"
            }
          ]
        },
      ]
    }
  ]
};