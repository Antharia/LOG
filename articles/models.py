from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from taggit.managers import TaggableManager


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50)
    content = MarkdownxField()
    tags = TaggableManager()

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "Articles"


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.slug)])

    def formatted_markdown(self):
        return markdownify(self.content)
