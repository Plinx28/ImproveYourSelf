from django.forms import CharField, Textarea
from django.forms import Textarea, TextInput, DateField, ModelForm, Form
from captcha.fields import CaptchaField
from .models import Article

class ContactForm(Form):
    name = CharField(max_length=150)
    content = CharField(widget=Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()
    

class CreateArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'text', 'image')
        widgets = {
            'title': TextInput(attrs={'class': 'form-input'}),
            'content': Textarea(attrs={'cols': 60, 'rows': 10}),
        }



    # title = CharField(max_length=300)
    # text = TextField()
    # image = ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    # pub_date = DateField(auto_created=True, verbose_name='publication date')
    # update_date = DateField(auto_now_add=True, verbose_name='update date')
    # slug = SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    # author = CharField(max_length=250, auto_created=True)