from django.shortcuts import render, get_object_or_404, redirect
from .models import Portfolio, Review
from django.utils import timezone
from .forms import PortfolioForm, ReviewForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    portfolio = Portfolio.objects.all()
    paginator = Paginator(portfolio, 5)
    page = request.GET.get('page')
    portfolio = paginator.get_page(page)
    return render(request, 'portfolio/portfolio_main.html', {'portfolio':portfolio})

def detail(request, portfolio_id):
    portfolio_detail = get_object_or_404(Portfolio, pk = portfolio_id)
    reviewForm = ReviewForm()
    return render(request, 'portfolio/portfolio_detail.html', {'portfolio' : portfolio_detail, 'reviewForm' : reviewForm})

def portfolio_new(request):
    if request.user.user_type == 'editor': 
        if request.method == "POST":
            form = PortfolioForm(request.POST)
            if form.is_valid():
                portfolio = form.save(commit=False)
                portfolio.editor = request.user
                portfolio.save()
                return redirect('detail', portfolio_id = portfolio.pk)
        else:
            form = PortfolioForm()
        return render(request, 'portfolio/portfolio_new.html', {'form': form})
    else :
        return redirect('main')

def portfolio_edit(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk = portfolio_id)
    if request.user.user_type == 'editor':
        if request.method == "POST":
            form = PortfolioForm(request.POST, instance = portfolio)
            if form.is_valid():
                portfolio = form.save(commit=False)
                portfolio.save()
                return redirect('detail', portfolio_id = portfolio.pk)
        else:
            form = PortfolioForm(instance = portfolio)
        return render(request, 'portfolio/portfolio_edit.html', {'form':form})
    else:
        return redirect('detail', portfolio_id = portfolio.pk)

def portfolio_delete(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    if request.user.user_type == 'editor':
        portfolio.delete()
        return redirect('main')
    else:
        return redirect('detail', portfolio_id = portfolio.pk)

@login_required(login_url='/user/login/')
def review_new(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit = False)
            review.portfolio = get_object_or_404(Portfolio, pk = portfolio_id)
            review.writer = request.user
            review.save()
            return redirect('detail', portfolio_id= portfolio_id)
    else:
        return redirect('detail', portfolio_id = portfolio.pk)

def review_delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    portfolio = review.portfolio
    review.delete()
    return redirect('detail', portfolio_id=portfolio.id)