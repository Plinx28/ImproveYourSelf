from django.contrib import admin
from .models import Profile

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'birth_date')
    list_display_links = ('user', )

admin.site.register(Profile, ArticleAdmin)

