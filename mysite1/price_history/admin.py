from django.contrib import admin

# Register your models here.
from .models import PriceHistory

admin.site.register(PriceHistory)