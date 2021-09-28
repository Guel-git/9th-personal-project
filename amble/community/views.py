from django.shortcuts import render
from .models import Community, Community_Reply
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.

def community(request):
    community = Community.objects
    return render(request, 'community.html', {'communitys': community})

def detail(request, community_id):
    community_detail = get_object_or_404(Community, pk=community_id)
    return render(request, 'community_detail.html', {'community': community_detail})

def new(request):
    return render(request, 'community_new.html')

def create(request):
    community = Community()
    community.author = request.user
    community.title = request.POST.get('title')
    community.content = request.POST.get('content')
    community.pub_date = timezone.now()
    community.save()
    return redirect('community')

def edit(request, community_id):
    community_detail = get_object_or_404(Community, pk=community_id)
    return render(request, 'community_edit.html', {'community': community_detail})

def update(request, community_id):
    community_update = get_object_or_404(Community, pk=community_id)
    community_update.title = request.POST['title']
    community_update.content = request.POST['content']
    community_update.save()
    return redirect('detail', community_id)

def delete(request, community_id):
    community_delete = get_object_or_404(Community, pk=community_id)
    community_delete.delete()
    return redirect('community')

def reply(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    if request.method == 'POST':
        reply = Community_Reply()
        reply.content = request.POST['content']
        reply.post = community
        reply.reply_by = request.user
        reply.save()
        return redirect('detail', community_id)
    else:
        return redirect('community')  # 홈으로

def reply_delete(request, community_id, reply_id):
    reply_delete = get_object_or_404(Community_Reply, pk=reply_id)
    reply_delete.delete()
    return redirect('detail', community_id)

        