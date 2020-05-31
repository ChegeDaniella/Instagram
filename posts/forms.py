from django import forms
from .models import Post, User,Profile

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['image_profile']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields  = ['username','email' ]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
         
