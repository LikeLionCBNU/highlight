from django.shortcuts import render, get_object_or_404
from .models import Portfolio, Review

# Create your views here.
def detail(request, portfolio_id):
    portfolio_detail = get_object_or_404(Portfolio, pk = portfolio_id)
    return render(request, 'portfolio/detail.html', {'portfolio' : portfolio_detail})