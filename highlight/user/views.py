from django.shortcuts import render, redirect
from .models import User
from .forms import UserLoginForm, UserSignupForm
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password_confirm"]:
            form = UserSignupForm(request.POST)
            if form.is_valid():
                user = User()
                user = form.save(commit=False)
                auth.login(request,user)
                return redirect('main')
            else:
                form = UserSignupForm()
                print('form not valid')
                print(form.errors)
                return render(request, 'user/signup.html',{'form':form})
        else:
            form = UserSignupForm()
            print('비밀번호와 비밀번호 확인이 다름')
            return render(request, 'user/signup.html',{'form':form})
    else:
        form = UserSignupForm()
        print('request not post')
        return render(request, 'user/signup.html',{'form':form})


# def signup(request):
#     form = UserSignupForm()
#     if request.method == "POST":
#         if form.is_valid():
#             if request.POST["password"] == request.POST["password_confirm"]:
#                 user = form.save(commit=False)
#                 auth.login(request,user)
#                 return redirect('user:login')
#             else:
#                 return render(request, 'user/signup.html')
#         else:
#             form = UserSignupForm()
#         return render(request, 'user/signup.html',{'form':form})
#     return render(request, 'user/signup.html',{'form':form})

    


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