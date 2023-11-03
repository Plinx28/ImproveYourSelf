from django.db import models
from django.urls import reverse
from users.models import Person

class Article(models.Model):
    """ Модель статьи."""
    title = models.CharField(max_length=300)
    text = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    pub_date = models.DateField(auto_created=True, verbose_name='publication date')
    update_date = models.DateField(auto_now_add=True, verbose_name='update date')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    # author_username = models.ForeignKey('Person', on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article', kwargs={'article_slug': self.slug})
    
    class Meta:
        verbose_name = 'Articles'
        verbose_name_plural = 'Articles'
        ordering = ['-pub_date', 'title']