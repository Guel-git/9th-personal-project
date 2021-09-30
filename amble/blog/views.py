from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog, Blog_Reply, HashTag
from django.utils import timezone
# Create your views here.

def blog(request):
    blog = Blog.objects
    return render(request, 'blog.html', {'blogs': blog})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    blog_hashtag = blog_detail.hashtag.all()
    return render(request, 'blog_detail.html', {'blog': blog_detail, 'hashtags': blog_hashtag})

def new(request):
    return render(request, 'blog_new.html')

def create(request):
    if request.method == 'POST':
        blog = Blog()
        blog.author = request.user
        blog.title = request.POST.get('title')
        blog.content = request.POST.get('content')
        blog.pub_date = timezone.now()
        blog.img = request.FILES.get('img')
        blog.save()
        hastags = request.POST['hashtags']
        hashtag = hastags.split(",")
        for tag in hashtag:
            ht = HashTag.objects.get_or_create(hashtag_name=tag)
            blog.hashtag.add(ht[0])
        return redirect('blog')
    else:
        return redirect('blog')

def edit(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_edit.html', {'blog': blog_detail})

def update(request, blog_id):
    if request.method == 'POST':
        blog_update = get_object_or_404(Blog, pk=blog_id)
        blog_update.title = request.POST['title']
        blog_update.img = request.FILES['img']
        blog_update.content = request.POST['content']
        blog_update.save()
        hastags = request.POST['hashtags']
        hashtag = hastags.split(",")
        for tag in hashtag:
            ht = HashTag.objects.get_or_create(hashtag_name=tag)
            blog_update.hashtag.add(ht[0])
        return redirect('blog_detail', blog_id)
    else:
        return redirect('blog')

def delete(request, blog_id):
    blog_delete = get_object_or_404(Blog, pk=blog_id)
    blog_delete.delete()
    return redirect('blog')

def reply(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        reply = Blog_Reply()
        reply.post = blog
        reply.content = request.POST['content']
        reply.reply_by = request.user
        reply.save()
        return redirect('blog_detail', blog_id)
    else:
        return redirect('blog')

def reply_delete(request, blog_id, reply_id):
    reply_delete = get_object_or_404(Blog_Reply, pk=reply_id)
    reply_delete.delete()
    return redirect('blog_detail', blog_id)