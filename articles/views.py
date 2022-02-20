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


def articles_by_tag(request, slug):
    article_list = Article.objects.filter(tags__slug=slug)
    context = {"article_list": article_list, "slug": slug}
    return render(request, "articles/articles_by_tag.html", context)


#  class ArticleTagListView(ListView):
#      model = Article
#      context_object_name = "article_list"
#      template_name = "articles/articles_by_tag.html"
#
#      def get_queryset(self):
#          return Article.objects.filter(tags__slug=self.kwargs.get("tag_slug"))
