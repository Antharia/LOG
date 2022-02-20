from django.shortcuts import get_object_or_404, render
from .models import Article


def article_list(request):
    article_list = Article.objects.all()
    context = {"article_list": article_list}
    return render(request, "articles/article_list.html", context)

def article_detail(request, slug):
    article = get_object_or_404(Article.objects.all(), slug=slug)
    context = {"article": article}
    return render(request, "articles/article_detail.html", context)
