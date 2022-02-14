from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from pages.models import Page


class HomePageView(TemplateView):
    template_name = "home.html"


class PageDetailView(DetailView):
    model = Page
