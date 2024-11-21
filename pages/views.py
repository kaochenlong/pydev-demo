from django.shortcuts import render


def about(request):
    return render(request, "pages/about.html")


def home(request):
    # 撈資料庫
    return render(request, "pages/home.html")


def contact(request):
    return render(request, "pages/contact.html")


def maintain(request):
    return render(request, "pages/maintain.html")
