from django.urls import path

from . import views

urlpatterns = [
    path('add', views.add_view),
    path('list', views.list_view, name='list'),
    path('update_order/<int:id>', views.update_order),
    path('delete_order', views.delete_order),
    # path('reg', views.reg_view),
    # path('logout', views.logout_view),
]
