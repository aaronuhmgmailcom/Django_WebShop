import jwt
from django.conf import settings
from django.http import JsonResponse
from users.models import User
def login_check(func):
    def wrap(request,*args,**kwargs):
        #从请求头获取token
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            result={'code':403 ,'error':'please login'}
            return JsonResponse(result)
        try:
            payload = jwt.decode(token,settings.JWT_TOKEN_KEY,algorithms='HS256')
        except Exception as e:
            print('check login error %s'% e)
            result = {'code': 403, 'error': 'please login'}
            return JsonResponse(result)
        username=payload["username"]
        user= User.objects.get(username=username)
        request.myuser=user
        return func(request,*args,**kwargs)
    return wrap

def get_user_by_request(request):
    token=request.META.get('HTTP_AUTHORIZATION')
    if not token:
        return None
    try:
        payload = jwt.decode(token, settings.JWT_TOKEN_KEY, algorithms='HS256')
    except Exception as e:
        print('get user jwt is error %s'%e)
        return None
    username = payload["username"]
    return username
