from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from .models import Rotation


def load(request):
    carousel_all = Rotation.objects.all()
    mycarousel_list=[]
    floorcarousel_list=[]
    floorcarousell_list=[]
    for carousel in carousel_all:
        item = {}
        item['src'] = "http://47.94.174.118:8000/media/"+str(carousel.img_path)
        item['href'] = carousel.link
        if carousel.type=="0":
            mycarousel_list.append(item)
        if carousel.type=="1":
            floorcarousel_list.append(item)
        if carousel.type=="2":
            floorcarousell_list.append(item)
    data=[mycarousel_list,floorcarousel_list,floorcarousell_list]
    print(data)
    result={}
    result['code']=200
    result['data']=data
    return JsonResponse(result)