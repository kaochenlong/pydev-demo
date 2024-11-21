from django.shortcuts import render


def home(request):
    return render(request, "resumes/home.html")


def new(request):
    return render(request, "resumes/new.html")
