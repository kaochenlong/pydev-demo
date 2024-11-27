from django.shortcuts import render


def login(request):
    return render(request, "users/login.html")


def register(request):
    if request.POST:
        # 註冊
        # redirect 首頁
        pass
    return render(request, "users/register.html")


def logout(request):
    pass
