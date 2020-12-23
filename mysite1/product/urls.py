from django.urls import path

from . import views

urlpatterns = [

    # path('<int:pid>',views.list_view,name='list'),

    path('<str:pid>', views.ProductView.as_view()),
    # path('reg', views.reg_view),
    # path('logout', views.logout_view),
    # path('userinfo', views.upload_view_dj),
    path('book_load', views.book_load),
]