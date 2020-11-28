from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from .models import Product

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
