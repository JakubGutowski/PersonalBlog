from django.db import models
from datetime import datetime


class VisitorIp(models.Model):
    pub_date = models.DateTimeField('GET reqest date ', default=datetime.now())
    ip_address = models.GenericIPAddressField()

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    commitDate = models.DateTimeField(auto_now=True)
    pubDate = models.DateTimeField(null=True)
    author = models.CharField(max_length=20, default='Gutech')


class PostComments(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    nick = models.CharField(max_length=20)
    comment = models.CharField(max_length=140)
    pubDate = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.comment
# Create your models here.
