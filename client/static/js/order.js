token = window.localStorage.getItem("dnblog_token");
username = window.localStorage.getItem("dnblog_user");
var url = window.location.toString();
var query_array = url.split("?");
if (query_array.length > 1) {
    var get_url = "http://47.94.174.118:8000/order/search" + "?" + query_array[1];
} else {
    var get_url = "http://47.94.174.118:8000/order/search";
}
// console.log(get_url)



// 请求获取到订单列表数据
var html = "";
$.ajax({
    type: "get",
    url: get_url,
    // 先发送token给服务器,验证用户是否具有登录状态
    beforeSend: function (request) {
        request.setRequestHeader("Authorization", token);
    },
    success: function (result) {
        if (result.code == 200) {
            console.log(result)
            var user = result.data.username
            var num1 = result.data.no_pay
            var num2 = result.data.no_arr
            var num3 = result.data.no_mes
            var t_html = `<li>
                                <a href="order">全部订单</a>
                                <span class="nums"></span>
                            </li>
                            <li>
                                <a href="order?status=0">待付款</a>
                                <span class="nums">${num1}</span>
                            </li>
                            <li>
                                <a href="order?status=3">待收货</a>
                                <span class="nums">0</span>
                            </li>
                            <li>
                                <a href="order?status=1">待收货</a>
                                <span class="nums">${num2}</span>
                            </li>
                            <li>
                                <a href="order?status=2">待评价</a>
                                <span class="nums">${num3}</span>
                            </li>`
            $(".menu_list").append(t_html);
            var orders = result.data.orders

            if (orders.length == 0) {
                html += `<div id="order">
                        <div class="my_order">
                        <!-- 订单详情 -->
                        <div class="order_box">
                        <h3>
                            您买的东西太少了，这里都是空的,
                            <a href="/index">快去挑选合适的商品吧!</a>
                        </h3>
                        </div>
                        </div>
                        </div>`
                        
            } else {
                for (var o in orders) {
                    // console.log(o)
                    html += `<tbody id="${orders[o].order_id}">
                    <tr class ="emp_row" ><td colspan = "5"></td>
                    </tr><tr class ="order_title" ><td colspan ="5">
                    <span class ="gap"></span><span class ="dealtime" title="订单创建时间" > ${orders[o].created_time}</span>
                    <span class ="number" >订单号: <a href = "#" >${orders[o].order_id}</a></span><div class ="order_shop" >
                    <span class ="shop"><a href = "" class ="shop_name" >趣书</a><a href = "" class ="shop_img" ></a></span></div>
                    </td></tr>`
                     var sub = orders[o].sub

                     for (var t in sub) {
                     html += `<tr class="order_body">
                        <td>
                            <div class="goods_item">
                                <div class="p_img">
                                    <a href="/product/${sub[t].p_id}">
                                        <img src="${sub[t].img}" width="60" height="60">
                                    </a>
                                </div>
                                <div class="p_msg">
                                    <div class="p_name">
                                        <a href="/product/${sub[t].p_id}">${sub[t].name}</a>
                                    </div>
                                </div>
                            </div>
                            <div class="goods_nums">×${sub[t].amount}</div>
                            <div class="goods_repair">
                                <a href="#">申请售后</a>
                                <br>
                                <a href="#">卖了换钱</a>
                            </div>
                        </td>
                        <td rowspan="1">
                            <div class="tooptip">
                                <span class="txt">${user}</span>
                                <b></b>
                            </div>
                        </td>
                        <td rowspan="1">
                            <div class="amount">
                                <span>${sub[t].price}</span>
                                <br>
                                <span class="pay">在线支付</span>
                            </div>
                        </td>
                        <td rowspan="1">
                            <div class="status">
                                <span style="color: #aaa">已完成</span>
                                <br>
                                <a href="#">订单详情</a>
                            </div>
                        </td>
                        <td rowspan="1">
                            <div class="operate">
                                <a href="#">查看发票</a>
                                <br>
                                <a href="#">评价</a>
                                <br>
                                <a href="#" class="btn_again">
                                    <b></b>
                                    立即购买
                                </a>
                            </div>
                        </td>
                    </tr>  `
                    }
                 html += `</tbody>`
                }
            }
            $(".order_tab").append(html);
        } else {
            alert(result.error)
        }
    }
})

