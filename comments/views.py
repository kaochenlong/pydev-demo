from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from resumes.models import Resume
from django.contrib import messages
from .models import Comment


@require_POST
def index(request, id):
    # 找出 resume
    resume = get_object_or_404(Resume, id=id)

    # 新增 comment
    comment = Comment()
    comment.content = request.POST.get("content")
    comment.resume_id = resume.id
    comment.save()

    messages.success(request, "新增留言成功")
    return redirect("resumes:show", id=resume.id)
