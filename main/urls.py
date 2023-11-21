from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('about/', views.aboutUsView, name='about'),
    path('contacts/', views.ContactFormView.as_view(), name='contacts'),
    path('create/', views.CreateArticleView.as_view(), name='create'),
    path('edit-article/<slug:article_slug>/', views.edit_article_view, name='edit_article'),
    path('<slug:article_slug>/', views.ArticleView.as_view(), name='article')
]