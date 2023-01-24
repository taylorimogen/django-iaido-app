from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

# Create your models here.

# Person model
class Person(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    username = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=60)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

