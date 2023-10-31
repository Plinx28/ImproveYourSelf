from django.forms import CharField, Textarea
from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    name = CharField(max_length=150)
    content = CharField(widget=Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()
    


