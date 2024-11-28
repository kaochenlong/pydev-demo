from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as login_user
from django.contrib import messages


def login(request):
    if request.POST:
        # 驗證
        user = authenticate(
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )

        if user is not None:
            login_user(request, user)
            messages.success(request, "登入成功")
            return redirect("pages:home")
        else:
            messages.success(request, "登入失敗")
            return redirect("users:login")

    return render(request, "users/login.html")


def register(request):
    if request.POST:
        # 註冊
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "註冊成功")
            return redirect("pages:home")
        else:
            return HttpResponse(form.error_messages)

    return render(request, "users/register.html")


def logout(request):
    pass
