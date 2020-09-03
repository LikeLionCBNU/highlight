from django.urls import path
from . import views

urlpatterns = [
    path('<int:portfolio_id>/', views.detail, name = 'detail'),
    path('new/', views.portfolio_new, name = 'new'),
]