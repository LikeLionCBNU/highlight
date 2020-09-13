from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = {'title', 'editor', 'content', 'production', 'profile', 'grade', 'price', 'career', }