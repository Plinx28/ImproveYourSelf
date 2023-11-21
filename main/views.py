from django.http import HttpResponse
from django.db import transaction
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.views.generic import ListView, DetailView, FormView, CreateView

from .models import Article
from .utils import DataMixin
from .forms import ContactForm, CreateArticleForm


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

    def get_context_data(self):
        context = {'action': 'Create',
                   'form': self.form_class}
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
@transaction.atomic
def edit_article_view(request, article_slug):
    instance = get_object_or_404(Article, slug=article_slug)
    if request.method == 'POST':
        article_form = CreateArticleForm(request.POST, request.FILES, instance=instance)
        if article_form.is_valid():
            article_form.save()
            messages.success(request, 'Your article was successfully updated!')
            return redirect(f'/{instance.slug}')
        else:
            messages.error(request, 'Please correct the error.')
    else:
        article_form = CreateArticleForm(instance=instance)
    return render(request, 'main/create.html', {
        'form': article_form,
        'action': 'Edit'
    })


