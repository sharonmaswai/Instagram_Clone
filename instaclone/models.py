from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Image(models.Model):
    image = models.ImageField(upload_to = 'articles/')
    image_name = models.CharField(max_length=30)
    image_caption = HTMLField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.CharField(max_length =50)
    comments = models.CharField(max_length =50)

