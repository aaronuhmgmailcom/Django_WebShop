from django.urls import path
from . import views
urlpatterns = [
    path('<str:author_id>', views.topic_views.as_view()),
    # path('<str:author_id>', views.topic_views.as_view()),


]