from django.shortcuts import render
import datetime
import json

from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import  UserAddress
import hashlib
import time
import jwt
from django.conf import settings
from tools.login_dec import login_check
import random


# Create your views here.

class UserAddressView(View):
    # @method_decorator(login_check)
    # def put(self, request, username=None):
    #     # 获取用户提交数据
    #     if request.method != 'PUT':
    #         result = {'code': 10106, 'error': '必须是PUT'}
    #         return JsonResponse(result)
    #     # 从REQUEST.MYUSER获取要修改用户
    #     user = User.objects.get(username=username)
    #     json_str = request.body
    #     json_obj = json.loads(json_str)
    #     user.nickname = json_obj['nickname']
    #     # user.sign = json_obj['sign']
    #     # user.Delivery_address1 = json_obj['info']
    #     user.province = json_obj['province']
    #     user.city = json_obj['city']
    #     user.district = json_obj['district']
    #     user.birthday = json_obj['year'] + '-' + json_obj['month'] + '-' + json_obj['day']
    #     user.gender = json_obj['gender']
    #
    #     user.save()
    #     result = {'code': 200, 'username': user.username}
    #     return JsonResponse(result)
    #
    # def get(self, request, username=None):
    #     print(username)
    #     if username:
    #         try:
    #             user = User.objects.get(username=username)
    #         except Exception as e:
    #             print('-get user error is %s-' % e)
    #             result = {'code': 10104, 'error': 'user not exist'}
    #             return JsonResponse(result)
    #         # get search data
    #         keys = request.GET.keys()
    #         if keys:
    #             data = {}
    #             for key in keys:
    #                 if key == 'password':
    #                     continue
    #                 if hasattr(user, key):
    #                     data[key] = getattr(user, key)
    #             result = {'code': 200, 'username': username, 'data': data}
    #         else:
    #             # get all data
    #             result = {'code': 200, 'username': username,
    #                       'data': {'info': user.Delivery_address1, 'sign': user.sign, 'gender': user.gender,
    #                                'year': user.birthday.year, 'province': user.province, 'city': user.city,
    #                                'district': user.district, 'month': user.birthday.month, 'day': user.birthday.day,
    #                                'nickname': user.nickname, 'avatar': str(user.IMAGE)}}
    #
    #         return JsonResponse(result)
    #     else:
    #         pass
    #
    #     return HttpResponse('--users get--')

    @method_decorator(login_check)
    def post(self,request, username=None):
        json_str=request.body
        json_obj =json.loads(json_str)
        username=json_obj['username']
        addressname = json_obj['addressname']
        email=json_obj['email']
        tel=json_obj['tel']
        detailaddress=json_obj['detailaddress']
        district=json_obj['district']
        city = json_obj['city']
        province = json_obj['province']
        receiver = json_obj['receiver']
        user = request.myuser
        print(addressname,detailaddress,province)

        # old_useraddress= UserAddress.objects.filter(username=username)
        # print(old_useraddress)

        try:
            UserAddress.objects.create(receiver=receiver,province=province,city=city,district=district,detail_address = detailaddress,TELEPHONE=tel,email=email,remark=addressname,default=1,user_profile=user)
        except Exception as e:
            print('error is %s' % e)
            return JsonResponse(e, safe=False)

        return JsonResponse({'code':200 ,'username':username})
