from django import forms
from travelingMechanic.models import webUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class userUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class webUserUpdateForm(forms.ModelForm):
    class Meta:
        model = webUser
        fields = ['profilePic']