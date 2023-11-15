from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Article
from .utils import DataMixin
from .forms import ContactForm, CreateArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin


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
            cache.set('articles', articles, 1 * 5)
        return articles


def aboutUsView(request):
    return render(request, 'main/about.html')


class ContactFormView(FormView):
    template_name = 'main/contacts.html'
    form_class = ContactForm

    def form_valid(self, form) -> HttpResponse:
        print(form.cleaned_data)
        return redirect('home')


class ArticleView(DetailView):
    template_name = 'main/article.html'
    model = Article

    slug_url_kwarg = 'article_slug'


class CreateArticleView(LoginRequiredMixin, CreateView):
    template_name = 'main/create.html'
    success_url = reverse_lazy('home')
    form_class = CreateArticleForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
