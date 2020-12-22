$(function(){
    $.ajax({
        type:"get",
        url:"http://127.0.0.1:8000/rotations/load",
        success:function (result) {
            var mycarousel_list=result.data[0];
            var floorcarousel_list=result.data[1];
            var floorcarousell_list=result.data[2];
            for(var i=0;i<mycarousel_list.length;i++){
                if(i==0){
                    html=`<li data-target="#myCarousel" data-slide-to="`+i+`" class="active" ng-repeat="item in contentList[1]"></li>`;
                }else{
                    html=`<li data-target="#myCarousel" data-slide-to="`+i+`" ng-repeat="item in contentList[1]"></li>`;
                }
                $("#myCarousel>.carousel-indicators").append(html);
                if(i==0){
                    html=`<div class="active item" ng-repeat="item in contentList[1]"><a href="`+mycarousel_list[i].href+`"><img src="`+mycarousel_list[i].src+`" style="width:730px;height:454px;"/></a></div>`;
                }else{
                    html=`<div class="item" ng-repeat="item in contentList[1]"><a href="`+mycarousel_list[i].href+`"><img src="`+mycarousel_list[i].src+`" style="width:730px;height:454px;"/></a></div>`;
                }
                $("#myCarousel>.carousel-inner").append(html);
            }
            for(var i=0;i<floorcarousel_list.length;i++){
                if(i==0){
                    html=`<li data-target="#floorCarousel" data-slide-to="`+i+`" class="active"></li>`;
                }else{
                    html=`<li data-target="#floorCarousel" data-slide-to="`+i+`"></li>`;
                }
                $("#floorCarousel>.carousel-indicators").append(html);
                if(i==0){
                    html=`<div class="active item"><a href="`+floorcarousel_list[i].href+`"><img src="`+floorcarousel_list[i].src+`"/></a></div>`;
                }else{
                    html=`<div class="item"><a href="`+floorcarousel_list[i].href+`"><img src="`+floorcarousel_list[i].src+`"/></a></div>`;
                }
                $("#floorCarousel>.carousel-inner").append(html);
            }
            for(var i=0;i<floorcarousell_list.length;i++){
                if(i==0){
                    html=`<li data-target="#floorCarousell" data-slide-to="`+i+`" class="active"></li>`;
                }else{
                    html=`<li data-target="#floorCarousell" data-slide-to="`+i+`"></li>`;
                }
                $("#floorCarousell>.carousel-indicators").append(html);
                if(i==0){
                    html=`<div class="active item"><a href="`+floorcarousell_list[i].href+`"><img src="`+floorcarousell_list[i].src+`"/></a></div>`;
                }else{
                    html=`<div class="item"><a href="`+floorcarousell_list[i].href+`"><img src="`+floorcarousell_list[i].src+`"/></a></div>`;
                }
                $("#floorCarousell>.carousel-inner").append(html);
            }
        }
    })
})
