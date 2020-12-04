window.addEventListener('load', function() {
    var focus = document.querySelector('.focus');
    // 按钮
    var arrow_l = document.querySelector('.arrow_l');
    var arrow_r = document.querySelector('.arrow_r');
    // 父盒子的宽度
    var focuswidth = focus.offsetWidth;
    // 控制圆圈播放
    var circle = 0;

    // 1.鼠标经过盒子显示按钮
    focus.addEventListener('mouseenter', function() {
        arrow_l.style.display = 'block';
        arrow_r.style.display = 'block';
        // 停止自动播放定时器
        clearInterval(timer);
        timer = null; //清除定时器变量

    });

    // 2.鼠标离开盒子隐藏按钮
    focus.addEventListener('mouseleave', function() {
        arrow_l.style.display = 'none';
        arrow_r.style.display = 'none';
        // 开启定时器
        timer = setInterval(function() {
            // 手动调用 右侧按钮点击事件
            arrow_r.click();
        }, 2000);

    });
    // 3.点击按钮切换图片
    // 点击事件
    var num = 0;
    // flag节流阀
    var flag = true;
    arrow_r.addEventListener('click', function() {
        // 添加判断节流阀,关闭节流阀之后,点击事件不执行了.因此在回调函数内开启
        if (flag) {
            // console.log(flag);
            // 节流阀
            flag = false;
            // console.log(flag);

            // 处于最后一张克隆的图时，迅速跳回第一张，并把num重新赋值为0
            if (num == ul.children.length - 1) {
                ul.style.left = 0;
                num = 0;
            }
            num++;
            animate(ul, -num * focuswidth, function() {
                // console.log(flag);
                flag = true; //打开节流阀
            });
            // console.log(circle);

            // 8。点击右侧按钮圆圈跟随按钮变化
            circle++;
            // 排他思想，先清除所有样式再给当前添加current
            for (var i = 0; i < ol.children.length; i++) {
                ol.children[i].className = '';
            };
            // if (circle == ol.children.length) {
            //     console.log(ol.children.length);
            //     circle = 0;
            // }
            circle = circle == ol.children.length ? 0 : circle;
            // 当前圆圈添加样式
            ol.children[circle].className = 'current';
            // console.log(num, '23');
            // console.log(flag);

        }
    });

    // 左侧
    arrow_l.addEventListener('click', function() {
        // 处于第一张时候，点击左侧按钮应该跳到最后一张克隆的图
        if (flag) {
            flag = false;
            if (num == 0) {
                num = ul.children.length - 1;
                // 最后一张图片的num*图片的宽度，是负值。下面是最后一张的位置
                ul.style.left = -num * focuswidth + 'px';
            }
            num--;
            animate(ul, -num * focuswidth, function() {
                flag = true;
            });
            // console.log(circle, '123');

            circle--;
            for (var i = 0; i < ol.children.length; i++) {
                ol.children[i].className = '';

            };
            // circle<0，说明是第一张图片，所以圆圈要改成最后一个圆圈
            // if (circle < 0) {
            //     console.log(ol.children.length);
            //     circle = ol.children.length - 1;
            // }
            circle = circle < 0 ? ol.children.length - 1 : circle;
            // 当前圆圈添加样式
            ol.children[circle].className = 'current';
            // console.log(num);
        }
    });

    // 4.底部圆圈数量与图片数量相同
    // 获取focus内的ul
    var ul = focus.querySelector('ul');
    var ol = focus.querySelector('.circle');
    // console.log(ul.children.length);//4
    // 循环添加存放圆圈的li
    for (var i = 0; i < ul.children.length; i++) {
        // ol的li的样式已经写好了，直接添加li就可以显示小圆圈  // 创建li
        var li = document.createElement('li');
        // 添加li插入ol
        ol.appendChild(li);
        // 记录当前圆圈的索引号,设置自定义属性
        li.setAttribute('index', i);

        // 5.圆圈点击改变颜色
        li.addEventListener('click', function() {
            // 排他思想 需要清空ol的所有子元素的classname
            for (var i = 0; i < ol.children.length; i++) {
                ol.children[i].className = ''
            }
            // 给当前点击的li添加底色
            this.className = 'current';

            // 6.点击圆圈滑动 移动的是ul
            // 移动距离 -(圆圈的索引号*图片的宽度) ；图片的宽度跟父盒子一样宽
            // console.log(focuswidth);
            // 得到当前圆圈索引号
            var index = this.getAttribute('index');
            // 点击了li，把索引号给num,num是按钮控制滚动图片的
            num = index;
            // circle是控制圆点滚动的
            circle = index;
            // console.log(index);

            animate(ul, -(index * focuswidth));
        })
    }
    // ol的第一个li设置成current 选中状态
    ol.children[0].className = 'current';

    // 8.复制第一张图片放到ul最后,底部圆圈不会变多，因为是放在生成圆圈的后面复制的
    var first = ul.children[0].cloneNode(true);
    ul.appendChild(first);

    // 9 自动播放 使用定时器
    var timer = setInterval(function() {
        // 手动调用 右侧按钮点击事件
        arrow_r.click();
    }, 2000)


})