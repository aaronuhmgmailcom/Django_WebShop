from django.shortcuts import render
import datetime
import json
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.
from .models import ShoppingCart
from product.models import Product


class cartView(View):
    def make_topics_res(self, author, author_topics):
        topics_res = []

        # result = {'code': 200, 'username': username,
        #           'data': {'product_id': user.product_id, 'purchase_quantity': user.purchase_quantity,
        #                    'purchaser_name': user.purchaser_name,
        #                    'status': user.status,
        #                    'create_date': user.create_date, 'cart_id': user.cart_id}}
        sum=0
        count=0
        for topic in author_topics:
            d = {}
            d['product_id'] = topic.product_id

            p = Product.objects.get(id=topic.product_id)
            d['product_name'] = p.product_name
            d['product_img'] = str(p.img)
            d['product_price'] = p.price
            d['purchase_quantity'] = topic.purchase_quantity
            d['purchaser_name'] = topic.purchaser_name
            d['status'] = topic.status
            d['create_date'] = topic.create_date.strftime('%Y-%m-%d %H:%M:%S')
            d['cart_id'] = topic.cart_id
            topics_res.append(d)
            sum+=(int)(p.price)
            count+=1

        res = {'code': 200, 'data': {}}
        res['data']['topics'] = topics_res
        res['data']['username'] = author
        res['data']['sum'] = sum
        res['data']['count'] = count
        return res

    def get(self, request, username=None):
        print(username)
        if username:
            try:
                topics = ShoppingCart.objects.filter(purchaser_name=username, status=1)
            except Exception as e:
                print('-get ShoppingCart error is %s-' % e)
                result = {'code': 10104, 'error': 'ShoppingCart not exist'}
                return JsonResponse(result)
            # get search data

            res = self.make_topics_res(username, topics)

            return JsonResponse(res)

        return HttpResponse('--users get--')

    def put(self, request, username=None):
        # 获取用户提交数据
        if request.method != 'PUT':
            result = {'code': 10106, 'error': '必须是PUT'}
            return JsonResponse(result)
        # 从REQUEST.MYUSER获取要修改用户
        json_str = request.body
        json_obj = json.loads(json_str)
        print(json_obj)
        product_id = json_obj['pid']
        purchase_quantity = 1
        purchaser_name = username
        status = 1
        cart_id =0

        topics = ShoppingCart.objects.create(product_id=product_id,purchase_quantity=purchase_quantity,purchaser_name=purchaser_name,status=status,cart_id=cart_id)

        result = {'code': 200, 'username': topics.purchaser_name}
        return JsonResponse(result)

    def delete(self, request, username=None):
        # 获取用户提交数据
        if request.method != 'DELETE':
            result = {'code': 10106, 'error': '必须是DELETE'}
            return JsonResponse(result)
        # 从REQUEST.MYUSER获取要修改用户
        json_str = request.body
        json_obj = json.loads(json_str)
        print(json_obj)
        product_id = json_obj['pid']
        purchaser_name = username
        status = 1

        topics = ShoppingCart.objects.filter(product_id=product_id,
                                             purchaser_name=purchaser_name, status=status)[0]
        topics.delete()

        result = {'code': 200, 'username': topics.purchaser_name}
        return JsonResponse(result)