from django.http import HttpResponse
from django.shortcuts import render


def index_view(request):
    return render(request,'MasterPage.html')

def cors(request):
    return render(request,'cors.html')


def cors_server(request):
    return HttpResponse('this is cors')