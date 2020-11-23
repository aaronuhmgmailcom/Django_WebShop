import csv

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="mybook.csv"'
    writer =csv.writer(response)
    writer.writerow(['编号','名称'])
    books= [{'id':1,'name':'python'},{'id':2,'name':'Java'},{'id':3,'name':'c++'},{'id':4, 'name':'c'}]
    for b in books:
        writer.writerow([b['id'],b['name']])

    return response