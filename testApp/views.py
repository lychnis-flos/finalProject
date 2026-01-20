from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import JsonResponse
from .models import Post

def timeline(request):
    keyword = request.GET.get('keyword', '')
    category = request.GET.get('category', '')

    posts = Post.objects.all()

    if keyword:
        posts = posts.filter(
            Q(title__icontains=keyword) | Q(content__icontains=keyword)
        )

    if category:
        posts = posts.filter(category=category)

    posts = posts.order_by('-created_at')

    return render(request, 'timeline.html', {
        'posts': posts,
        'keyword': keyword,
        'category': category,
    })

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timeline')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form, 'post': post})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('timeline')
    return render(request, 'post_delete.html', {'post': post})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('timeline')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def api_posts(request):
    posts = Post.objects.all().order_by("-created_at") 

    data = []
    for p in posts:
        data.append({
            "id": p.id,
            "title": p.title,
            "category": p.category,
            "content": p.content,
            "likes": p.likes,
        })

    return JsonResponse(data, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 2})

