from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Create your models here.

class Community(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    content = models.TextField(max_length=800)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:30]

class Community_Reply(models.Model):
    post = models.ForeignKey(Community, related_name="community_replys", on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    reply_at = models.DateTimeField(auto_now_add=True)
    reply_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def approve(self):
        self.save()

    def __str__(self):
        return self.content