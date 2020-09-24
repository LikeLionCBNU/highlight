from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('<int:portfolio_id>/', views.detail, name = 'detail'),
    path('new/', views.portfolio_new, name = 'new'),
    path('<int:portfolio_id>/edit/', views.portfolio_edit, name = 'edit'),
    path('<int:portfolio_id>/delete/', views.portfolio_delete, name = 'delete'),
    path('<int:portfolio_id>/review_new/', views.review_new, name = 'review_new'),
    path('<int:review_id>/review_delete/', views.review_delete, name = 'review_delete'),

]