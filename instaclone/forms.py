from .models import Image, Profile, Comment
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user_id']
class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'profile','comments', 'image_name']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image', 'user_comment']

      