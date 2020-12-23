$(function() {
    token = window.localStorage.getItem("dnblog_token");
    $(".sum-btn").click(function() {
        $.ajax({
            type: "get",
            url: "http://176.215.66.101:8000/payment/jump/",
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