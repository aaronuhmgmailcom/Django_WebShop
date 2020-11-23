from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import User
import hashlib
def login_view(request):
    if request.method=='GET':
        if 'uname' in request.session and 'uid' in request.session:
            return HttpResponse('already login')
        uname = request.COOKIES.get('uname')
        uid= request.COOKIES.get('uid')
        if uname and uid:
            request.session['uname']=uname
            request.session['uid']=uid
            return HttpResponse('already login')
        return render(request, 'users/login.html')
    elif request.method=='POST':
        print(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not username or not password:
            return HttpResponse('not be null')
        try:
            user=User.objects.get(username=username)
        except Exception as e:
            return HttpResponse('account or password wrong')

        md5= hashlib.md5()
        md5.update(password.encode())
        password_h=md5.hexdigest()
        if password_h!=user.password:
            return HttpResponse('password wrong')
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
        if not username or not password1 or not password2:
            return HttpResponse('can not be null')
        if not password1==password2:
            return HttpResponse('password must same')
        old_user=User.objects.filter(username=username)
        if old_user:
            return HttpResponse('user name exist')
        md5= hashlib.md5()
        md5.update(password1.encode())
        password_h=md5.hexdigest()
        try:
            User.objects.create(username=username,password=password_h)
        except Exception as e:
            print('error is %s' % e)
            return HttpResponse('user name exist')
        return HttpResponse('reg success')

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

