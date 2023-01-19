from django.db import models

# Create your models here.

# Person model
class Person(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
