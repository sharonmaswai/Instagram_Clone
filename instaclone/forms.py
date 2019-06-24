from .models import Image, Profile
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user_id']
class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'profile','comments', 'image_name']
       