from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    '''Модель статьи.'''
    title = models.CharField(max_length=300)
    text = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    pub_date = models.DateField(auto_created=True)
    update_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    # author_id = models.ForeignKey(on_delete=PROTECTED)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article', kwargs={'article_slug': self.slug})
    
    class Meta:
        verbose_name = 'Articles'
        verbose_name_plural = 'Articles'
        ordering = ['-pub_date', 'title']