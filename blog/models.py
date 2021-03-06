from django.conf import settings
from django.db import models
from django.utils import timezone


class Config(models.Model):
    key = models.CharField(max_length=50, blank=False, unique=True)
    value = models.CharField(max_length=200, blank=False)
    modify_date = models.DateTimeField(default=timezone.now)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    text = models.TextField(blank=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200, blank=False)
    text = models.TextField(blank=False)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like')

    def approve(self):
        self.approve_comment = True
        self.save()

    def __str__(self):
        return self.text
