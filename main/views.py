from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Article
from .utils import DataMixin
from .forms import ContactForm


class IndexView(DataMixin, ListView):
    template_name = 'main/index.html'
    model = Article
    context_object_name = 'articles'

    def get_queryset(self):
        articles_cache = cache.get('articles')

        if articles_cache:
            articles = articles_cache
        else:
            articles = Article.objects.order_by("-pub_date")
            cache.set('articles', articles, 5 * 60)
        return articles


def aboutUsView(request):
    return render(request, 'main/about.html')


class ContactFormView(FormView):
    template_name = 'main/contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form) -> HttpResponse:
        print(form.cleaned_data)
        return redirect('home')


class ArticleView(DetailView):
    template_name = 'main/article.html'
    model = Article

    slug_url_kwarg = 'article_slug'
