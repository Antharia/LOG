from django.urls import path
from . import views


urlpatterns = [
    path("", views.article_list, name="article_list"),
    path("<slug:slug>", views.article_detail, name="article_detail"),
    path("tags/<slug:slug>", views.articles_by_tag, name="articles_by_tag"),
]
