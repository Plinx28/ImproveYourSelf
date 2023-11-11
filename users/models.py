from django.db.models import Model, CASCADE, OneToOneField, DateField, CharField, ImageField
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import GENDER_CHOICES


class Profile(Model):
    """Модель, расширяющая атрибуты пользователя."""
    user = OneToOneField(User, on_delete=CASCADE)
    avatar = ImageField(blank=True, default='images/profile/__default_user_avatar.png', upload_to="images/profile/")
    birth_date = DateField(null=True, verbose_name='birthday date', blank=True)
    gender = CharField(choices=GENDER_CHOICES, max_length=1, blank=True)

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('profile', kwargs={'profile_id': self.user.id})
    
    def save(self, *args, **kwargs):
        super().save()

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ['user']
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User) 
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()