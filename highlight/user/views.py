from django.shortcuts import render, redirect
from .models import User
from .forms import UserLoginForm, UserSignupForm
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password_confirm"]:
            form = UserSignupForm(request.POST)
            print(form.errors)

            if form.is_valid():
                user = User()
                user = form.save(commit=False)
                user.save()
                auth.login(request,user)
                return redirect('main')
            else:
                form = UserSignupForm()
                print('form not valid')
                return render(request, 'user/signup.html',{'form':form})
        else:
            form = UserSignupForm()
            print('비밀번호와 비밀번호 확인이 다름')
            return render(request, 'user/signup.html',{'form':form})
    else:
        form = UserSignupForm()
        print('request not post')
        return render(request, 'user/signup.html',{'form':form})


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


    # 경욱님
    # 포트폴리오 평점 적용
    # 리뷰 필터링
    # 검색하기 기능 