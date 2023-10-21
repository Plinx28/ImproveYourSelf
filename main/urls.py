from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('about/', views.aboutUsView, name='about'),
    path('contacts/', views.contactsView, name='contacts'),
    path('<slug:article_slug>/', views.ArticleView.as_view(), name='article')
]