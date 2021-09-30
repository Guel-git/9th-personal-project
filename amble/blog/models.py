from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class HashTag(models.Model):
    hashtag_name = models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag_name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    content = models.TextField(max_length=2000)
    img = models.ImageField(upload_to='images/')
    hashtag = models.ManyToManyField(HashTag)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:90]

class Blog_Reply(models.Model):
    post = models.ForeignKey(Blog, related_name="blog_replys", on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    reply_at = models.DateTimeField(auto_now_add=True)
    reply_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def approve(self):
        self.save()

    def __str__(self):
        return self.content

