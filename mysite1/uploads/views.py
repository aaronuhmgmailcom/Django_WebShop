import csv

from django.http import HttpResponse
from django.shortcuts import render

from .models import Content


def test_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="mybook.csv"'
    writer =csv.writer(response)
    writer.writerow(['编号','名称'])
    books= [{'id':1,'name':'python'},{'id':2,'name':'Java'},{'id':3,'name':'c++'},{'id':4, 'name':'c'}]
    for b in books:
        writer.writerow([b['id'],b['name']])

    return response

# file views.py
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import os

@csrf_exempt
def upload_view(request):
    if request.method == 'GET':
        return render(request, 'uploads/test_upload.html')
    elif request.method == "POST":
        title = request.POST['title']
        a_file = request.FILES['myfile']
        # method1:
        # print("上传文件名是:", a_file.name)
        # filename =os.path.join(settings.MEDIA_ROOT, a_file.name)
        # with open(filename, 'wb') as f:
        #     data = a_file.file.read()
        #     f.write(data)
        # method12:
        Content.objects.create(title=title,myfile=a_file)

        return HttpResponse("接收文件:" + a_file.name + "成功")