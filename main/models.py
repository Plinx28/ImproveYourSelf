from django.db import models
from django.db.models import TextField, ImageField, CharField, SlugField, DateField
from django.urls import reverse

class Article(models.Model):
    """ Модель статьи."""
    title = CharField(max_length=300)
    text = TextField()
    image = ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    pub_date = DateField(auto_created=True, verbose_name='publication date')
    update_date = DateField(auto_now_add=True, verbose_name='update date')
    slug = SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    author = CharField(max_length=250, auto_created=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article', kwargs={'article_slug': self.slug})
    
    class Meta:
        verbose_name = 'Articles'
        verbose_name_plural = 'Articles'
        ordering = ['-pub_date', 'title']