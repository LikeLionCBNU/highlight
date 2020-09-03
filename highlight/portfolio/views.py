from django.shortcuts import render, get_object_or_404, redirect
from .models import Portfolio, Review
from django.utils import timezone
from .forms import PortfolioForm

# Create your views here.
def detail(request, portfolio_id):
    portfolio_detail = get_object_or_404(Portfolio, pk = portfolio_id)
    return render(request, 'portfolio/detail.html', {'portfolio' : portfolio_detail})

def portfolio_new(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolio = form.save(commit=False)
            # request.user.is_authenticated
            portfolio.save()
            return redirect('detail', portfolio_id = portfolio.pk)
    else:
        form = PortfolioForm()
    return render(request, 'portfolio/portfolio_new.html', {'form': form})