from django import forms
from .models import User

class UserSignupForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = {'username', 'email', 'password','user_type', 'name', 'phone_number' }



class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = {'username', 'password'}
