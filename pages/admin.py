from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Page

admin.site.register(Page, MarkdownxModelAdmin)
