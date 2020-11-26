from django.contrib import admin

# Register your models here.
from .models import OrderItem

admin.site.register(OrderItem)