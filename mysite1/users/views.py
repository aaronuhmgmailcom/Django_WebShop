# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
# from .models import *
# from django.views.decorators.csrf import csrf_exempt
import datetime
import json

from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import User
import hashlib
import time
import jwt
from django.conf import settings
from tools.login_dec import login_check
import random
from tools.sms import YunTongXin
from .tasks import task_test
from .tasks import get_res
from user_wallet.models import UserWallet


def test_celery(request):
    task_test.delay()
    now = datetime.datetime.now()
    html = 'result at %s' % (now.strftime('%H:%M:%S'))
    return HttpResponse(html)


@login_check
def user_avatar(request, username):
    if request.method != 'POST':
        result = {'code': 10105, 'error': '必须是POST'}
        return JsonResponse(result)
    user = request.myuser
    user.IMAGE = request.FILES['avatar']
    user.save()
    result = {'code': 200, 'username': user.username}
    return JsonResponse(result)


class UsersView(View):
    @method_decorator(login_check)
    def put(self, request, username=None):
        # 获取用户提交数据
        if request.method != 'PUT':
            result = {'code': 10106, 'error': '必须是PUT'}
            return JsonResponse(result)
        # 从REQUEST.MYUSER获取要修改用户
        user = User.objects.get(username=username)
        json_str = request.body
        json_obj = json.loads(json_str)
        user.nickname = json_obj['nickname']
        # user.sign = json_obj['sign']
        # user.Delivery_address1 = json_obj['info']
        user.province = json_obj['province']
        user.city = json_obj['city']
        user.district = json_obj['district']
        user.birthday = json_obj['year'] + '-' + json_obj['month'] + '-' + json_obj['day']
        user.gender = json_obj['gender']

        user.save()
        result = {'code': 200, 'username': user.username}
        return JsonResponse(result)

    def get(self, request, username=None):
        print(username)
        if username:
            try:
                user = User.objects.get(username=username)
            except Exception as e:
                print('-get user error is %s-' % e)
                result = {'code': 10104, 'error': 'user not exist'}
                return JsonResponse(result)
            # get search data
            keys = request.GET.keys()
            if keys:
                data = {}
                for key in keys:
                    if key == 'password':
                        continue
                    if hasattr(user, key):
                        data[key] = getattr(user, key)
                result = {'code': 200, 'username': username, 'data': data}
            else:
                # get all data
                result = {'code': 200, 'username': username,
                          'data': {'info': user.Delivery_address1, 'sign': user.sign, 'gender': user.gender,
                                   'year': user.birthday.year, 'province': user.province, 'city': user.city,
                                   'district': user.district, 'month': user.birthday.month, 'day': user.birthday.day,
                                   'nickname': user.nickname, 'avatar': str(user.IMAGE)}}

            return JsonResponse(result)
        else:
            pass

        return HttpResponse('--users get--')


    def post(self,request):
        json_str=request.body
        json_obj =json.loads(json_str)
        username=json_obj['username']
        nickname = json_obj['nickname']
        email=json_obj['email']
        phone=json_obj['phone']
        password1=json_obj['password1']
        password2=json_obj['password2']
        code = json_obj['code']
        redis_code= cache.get('sms_%s'%phone)
        print(code)
        print(redis_code)
        # if code!=redis_code:
        #     result = {'code': 10103, 'error': '验证码错误！'}
        #     return JsonResponse(result)
        print(username,email,phone,password1,password2)
        if len(username)>11:
            result={'code':10100, 'error':'用户名太长！'}
            return JsonResponse(result)
        print(username)
        old_user= User.objects.filter(username=username)
        print(old_user)
        if password1 !=password2:
            result = {'code': 10102, 'error': "两次密码不一致"}
            return JsonResponse(result)
            # hash
        md5 = hashlib.md5()
        md5.update(password1.encode())
        password_h = md5.hexdigest()
        print(password_h,nickname,username)
        if old_user and email and phone:
            result = {'code': 10101, 'error': "用户名已被使用"}
            return JsonResponse(result)
        elif (old_user and not email) and phone:
            print(phone)
            old_user[0].TELEPHONE = phone
            old_user[0].save()
            result = {'code': 200, 'username': old_user[0].username}
            return JsonResponse(result)
        elif old_user and not email and not phone:
            old_user[0].password = password_h
            old_user[0].nickname = nickname
            old_user[0].save()
            result = {'code': 200, 'username': old_user[0].username}

            return JsonResponse(result)
        else:
            try:
                User.objects.create(username=username,password=password_h,EMAIL=email,TELEPHONE=phone)
            except Exception as e:
                print('error is %s' % e)
                return JsonResponse('user name exist', safe=False)
            token= makeToken(username)
            return JsonResponse({'code':200 ,'username':username, 'data':{'token':token.decode()}})


def makeToken(username, expire=3600 * 24):
    now = time.time()
    payload = {'username': username, 'exp': now + expire}
    key = settings.JWT_TOKEN_KEY
    return jwt.encode(payload, key, algorithm='HS256')


def getResult(r):
    while True:
        if r.ready():
            return r.result
            break


def sms_view(request):
    json_str = request.body
    json_obj = json.loads(json_str)
    phone = json_obj['phone']
    code = random.randint(1000, 9999)
    cache_key = 'sms_%s' % phone

    cache.set(cache_key, code, 65)
    print('--send code -- is %s' % code)

    # x=YunTongXin(settings.SMS_ACCOUNT_ID,settings.SMS_ACCOUNT_TOKEN,settings.SMS_APP_ID,settings.SMS_TEMPLATE_ID)
    # res= x.run(phone,code)
    res = get_res.delay(phone, code)
    # print(res)
    # res = getResult(res)

    print('--send sms result is %s' % res)
    return JsonResponse({'code': 200, 'sms': code})


# 用户about页面的相关数据返还
@login_check
def about_view(request):
    user = request.myuser
    avatar = str(user.IMAGE)
    wallet = UserWallet.objects.filter(user_id=user.id).last()
    if wallet:
        balance = wallet.total_balance
        result = {"code": 200, "balance": balance, "avatar": avatar}
        return JsonResponse(result)
    else:
        result = {"code": 200, "balance": 0, "avatar": avatar}
        return JsonResponse(result)

@login_check
def balance_view(request):
    user = request.myuser
    avatar = str(user.IMAGE)
    wallet = UserWallet.objects.filter(user_id=user.id).last()
    # 若存在余额充值订单
    if wallet:
        available = wallet.available_balance
        total = wallet.total_balance
        unavailable = total - available
        result = {"code": 200, "available": available, "total": total, "unavailable": unavailable, "avatar": avatar}
        return JsonResponse(result)
    # 没有充值记录
    else:
        result = {"code": 200, "available": 0, "total": 0, "unavailable": 0, "avatar": avatar}
        return JsonResponse(result)



# # Create your views here.
# from .models import User
# import hashlib
# def login_view(request):
#     if request.method=='GET':
#         if 'uname' in request.session and 'uid' in request.session:
#             return JsonResponse('already login', safe=False)
#             # HttpResponse('already login')
#         uname = request.COOKIES.get('uname')
#         uid= request.COOKIES.get('uid')
#         if uname and uid:
#             request.session['uname']=uname
#             request.session['uid']=uid
#             return JsonResponse('already login', safe=False)
#             # return HttpResponse('already login')
#         return render(request, 'users/login.html')
#     elif request.method=='POST':
#         print(request.POST)
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         print(username)
#         if not username or not password:
#             # error='not exist'
#             return JsonResponse('account or password wrong', safe=False)
#             # return render(request, 'users/login.html', locals())
#         try:
#             user=User.objects.get(username=username)
#         except Exception as e:
#             # error = 'account or password wrong'
#             return JsonResponse('account or password wrong', safe=False)
#             # return render(request, 'users/login.html', locals())
#             # return HttpResponse('account or password wrong')
#
#         md5= hashlib.md5()
#         md5.update(password.encode())
#         password_h=md5.hexdigest()
#         if password_h!=user.password:
#             # error = 'account or password wrong'
#             return JsonResponse('account or password wrong', safe=False)
#             # return render(request, 'users/login.html', locals())
#     request.session['uname']=user.username
#     request.session['uid']=user.id
#     resp=HttpResponse('scuuess')
#     if 'remember' in request.POST:
#         resp.set_cookie('uname',user.username,7*3600*24)
#         resp.set_cookie('uid',user.id,7*3600*24)
#     return resp
#
# def reg_view(request):
#     if request.method=='GET':
#         return render(request, 'users/reg.html')
#     elif request.method=='POST':
#         username=request.POST.get('username')
#         password1=request.POST.get('password1')
#         password2=request.POST.get('password2')
#         print(username)
#         if not username or not password1 or not password2:
#             return JsonResponse('can not be null', safe=False)
#             # return HttpResponse('can not be null')
#         if not password1==password2:
#             # return HttpResponse('password must same')
#             return JsonResponse('password must be same', safe=False)
#         old_user=User.objects.filter(username=username)
#         if old_user:
#             return JsonResponse('user name exist', safe=False)
#             # return HttpResponse('user name exist')
#         md5= hashlib.md5()
#         md5.update(password1.encode())
#         password_h=md5.hexdigest()
#         try:
#             User.objects.create(username=username,password=password_h)
#         except Exception as e:
#             print('error is %s' % e)
#             # return HttpResponse('user name exist')
#             return JsonResponse('user name exist', safe=False)
#         # return HttpResponse('reg success')
#         return JsonResponse('reg success', safe=False)
#
# def logout_view(request):
#     if 'uname' in request.session:
#         del request.session['uname']
#     if 'uid' in request.session:
#         del request.session['uid']
#
#     resp = HttpResponse('success')
#     if 'uname' in request.COOKIES:
#         resp.delete_cookie('uname')
#     if 'uid' in request.COOKIES:
#         resp.delete_cookie('uid')
#     return resp
#
# @csrf_exempt
# def upload_view_dj(request):
#     if request.method == 'GET':
#         return render(request, 'users/upload_userinfo.html')
#     elif request.method == 'POST':
#         try:
#             username =request.POST['username']
#             # password =
#             IMAGE = request.FILES['myfile']
#             nickname =request.POST['nickname']
#             lastname =request.POST['lastname']
#             firstname =request.POST['firstname']
#             country =request.POST['country']
#             province =request.POST['province']
#             city =request.POST['city']
#             gender =request.POST['gender']
#             age =request.POST['age']
#             birthday =request.POST['birthday']
#             status =0
#             Delivery_address1 =request.POST['Delivery_address1']
#             Delivery_address2 =request.POST['Delivery_address2']
#             EMAIL =request.POST['EMAIL']
#             TELEPHONE =request.POST['TELEPHONE']
#
#             User.objects.create(username=username,IMAGE=IMAGE,nickname=nickname,lastname=lastname,firstname=firstname,country=country,province=province,city=city,gender=gender
#                                 ,age=age,birthday=birthday,status=status,Delivery_address1=Delivery_address1,Delivery_address2=Delivery_address2,EMAIL=EMAIL,TELEPHONE=TELEPHONE)
#         except Exception as e:
#             return HttpResponse(e)
#
#
#         return HttpResponse('----upload userinfo is ok-----')
