$(function() {
    token = window.localStorage.getItem("dnblog_token");
    $(".sum-btn").click(function() {
        $.ajax({
            type: "get",
            url: "http://127.0.0.1:8000/payment/jump/",
            beforeSend: function(request) {
                request.setRequestHeader("Authorization", token);
            },
            success: function(res) {
                if (res.code == 200) {
                    window.location.href = res.pay_url;
                } else {
                    alert("支付错误")
                }
            }
        })
    })
})