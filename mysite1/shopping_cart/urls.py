from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>', views.cartView.as_view()),


]
