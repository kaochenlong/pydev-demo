from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST

from resumes.models import Resume

from .models import Comment


@require_POST
@login_required
def index(request, id):
    # 找出 resume
    resume = get_object_or_404(Resume, id=id)

    # 新增 comment
    content = request.POST.get("content")
    comment = resume.comment_set.create(
        content=content,
        user_id=request.user.id,
    )
    comment.save()

    return render(request, "comments/_comment.html", {"comment": comment})


@require_POST
@login_required
def delete(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()

    return HttpResponse("")
