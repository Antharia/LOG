from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=64)
    content = MarkdownxField()

    def __str__(self):
        return self.title

    def formatted_content(self):
        return markdownify(self.content)

