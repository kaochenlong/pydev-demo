from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ResumeForm
from .models import FavoriteResume, Resume


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
    keyword = request.GET.get("keyword", "")

    resumes = request.user.resume_set.order_by("-id")

    if keyword:
        resumes = resumes.filter(title__icontains=keyword)

    return render(
        request,
        "resumes/index.html",
        {"resumes": resumes, "keyword": keyword},
    )


def list(request):
    resumes = Resume.objects.order_by("-id")
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
    resume = get_object_or_404(Resume, id=id, user=request.user)

    if request.POST:
        # 更新
        form = ResumeForm(request.POST, instance=resume)
        form.save()

        messages.success(request, "更新成功")
        return redirect("resumes:index")

    comments = resume.comment_set.prefetch_related("user")
    favorited = resume.favorite_users.filter(id=request.user.id).first()

    return render(
        request,
        "resumes/show.html",
        {
            "resume": resume,
            "comments": comments,
            "favorited": favorited,
        },
    )


@login_required
def edit(request, id):
    resume = get_object_or_404(Resume, id=id, user=request.user)
    form = ResumeForm(instance=resume)

    return render(
        request,
        "resumes/edit.html",
        {
            "resume": resume,
            "form": form,
        },
    )


@require_POST
@login_required
def delete(request, id):
    resume = get_object_or_404(Resume, id=id, user=request.user)

    if request.POST:
        resume.delete()
        messages.success(request, "刪除成功")
        return redirect("resumes:index")

    return render(
        request,
        "resumes/delete.html",
        {"resume": resume},
    )


def public(request, id):
    resume = get_object_or_404(Resume, id=id)
    comments = resume.comment_set.all()

    return render(
        request,
        "resumes/show.html",
        {
            "resume": resume,
            "comments": comments,
        },
    )


@require_POST
@login_required
def toggle_favorite(request, id):
    resume = get_object_or_404(Resume, id=id)

    favorite, created = FavoriteResume.objects.get_or_create(
        user=request.user,
        resume=resume,
    )

    if not created:
        favorite.delete()

    return redirect("resumes:show", id=resume.id)
