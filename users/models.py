from django.db import models
from users.models import User


class User(models.Model):
    '''Модель пользователя сайта.'''
    nickname = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    password = models.PasswordField()
    create_date = models.DateField(auto_created=True)
    author_id = models.ForeignKey('User', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.nickname