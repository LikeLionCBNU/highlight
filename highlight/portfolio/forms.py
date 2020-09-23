from django import forms
from .models import Portfolio, Review

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = {'title', 'content', 'production', 'profile', 'price', 'career', }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = {'content', 'grade', }