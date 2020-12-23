var countdown = 90;
    function settime(obj) {
        if (countdown == 0) {
            obj.removeAttribute("disabled");
            obj.value = "免费获取验证码";
            countdown = 90;
            return;
        } else {
            obj.setAttribute("disabled", true);
            obj.value = "重新发送(" + countdown + ")";
            countdown--;
        }
        setTimeout(function () {
            settime(obj)
        }
            , 1000)
    }

    // 对输入框做一个简单事件处理
    $(function () {
        var get_phone = $("#tel");
        // 当输入框发生失去焦点事件后,执行函数
        get_phone.blur(function () {
            $("span").remove();
            var phone = get_phone.val();
            if (phone.length == 11) {
                $("#tel").after('<span class="success"><i class="success_icon"></i></span>')
            } else if (phone.length > 0 || phone.length > 11) {
                $("#tel").after('<span class="error"><i class="error_icon"></i>手机号格式不正确</span>')
            }
        })
        var get_password_1 = $("#password_1");
        // 密码框发生失去焦点事件,给出密码强弱提示信息
        get_password_1.blur(function () {
            $("em").remove();
            var password_1 = get_password_1.val()
            if (password_1.length >= 8 && password_1.length <= 12) {
                $(".safe").append('<em class="ruo">弱</em>');
            } else if (password_1.length >= 13 && password_1.length <= 16) {
                $(".safe").append('<em class="zhong">中</em>');
            } else if (password_1.length >= 17 && password_1.length <= 20) {
                $(".safe").append('<em class="qiang">强</em>');
            }
        })
    })


    // 获取手机验证码,点击事件请求；手机验证码接口已完成
    function sendSMS() {
        $("span").remove();
        // 获取到用户输入的手机号
        var phone = $("#tel").val()
        // 封装为json对象
        var post_data = { "phone": phone }
        // 同时想服务器发送跨域请求
        $.ajax({
            url: "http://176.215.66.101:8000/users/sms",
            type: "POST",
            data: JSON.stringify(post_data),
            contentType: "application/json", // 发送数据类型
            dataType: "json", //响应数据类型
            success: function (result) {
                if (result.code == 200) {
                    // 在手机号节点后面添加正确提示信息
                    $("#sms").after('<span class="success"><i class="success_icon"></i>验证码发送成功</span>')
                } else {
                    $("#sms").after(`<span class="error"><i class="error_icon"></i>${result.error}</span>`)
                }
            }

        })
    }

    // 登录注册提交按钮
    function register() {
        if ($('input[type="checkbox"]').is(':checked')) {
            var phone = $("#tel").val();
            var sms_num = $("#sms").val();
            var password_1 = $("#password_1").val();
            var password_2 = $("#password_2").val();
            var post_data = { "phone": phone, "sms_num": sms_num, "password_1": password_1, "password_2": password_2 }
            $.ajax({
                url: "http://176.215.66.101:8000/users",
                type: "post",
                data: JSON.stringify(post_data),
                contentType: "application/json",
                dataType: "json",
                success: function (result) {
                    if (result.code == 200) {
                        window.localStorage.setItem("user_token", result.data.token);
                        window.localStorage.setItem("user_name", result.nickname);
                        // 跳转页面,到首页导航页面(导航页面的左上角会添加登录者的昵称)
                        window.location = "/index"
                    } else {
                        // 后端返回多种情况，验证码不正确，密码不一致,手机号已存在,等等,根据服务器提示码给出对应页面显示
                        alert("注册失败")
                    }
                }
            })
        } else {
            alert("请同意协议进行注册")
        }
    }