from .models import Image, Profile
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user_id']
class ImageForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['likes', 'comment', 'image_name']
       