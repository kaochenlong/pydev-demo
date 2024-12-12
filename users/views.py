from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST


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


@require_POST
@login_required
def logout(request):
    logout_user(request)
    messages.success(request, "已登出")
    return redirect("pages:home")
