from django.db import models
from django.conf import settings
# Create your models here.

class HashTag(models.Model):
    hashtag_name = models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag_name

class Trail(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=200)
    link = models.CharField(max_length=300)
    content = models.TextField(max_length=1000)
    hashtag = models.ManyToManyField(HashTag)

    def __str__(self):
        return self.name