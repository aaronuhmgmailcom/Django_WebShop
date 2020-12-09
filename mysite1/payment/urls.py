from django.urls import path

from . import views

urlpatterns = [
    path('jump/',views.JumpView.as_view()),


]