from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/<int:portfolio_id>/', views.detail, name = 'detail'),
    path('portfolio/new/', views.portfolio_new, name = 'new'),
]