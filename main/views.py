from typing import Any
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Article
from .utils import DataMixin

# Это пример использования отображения данных из БД
class IndexView(DataMixin, ListView):

    template_name = 'main/index.html'
    model = Article

    context_object_name = 'articles'

    def get_queryset(self):
        '''Return the last three published articles.'''
        return Article.objects.order_by("-pub_date")

def aboutUsView(request):
    return render(request, 'main/about.html')

def contactsView(request):
    return render(request, 'main/contacts.html')

class ArticleView(DetailView):
    template_name = 'main/article.html'
    model = Article

    slug_url_kwarg = 'article_slug'

