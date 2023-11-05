from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pub_date')
    list_display_links = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Article, ArticleAdmin)

