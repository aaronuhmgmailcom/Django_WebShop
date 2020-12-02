from django.urls import path
from . import views
urlpatterns = [
    #http://127.0.0.1:8000/v1/users/tedu
    path('<str:username>', views.UsersView.as_view()),


    # path('login', views.login_view),
    # path('reg', views.reg_view),
    # path('logout', views.logout_view),
    # path('userinfo', views.upload_view_dj),

]