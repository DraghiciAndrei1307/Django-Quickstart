from django.db import models
import django.contrib.auth.models
# Create your models here.

class Company(models.Model):

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class User(django.contrib.auth.models.User):

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Group(django.contrib.auth.models.Group):

    employed = models.BooleanField(default=False)
