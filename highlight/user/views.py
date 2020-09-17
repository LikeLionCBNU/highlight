from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password_confirm"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password"],
                email=request.POST["email"],
            )
            auth.login(request,user)
            return redirect('user:login')
        return render(request, 'user/signup.html')
    return render(request, 'user/signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            print("인증성공")
            auth.login(request, user)
            return redirect('main')
        else:
            print("인증실패")
            return render(request, 'user/login_test.html', {'error': '사용자ID 혹은 비밀번호가 잘못되었습니다.'})
    else:
        return render(request, 'user/login.html')

def logout(request):
    auth.logout(request)
    return redirect('user:login')

def mypage(request):
    return render(request, 'home')