from django.db.models import Model, SET_DEFAULT, CASCADE
from django.db.models import TextField, ImageField, CharField, SlugField, ForeignKey, DateTimeField
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Article(Model):
    """ Модель статьи."""
    title = CharField(max_length=300)
    text = TextField()
    image = ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    pub_date = DateTimeField(auto_now_add=True, verbose_name='publication date')
    update_date = DateTimeField(auto_now=True, verbose_name='update date')
    slug = SlugField(auto_created=True, max_length=255, unique=True, db_index=True, verbose_name="URL")
    author = ForeignKey(to=User, default='Community', on_delete=SET_DEFAULT)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article', kwargs={'article_slug': self.slug})
    
    class Meta:
        verbose_name = 'Articles'
        verbose_name_plural = 'Articles'
        ordering = ['-pub_date', 'title']

class Comment(Model):
    """Модель комментариев."""
    author = ForeignKey(to=User, on_delete=CASCADE)
    text = TextField()
    date = DateTimeField(auto_now_add=True)