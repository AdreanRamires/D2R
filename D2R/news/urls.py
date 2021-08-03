from django.urls import path
from .views import latest_news, read_more


urlpatterns = [
    path('news/', latest_news, name='news'),
    path('news-detail/<int:pk>', read_more, name='news detail'),
]
