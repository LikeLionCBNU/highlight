from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    return render(request, 'user/signup.html')


def login(request):
    return render(request, 'user/login.html')

def logout(request):
    auth.logout(request)
    return redirect(request,'home')

