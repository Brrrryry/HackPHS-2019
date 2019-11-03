from django import forms
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth import get_user_model
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
