from django.urls import *
from .views import *


urlpatterns = [
    path('news_list/', news_list, name='news-list'),
    path('detail_news/<int:pk>/', detail_news, name='news-detail'),
    path('create/', NewsCreateView.as_view(), name='create-news'),
    path('edit/<int:pk>/', NewsEditView.as_view(), name='edit-news'),
]