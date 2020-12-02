import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
from users.models import User
import hashlib
from users.views import makeToken

class TokenView(View):
    def get(self,request):
        pass
    def post(self,request):
        json_str=request.body
        json_body=json.loads(json_str)
        username=json_body['username']
        password=json_body['password']
        print(username,password)
        try:
            user=User.objects.get(username=username)
        except Exception as e:
            print('error is %s'%e)
            result = {'code':10200,'error':'用户名或密码错误'}
            return JsonResponse(result)

        md5=hashlib.md5()
        md5.update(password.encode())
        if md5.hexdigest()!= user.password:
            result = {'code': 10201, 'error': '用户名或密码错误'}
            return JsonResponse(result)
        token=makeToken(username)

        return JsonResponse({'code':200, 'username':username, 'data':{'token':token.decode()}})