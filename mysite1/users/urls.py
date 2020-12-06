from django.urls import path
from . import views
urlpatterns = [
    path('test_celery', views.test_celery),
    path('', views.UsersView.as_view()),
    #http://127.0.0.1:8000/v1/users/sms
    path('sms',views.sms_view),
    #http://127.0.0.1:8000/v1/users/tedu
    path('<str:username>', views.UsersView.as_view()),
    #http://127.0.0.1:8000/v1/users/tedu/avatar
    path('<str:username>/avatar', views.user_avatar),



    # path('login', views.login_view),
    # path('reg', views.reg_view),
    # path('logout', views.logout_view),
    # path('userinfo', views.upload_view_dj),

]