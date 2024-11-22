from django.shortcuts import render, redirect
from .models import Resume


def index(request):
    if request.POST:
        resume = Resume()
        resume.title = request.POST.get("title")
        resume.skill = request.POST.get("skill")
        resume.content = request.POST.get("content")
        resume.save()

        return redirect("resumes:index")

    # 讀取 resume 列表
    resumes = Resume.objects.all()
    return render(
        request,
        "resumes/index.html",
        {"resumes": resumes},
    )


def new(request):
    return render(request, "resumes/new.html")
