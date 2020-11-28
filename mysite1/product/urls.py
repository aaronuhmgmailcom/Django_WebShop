from django.urls import path

from . import views

urlpatterns = [

    path('all',views.list_view,name='list'),
    # path('reg', views.reg_view),
    # path('logout', views.logout_view),
    # path('userinfo', views.upload_view_dj),

]