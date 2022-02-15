from django.urls import path
from .views import ArticleListView, ArticleDetailView


urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("<slug:slug>", ArticleDetailView.as_view(), name="article_detail"),
]