from django.shortcuts import render, redirect, get_object_or_404
from .models import Resume
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ResumeForm


@login_required
def index(request):
    if request.POST:
        form = ResumeForm(
            request.POST,
            instance=Resume(user=request.user),
        )
        form.save()

        messages.success(request, "新增成功")
        return redirect("resumes:index")

    # 讀取 resume 列表
    resumes = Resume.objects.filter(user=request.user).order_by("-id")
    return render(
        request,
        "resumes/index.html",
        {"resumes": resumes},
    )


@login_required
def new(request):
    form = ResumeForm()
    return render(
        request,
        "resumes/new.html",
        {"form": form},
    )


def show(request, id):
    resume = get_object_or_404(Resume, id=id)

    if request.POST:
        # 更新
        form = ResumeForm(request.POST, instance=resume)
        form.save()

        messages.success(request, "更新成功")
        return redirect("resumes:index")

    comments = resume.comment_set.all()

    return render(
        request,
        "resumes/show.html",
        {
            "resume": resume,
            "comments": comments,
        },
    )


@login_required
def edit(request, id):
    resume = get_object_or_404(Resume, id=id)
    form = ResumeForm(instance=resume)

    return render(
        request,
        "resumes/edit.html",
        {
            "resume": resume,
            "form": form,
        },
    )


@login_required
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
