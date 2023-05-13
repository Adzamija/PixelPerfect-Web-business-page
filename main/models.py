from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Blog(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=64)
    time = models.TimeField()
    image = models.CharField(max_length=5000)
    tag = models.CharField(max_length=64)
    description = models.CharField(max_length=5000)
    short_description = models.CharField(max_length=2000, default='SOME STRING')

class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.CharField(max_length=5000)


class Portfolio(models.Model):
    title = models.CharField(max_length=64)
    short_description = models.CharField(max_length=2000)
    description = models.CharField(max_length=5000)
    photo_1300 = models.CharField(max_length=5000)
    photo1_600 = models.CharField(max_length=5000)
    photo2_600 = models.CharField(max_length=5000)
