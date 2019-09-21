from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User



# Create your views here.

def post_list(request):
    user = request.user
    posts = None
    if user.is_authenticated:
        posts = Post.objects.filter(published_date__lte=timezone.now(),author=user).order_by('published_date')


    return render(request, 'blog/post_list.html', {'posts' :posts , 'user':user})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
