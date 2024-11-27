from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from resumes.models import Resume
from .models import Comment
from django.http import HttpResponse


@require_POST
def index(request, id):
    # 找出 resume
    resume = get_object_or_404(Resume, id=id)

    # 新增 comment
    content = request.POST.get("content")
    comment = resume.comment_set.create(content=content)
    comment.save()

    return render(request, "comments/_comment.html", {"comment": comment})


@require_POST
def delete(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()

    return HttpResponse("")
