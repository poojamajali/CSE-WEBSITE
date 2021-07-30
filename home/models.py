from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class news(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="home/images",default="")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-show')


class achievements(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="home/images",default="")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('achieve')