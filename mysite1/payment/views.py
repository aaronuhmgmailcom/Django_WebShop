from django.shortcuts import render

# Create your views here.
import json
import time

from alipay import AliPay

from django.conf import settings
from django.http import JsonResponse, HttpResponse
from order.models import Order
from order_item.models import OrderItem
from tools.login_dec import login_check

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

# 测试环境支付账号:自己的账号


# 读取生成的私钥文件内容
from user_wallet.models import UserWallet
from product.models import Product
from shopping_cart.models import ShoppingCart

private_key = open(settings.ALIPAY_KEY_DIR + "app_private_key.pem").read()
public_key = open(settings.ALIPAY_KEY_DIR + "alipay_publickey.pem").read()


# 1.基类(创建AliPay对象,封装API)
class MyAliPay(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 给ali包进行赋值
        self.alipay = AliPay(
            appid=settings.ALIPAY_APPID,  # 应用程序id
            # 当前app的私钥
            app_private_key_string=private_key,
            # alipay的公钥
            alipay_public_key_string=public_key,
            # 签名算法
            sign_type="RSA2",
            # 设定为测试环境
            debug=True,
            # 支付宝向返还支付情况的服务器路由
            app_notify_url="http://176.215.66.101:8000/payment/result"
        )

    # 凑出ali返回支付页面的url:payurl
    def get_trade_url(self, order_id, amount, mes, result_url):
        base_url = "https://openapi.alipaydev.com/gateway.do"
        # 凑出订单支付页面的查询支付串
        order_string = self.alipay.api_alipay_trade_page_pay(
            out_trade_no=order_id,  # 订单号
            total_amount=amount,  # 订单金额
            subject=mes,  # 订单的相关描述
            return_url=result_url,  # 支付结束重定向路由
            notify_url=settings.ALIPAY_NOTIFY_URL  # 返还支付结果路由
        )
        return base_url + "?" + order_string

    # 验签结果
    def get_verify_result(self, data, sign):
        return self.alipay.verify(data, sign)

    # 主动查询结果
    def get_trade_result(self, order_id):
        res = self.alipay.api_alipay_trade_query(out_trade_no=order_id)
        if res.get("trade_status") == "TRADE_SUCCESS":
            return True
        else:
            return False


# 此为支付路由页面逻辑逻辑
class JumpView(MyAliPay):
    @method_decorator(login_check)
    def get(self, request):
        user = request.myuser
        carts_list = ShoppingCart.objects.filter(purchaser_name=user.username, status=1)
        amount = 0
        for cart in carts_list:
            try:
                product = Product.objects.get(id=cart.product_id)
            except:
                print("-----------")

            amount += (product.price * cart.purchase_quantity)
        order = Order.objects.create(order_amount=amount, create_user_id=user.id, order_status=5,
                                     receiver=user.username, receiver_address=user.Delivery_address1,
                                     receiver_tel=user.TELEPHONE)
        # 进行用户账户明细表的创建
        for cart in carts_list:
            try:
                product = Product.objects.get(id=cart.product_id)
            except:
                print("------------------------")
            OrderItem.objects.create(order_id=order.id, product_id=cart.product_id, price=product.price,amount=cart.purchase_quantity)

            for cart in carts_list:
                cart.status=0
                cart.save()

        # 获取到订单支付页面地址
        result_url = "http://176.215.66.101:8000/payment/result?type=buy"
        url = self.get_trade_url(order.id, int(amount), "商品购买", result_url)
        return JsonResponse({"code": 200, "pay_url": url})

    @method_decorator(login_check)
    def post(self, request):
        json_str = request.body
        json_obj = json.loads(json_str)
        user = request.myuser
        # 创建用户账单明细表
        amount = json_obj["money"]
        old_wallet = UserWallet.objects.filter(user_id=user.id).last()
        wallet = UserWallet.objects.create(user_id=user.id, recharge=amount, total_balance=float(old_wallet.total_balance) + float(amount),
                                           available_balance=float(old_wallet.available_balance)+float(amount))
        result_url = "http://176.215.66.101:8000/payment/result?type=chongzhi"
        url = self.get_trade_url(wallet.id, amount, "余额充值", result_url)
        return JsonResponse({"code": 200, "pay_url": url})


# 在alipay支付平台结束,alipay重定向的结果页面
class ResultView(MyAliPay):
    def get(self, request):
        # 获取全部的重定向字符串
        print('===================')
        request_data = {k: request.GET[k] for k in request.GET.keys()}
        order_id = request_data["out_trade_no"]  # 获取订单id
        money = request_data["total_amount"]  # 订单金额
        genre = request_data.get("type")
        print(money)
        if genre == "chongzhi":
            try:
                wallet = UserWallet.objects.get(id=order_id)
            except:
                print("-------没有该余额充值订单----------")
                words = "充值失败!没有该余额充值订单!"
                return render(request, "result.html", locals())
            else:
                # 获取到订单后,向查询支付结果
                result = self.get_trade_result(order_id)
                if result:
                    # 支付成功修改用户明细表的余额信息
                    wallet.total_balance = float(wallet.total_balance) + float(money)
                    wallet.available_balance = float(wallet.available_balance) + float(money)
                    wallet.save()
                    words = "充值成功!"
                    return render(request, "result.html", locals())
                else:
                    # 支付失败
                    words = "充值失败!请您完成支付!"
                    return render(request, "result.html", locals())
        elif genre == "buy":
            order_id = request_data["out_trade_no"]
            try:
                order = Order.objects.get(id=order_id)
            except:
                print("--------没有该订单----------")
            # money = order.order_amount  # 获取到订单金额
            # 在查看订单状态是否修改
            if order.order_status == 1:
                # ---------此处需要是否创建用户详情表------------
                words = "支付成功!我们将尽快为您发货!"
                return render(request, "result.html", locals())
            elif order.order_status == 0:
                # 主动查询
                result = self.get_trade_result(order_id)
                if result:
                    # 同时也进行订单数据库的修改
                    order.order_status = 1
                    order.pay_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    order.save()
                    words = "支付成功!我们将尽快为您发货!"
                    return render(request, "result.html", locals())
                else:
                    words = "支付失败!请您在24小时内完成支付"
                    return render(request, "result.html", locals())

    # 此部分无法实现:需真实服务器ip才可获取到ali提交数据结果
    def post(self, request):
        request_data = {k: request.POST[k] for k in request.POST.key()}
        sign = request_data.pop("sign")
        res = self.get_verify_result(request_data, sign)
        if res:
            trade_status = request_data["trade_status"]
            if trade_status == "TRADE_SUCCESS":
                order_id = request_data["out_trade_no"]
                try:
                    order = Order.objects.get(id=order_id)
                except Exception as e:
                    print("-----订单未创建成功 %s------" % e)
                else:
                    order.order_status = 1
                    # 也可修改支付时间
                    order.pay_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    order.save()
                    return HttpResponse("ok")
            else:
                # 支付状态不对,不做修改;
                return HttpResponse("ok")
        else:
            # 验签不正确
            return HttpResponse("非法访问")
