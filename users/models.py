# from django.db.models import Model, CASCADE, OneToOneField, DateField, CharField, EmailField
# from django.urls import reverse
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# class Person(Model):
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female')
#     )

#     user = OneToOneField(User, on_delete=CASCADE)
#     birth_date = DateField(null=True, verbose_name='birthday date')
#     gender = CharField(choices=GENDER_CHOICES, max_length=1)

#     def __str__(self):
#         return self.user
    
# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Person.objects.create(user=instance)
#     instance.profile.save()

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()