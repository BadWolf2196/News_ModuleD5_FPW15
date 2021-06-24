from django.urls import path
from .views import NewsList, NewsDetailView, Search, NewsCreateView, NewsUpdateView, NewsDeleteView

urlpatterns = [

    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetailView.as_view(), name = 'news_detail'),
    path('add/', NewsCreateView.as_view(), name='news_create'),
    path('search/', Search.as_view(), name = 'search'),
    path('<int:pk>/edit', NewsUpdateView.as_view(), name='news_create'),
    path('<int:pk>/delete', NewsDeleteView.as_view(), name='news_delete'),
]