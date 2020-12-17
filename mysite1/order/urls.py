from django.urls import path
from . import views

urlpatterns = [
    path("search", views.OrdersView.as_view()),
]
