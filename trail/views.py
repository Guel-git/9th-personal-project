from django.shortcuts import get_object_or_404, render
from .models import Trail, HashTag
# Create your views here.
def trail(request):
    trail = Trail.objects
    return render(request, 'trail.html', {'trails': trail})

def detail(request, trail_id):
    trail_detail = get_object_or_404(Trail, pk=trail_id)
    trail_hashtag = trail_detail.hashtag.all()
    return render(request, 'trail_detail.html', {'trail': trail_detail, 'hashtags': trail_hashtag})

def search(request):
    trails = Trail.objects.all().order_by('-id')

    q = request.POST.get('q', "")

    if q:
        trails = trails.filter(name__icontains=q)
        return render(request, 'trail.html', {'trails': trails, 'q': q})
    else:
        return render(request, 'trail.html')