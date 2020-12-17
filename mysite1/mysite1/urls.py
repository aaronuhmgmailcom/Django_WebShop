"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
from users import views as user_views
from btoken import views as btoken_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment/', include('payment.urls')),
    path('', views.index_view),
    path('cors', views.cors),
    path('cors_server', views.cors_server),
    path('v1/users', user_views.UsersView.as_view()),
    path('v1/tokens', btoken_views.TokenView.as_view()),
    path('users/', include('users.urls')),
    path('useraddress/', include('useraddress.urls')),
    path('topics/', include('topic.urls')),
    path("order/", include("order.urls")),
    path('product/', include('product.urls')),
    path('orders/', include('orders.urls')),
    path('download/', include('download.urls')),
    path('uploads/', include('uploads.urls')),
    path('messages/', include('message.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
