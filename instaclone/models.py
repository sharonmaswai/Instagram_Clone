from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Profile(models.Model):
    user_id = models.IntegerField(default=0)
    profile_photo= models.ImageField(upload_to = 'profiles/', blank = True)
    bio=models.CharField(max_length =50)
   
    
  
    def save_profile(self):
        self.save()

    def __str__(self):
        return self.bio

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length=30, default='paint')
    image_caption = HTMLField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.CharField(max_length =50)
    comments = models.CharField(max_length =50)

