$(function(){
    $.ajax({
        type:"get",
        url:"http://176.215.66.101:8000/product/book_load",
        success:function (result) {
            var book1_list=result.data[0];
            var book2_list=result.data[1];
            var book3_list=result.data[2];
            var book4_list=result.data[3];
            html=``;
            for(var i=0;i<book1_list.length;i++){
                if(i%6==0){html+=`<br>`;}
                html+=`<li class="yui3-u-1-6"><a href="" class="pic"><img src="`;
                html+=book1_list[i].img;
                html+=`" alt="" onclick="showProduct(`;
                html+=book1_list[i].id;
                html+=`)"/></a><div class="like-text"><p>`;
                html+=book1_list[i].product_name;
                html+=`</p><h3>¥`;
                html+=book1_list[i].price;
                html+=`</h3></div></li>`;
            }
            $("#picLBxxl").append(html);
            html=``
            for(var i=0;i<book2_list.length;i++){
                if(i%6==0){html+=`<br>`;}
                html+=`<li class="yui3-u-1-6"><a href="" class="pic"><img src="`;
                html+=book2_list[i].img;
                html+=`" alt="" onclick="showProduct(`;
                html+=book2_list[i].id;
                html+=`)"/></a><div class="like-text"><p>`;
                html+=book2_list[i].product_name;
                html+=`</p><h3>¥`;
                html+=book2_list[i].price;
                html+=`</h3></div></li>`;
            }
            $("#gdmz").append(html);
            html=``
            for(var i=0;i<book3_list.length;i++){
                if(i%6==0){html+=`<br>`;}
                html+=`<li class="yui3-u-1-6"><a href="" class="pic"><img src="`;
                html+=book3_list[i].img;
                html+=`" alt="" onclick="showProduct(`;
                html+=book3_list[i].id;
                html+=`)"/></a><div class="like-text"><p>`;
                html+=book3_list[i].product_name;
                html+=`</p><h3>¥`;
                html+=book3_list[i].price;
                html+=`</h3></div></li>`;
            }
            $("#xs").append(html);
            html=``
            for(var i=0;i<book4_list.length;i++){
                if(i%6==0){html+=`<br>`;}
                html+=`<li class="yui3-u-1-6"><a href="" class="pic"><img src="`;
                html+=book4_list[i].img;
                html+=`" alt="" onclick="showProduct(`;
                html+=book4_list[i].id;
                html+=`)"/></a><div class="like-text"><p>`;
                html+=book4_list[i].product_name;
                html+=`</p><h3>¥`;
                html+=book4_list[i].price;
                html+=`</h3></div></li>`;
            }
            $("#mh").append(html);
        }
    })
})