from django.contrib import admin

# Register your models here.
from .models import UserAddress

admin.site.register(UserAddress)