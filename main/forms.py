from django.forms import CharField, Textarea
from django.forms import Textarea, ModelForm, Form
from captcha.fields import CaptchaField
from .models import Article

class ContactForm(Form):
    name = CharField(max_length=150)
    content = CharField(widget=Textarea(attrs={'cols': 80, 'rows': 15}))
    captcha = CaptchaField()


class CreateArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'text', 'image')

