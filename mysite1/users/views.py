from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import User
import hashlib
def login_view(request):
    if request.method=='GET':
        if 'uname' in request.session and 'uid' in request.session:
            return JsonResponse('already login', safe=False)
            # HttpResponse('already login')
        uname = request.COOKIES.get('uname')
        uid= request.COOKIES.get('uid')
        if uname and uid:
            request.session['uname']=uname
            request.session['uid']=uid
            return JsonResponse('already login', safe=False)
            # return HttpResponse('already login')
        return render(request, 'users/login.html')
    elif request.method=='POST':
        print(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        if not username or not password:
            # error='not exist'
            return JsonResponse('account or password wrong', safe=False)
            # return render(request, 'users/login.html', locals())
        try:
            user=User.objects.get(username=username)
        except Exception as e:
            # error = 'account or password wrong'
            return JsonResponse('account or password wrong', safe=False)
            # return render(request, 'users/login.html', locals())
            # return HttpResponse('account or password wrong')

        md5= hashlib.md5()
        md5.update(password.encode())
        password_h=md5.hexdigest()
        if password_h!=user.password:
            # error = 'account or password wrong'
            return JsonResponse('account or password wrong', safe=False)
            # return render(request, 'users/login.html', locals())
    request.session['uname']=user.username
    request.session['uid']=user.id
    resp=HttpResponse('scuuess')
    if 'remember' in request.POST:
        resp.set_cookie('uname',user.username,7*3600*24)
        resp.set_cookie('uid',user.id,7*3600*24)
    return resp

def reg_view(request):
    if request.method=='GET':
        return render(request, 'users/reg.html')
    elif request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        print(username)
        if not username or not password1 or not password2:
            return JsonResponse('can not be null', safe=False)
            # return HttpResponse('can not be null')
        if not password1==password2:
            # return HttpResponse('password must same')
            return JsonResponse('password must be same', safe=False)
        old_user=User.objects.filter(username=username)
        if old_user:
            return JsonResponse('user name exist', safe=False)
            # return HttpResponse('user name exist')
        md5= hashlib.md5()
        md5.update(password1.encode())
        password_h=md5.hexdigest()
        try:
            User.objects.create(username=username,password=password_h)
        except Exception as e:
            print('error is %s' % e)
            # return HttpResponse('user name exist')
            return JsonResponse('user name exist', safe=False)
        # return HttpResponse('reg success')
        return JsonResponse('reg success', safe=False)

def logout_view(request):
    if 'uname' in request.session:
        del request.session['uname']
    if 'uid' in request.session:
        del request.session['uid']

    resp = HttpResponse('success')
    if 'uname' in request.COOKIES:
        resp.delete_cookie('uname')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    return resp

@csrf_exempt
def upload_view_dj(request):
    if request.method == 'GET':
        return render(request, 'users/upload_userinfo.html')
    elif request.method == 'POST':
        try:
            username =request.POST['username']
            # password =
            IMAGE = request.FILES['myfile']
            nickname =request.POST['nickname']
            lastname =request.POST['lastname']
            firstname =request.POST['firstname']
            country =request.POST['country']
            province =request.POST['province']
            city =request.POST['city']
            gender =request.POST['gender']
            age =request.POST['age']
            birthday =request.POST['birthday']
            status =0
            Delivery_address1 =request.POST['Delivery_address1']
            Delivery_address2 =request.POST['Delivery_address2']
            EMAIL =request.POST['EMAIL']
            TELEPHONE =request.POST['TELEPHONE']

            User.objects.create(username=username,IMAGE=IMAGE,nickname=nickname,lastname=lastname,firstname=firstname,country=country,province=province,city=city,gender=gender
                                ,age=age,birthday=birthday,status=status,Delivery_address1=Delivery_address1,Delivery_address2=Delivery_address2,EMAIL=EMAIL,TELEPHONE=TELEPHONE)
        except Exception as e:
            return HttpResponse(e)


        return HttpResponse('----upload userinfo is ok-----')