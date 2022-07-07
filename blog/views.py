from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from blog.models import Post, Comment


def blog_home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog_home.html', context)


def blog_detail(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post, parent=None)
    replies = Comment.objects.filter(post=post).exclude(parent=None)
    reply_dict = {}

    for reply in replies:
        if reply.parent.id not in reply_dict.keys():
            reply_dict[reply.parent.id] = [reply]
        else:
            reply_dict[reply.parent.id].append(reply)

    context = {'post': post, 'comments': comments, 'reply_dict': reply_dict}
    return render(request, 'blog.html', context)


def post_comment(request):
    if request.method == 'POST':
        comment = request.POST.get("comment")
        name = request.POST.get("name")
        email = request.POST.get("email")
        post_id = request.POST.get("post_id")
        post = Post.objects.get(id=post_id)
        parent_id = request.POST.get("parent_id")

        if parent_id == '':
            if name.isalnum():
                messages.error(request, "Name should not contain numeric or special characters")
            elif name.isnumeric():
                messages.error(request, "Name should not contain numeric or special characters")
            else:
                comment = Comment(comment=comment, name=name, email=email, post=post)
                comment.save()
                messages.success(request, "Comment Posted")
        else:
            parent = Comment.objects.get(id=parent_id)
            reply_name = request.POST.get("reply_name")
            reply_email = request.POST.get("reply_email")
            comment = Comment(comment=comment, name=reply_name, email=reply_email, post=post, parent=parent)
            comment.save()
            messages.success(request, "Reply Posted")

    return redirect(f"/blog/{post.slug}")
