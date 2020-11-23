# Create your views here.
from django.core import mail
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import hashlib

from django.utils import html

from .models import Order

def login_check(fn):
    def wrap(request,*args,**kwargs):
        if 'uname' not in request.session or 'uid' not in request.session:
            c_uname=request.COOKIES.get('uname')
            c_uid=request.COOKIES.get('uid')
            if not c_uname or not c_uid:
                return HttpResponseRedirect('/users/login')
            else:
                request.session['uname']=c_uname
                request.session['uid']=c_uid
        return fn(request,*args,**kwargs)
    return wrap

@login_check
def add_view(request):
    if request.method=='GET':
        return render(request,'orders/add_order.html')
    elif request.method=='POST':
        title= request.POST.get('title')
        content=request.POST.get('content')
        title=html.escape(title)
        content=html.escape(content)
        uid= request.session['uid']
        note= Order.objects.create(title=title, content=content,user_id=uid)

        return HttpResponseRedirect('list')

@login_check
def list_view(request):
    order = Order.objects.all()
    # mail.send_mail('mail test', 'hello world', '54778723@qq.com', ['82780270@qq.com'])
    paginator = Paginator(order, 2)
    cur_page = request.GET.get('page', 1)  # 得到默认的当前页
    page = paginator.page(cur_page)
    # return render(request, 'bookstore/book.html', locals())
    # return render(request, 'bookstore/all_book.html', locals())

    return render(request, 'orders/list_order.html', locals())
    # return render(request,'note/list_note.html')

@login_check
def update_order(request,id):
    try:
        order = Order.objects.get(id=id)
    except Exception as e:
        print('error is %s'% e)
        return HttpResponse('order id is wrong')
    if request.method=='GET':
        return render(request, 'orders/update_order.html', locals())
    elif request.method=='POST':
        order.title = request.POST.get('title')
        order.content = request.POST.get('content')
        order.save()
        return HttpResponseRedirect('/orders/list')

@login_check
def delete_order(request):
    if request.method=="GET":
        id= int(request.GET.get('id'))
        print(id)
        book =  Order.objects.get(id=id)
        book.delete()
    return HttpResponseRedirect('/orders/list')