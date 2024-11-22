from django.shortcuts import render, redirect, get_object_or_404
from .models import Resume
from django.contrib import messages


def index(request):
    if request.POST:
        resume = Resume()
        resume.title = request.POST.get("title")
        resume.skill = request.POST.get("skill")
        resume.content = request.POST.get("content")
        resume.save()

        messages.success(request, "新增成功")

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


def show(request, id):
    resume = get_object_or_404(Resume, id=id)

    if request.POST:
        # 更新
        resume.title = request.POST.get("title")
        resume.skill = request.POST.get("skill")
        resume.content = request.POST.get("content")
        resume.save()

        messages.success(request, "更新成功")

        return redirect("resumes:index")

    return render(
        request,
        "resumes/show.html",
        {"resume": resume},
    )


def edit(request, id):
    resume = get_object_or_404(Resume, id=id)

    return render(
        request,
        "resumes/edit.html",
        {"resume": resume},
    )


def delete(request, id):
    resume = get_object_or_404(Resume, id=id)

    if request.POST:
        # 刪除
        resume.delete()
        messages.success(request, "刪除成功")
        return redirect("resumes:index")

    return render(
        request,
        "resumes/delete.html",
        {"resume": resume},
    )
