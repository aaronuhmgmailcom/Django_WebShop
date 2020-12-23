from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from .models import Rotation


def load(request):
    mycarousel=Rotation.objects.filter(type="0")
    floorcarousel = Rotation.objects.filter(type="1")
    floorcarousell = Rotation.objects.filter(type="2")
    mycarousel_list=[]
    floorcarousel_list=[]
    floorcarousell_list=[]
    for item in mycarousel:
        item_list={}
        item_list['src']=str(item.img_path)
        item_list['href']=item.link
        mycarousel_list.append(item_list)
    for item in floorcarousel:
        item_list={}
        item_list['src'] = str(item.img_path)
        item_list['href'] = item.link
        floorcarousel_list.append(item_list)
    for item in floorcarousell:
        item_list={}
        item_list['src'] = str(item.img_path)
        item_list['href'] = item.link
        floorcarousell_list.append(item_list)
    data=[mycarousel_list,floorcarousel_list,floorcarousell_list]
    result={}
    result['code']=200
    result['data']=data
    return JsonResponse(result)