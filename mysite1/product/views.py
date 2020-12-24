from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from .models import Product
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
import hashlib
import time
import jwt
from django.conf import settings


class ProductView(View):
    def get(self, request, pid=None):
        print(pid)
        if pid:
            try:
                p = Product.objects.get(id=pid)
            except Exception as e:
                print('-get Product error is %s-' % e)
                result = {'code': 10104, 'error': 'Product not exist'}
                return JsonResponse(result)
            # get search data

            result = {'code': 200, 'productname': p.product_name,
                      'class_ids': p.class_ids, 'img': str(p.img), 'img2': str(p.img2),
                      'img3': str(p.img3), 'img4': str(p.img4), 'img5': str(p.img5),
                      'description': p.description, 'price': p.price, 'discount': p.discount,
                      'amount': p.amount, 'productor': p.productor, 'author': p.author, 'status': p.status}

            return JsonResponse(result)
        else:
            pass

        return HttpResponse('--users get--')


def list_view(request):
    product = Product.objects.all()
    # mail.send_mail('mail test', 'hello world', '54778723@qq.com', ['82780270@qq.com'])
    paginator = Paginator(product, 2)
    cur_page = request.GET.get('page', 1)  # 得到默认的当前页
    page = paginator.page(cur_page)
    # return render(request, 'bookstore/book.html', locals())
    # return render(request, 'bookstore/all_book.html', locals())

    return render(request, 'product/list_product.html', locals())
    # return render(request,'note/list_note.html')

def book_load(request):
    book_all=Product.objects.all()
    book1_list = []
    book2_list = []
    book3_list = []
    book4_list=[]
    for book in book_all:
        item = {}
        item['id'] = book.id
        item['img']="http://47.94.174.118:8000"+str(book.img)
        item['product_name']=book.product_name
        item['price']=book.price
        if book.class_ids == "1":
            book1_list.append(item)
        if book.class_ids == "2":
            book2_list.append(item)
        if book.class_ids == "3":
            book3_list.append(item)
        if book.class_ids=="4":
            book4_list.append(item)
    data = [book1_list, book2_list, book3_list,book4_list]
    print(data)
    result = {}
    result['code'] = 200
    result['data'] = data
    return JsonResponse(result)