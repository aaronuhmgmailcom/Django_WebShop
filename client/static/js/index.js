// 外部js文件
$(function () {
    var BASE_URL = '../static/images/';
    var html = '';
    $.each(faderData, function (i, o) {
        html += '<li class="slide">';
        html += '<a href="#">'
        html += `<img src="${BASE_URL + o.img_url}" alt="">`
        html += '</a></li>'
    })
    $('.fader_controls').before(html);
    $('.fader').easyFader();
    function add_products(data) {
        var html = '';
        $.each(data, function (i, o) {
            var product = `
            <div class="products">
                <div class="img">
                    <a href="#">
                        <img src="${BASE_URL+o.img}" alt="">
                    </a>
                </div>
                <p class="product_name">
                    <a href="#">
                        ${o.product_name}
                    </a>
                </p>
                <h3 class="price">
                   ￥${o.price}
                </h3>
            </div>
            `
            html += product
        })//each结束
        // 将拼接好的字符串追加到页面
        $('.productsbox').append(html)
    }

    add_products(productData.slice(0,20));

    var canLoad = true;//判读是否可以加载数据
    $(document).scroll(function(){
        var scrollTop = $(document).scrollTop()
        var windowHeight = $(window).height()
        var documentHeight = $(document).height()
        if(documentHeight-scrollTop-windowHeight<=200){
            var size = $('.products').length;
            if(canLoad){
                var data = productData.slice(size,size+5);
                if (data.length>0){
                    add_products(data)
                }else{
                    alert('没有更多商品')
                    canLoad = false//没有数据后就禁止加载
                }
            }
        }

    })
})
$('#addr').mouseover(function(){
    $('#prov_list').removeClass('hide')
})
$('#addr').mouseleave(function(){
    $('#prov_list').addClass('hide')
})
$('#prov_list').mouseover(function(){
    $('#prov_list').removeClass('hide')
})
$('#prov_list').mouseleave(function(){
    $('#prov_list').addClass('hide')
})