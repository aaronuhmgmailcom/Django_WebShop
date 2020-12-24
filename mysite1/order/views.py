from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from order_item.models import OrderItem
from product.models import Product
from tools.login_dec import login_check
from .models import Order


# Create your views here.
class OrdersView(View):
    def __make_order_list(self, orders):
        order_list = []
        order_item_list = []
        for order in orders:
            x = {}
            try:
                order_item = OrderItem.objects.filter(order_id=order.id)  # 查找到订单详情表
                product = Product.objects.get(id=order_item[0].product_id)
            except Exception as e:
                print("---没有获取订单%s的商品详情信息---" % order.id)
            else:
                x["created_time"] = order.create_date.strftime("%Y-%m-%d %H:%M:%S")
                x["order_id"] = order.id
                x["price"] = order.order_amount
                x["img"] = str(product.img)
                x["sign"] = product.description
                x["amount"] = order_item[0].amount
                x["sub"]=[]
                for item in order_item:
                    product = Product.objects.get(id=item.product_id)
                    xx = {}
                    xx["created_time"] = order.create_date.strftime("%Y-%m-%d %H:%M:%S")
                    xx["order_id"] = order.id
                    xx["p_id"] = product.id
                    xx["price"] = item.price
                    xx["name"] = product.product_name
                    xx["img"] = str(product.img)
                    xx["sign"] = product.description
                    xx["amount"] = item.amount

                    x["sub"].append(xx)
                order_list.append(x)
        return order_list

    @method_decorator(login_check)
    def get(self, request):
        """
        v1/orders 全量订单
        v1/orders?status=0  待支付
        v1/orders?status=1  待收货
        v1/orders?status=2  待评价
        """
        # 获取到用户
        user = request.myuser
        # 获取到查询字符串
        status = request.GET.get("status")
        no_pay_orders = Order.objects.filter(create_user_id=user.id, order_status=0)
        no_arr_orders = Order.objects.filter(create_user_id=user.id, order_status=5)
        no_mes_orders = Order.objects.filter(create_user_id=user.id, order_status=6)
        if status == "0":
            order_list = self.__make_order_list(no_pay_orders)
        elif status == "1":
            order_list = self.__make_order_list(no_arr_orders)
        elif status == "2":
            order_list = self.__make_order_list(no_mes_orders)
        else:
            all_orders = Order.objects.filter(create_user_id=user.id)
            order_list = self.__make_order_list(all_orders)
        result = {"code": 200, "data": {}}
        result["data"]["username"] = user.username
        result["data"]["no_pay"] = len(no_pay_orders)
        result["data"]["no_arr"] = len(no_arr_orders)
        result["data"]["no_mes"] = len(no_mes_orders)
        result["data"]["orders"] = order_list
        # print(result)
        return JsonResponse(result)
