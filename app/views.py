from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def cached_posts(request):
    user_id = request.user.pk
    visited_pages = cache.get(user_id)
    if visited_pages is None:
        cache.set(user_id, "")
        visited_pages = cache.get(user_id)
    pages = []
    print(visited_pages)
    print(visited_pages.split(' '))
    for a in visited_pages.split(' '):
        if a is not "" and a is not " ":
            pages.append(int(a))
    print(pages)
    return pages

def paginated_posts(request ,all_posts):
    page = request.GET.get('page', 1)

    paginator = Paginator(all_posts, 4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return posts

@login_required
def post_list(request):
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = paginated_posts(request, post_list)
    pages = cached_posts(request)

    return render(request, 'app/post_list.html', {'posts': posts, 'pages': pages})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)

    user_id = request.user.pk
    visited_pages = cache.get(user_id)

    if visited_pages is None:
        cache.set(user_id, "")
        visited_pages = cache.get(user_id)

    if str(pk) not in visited_pages.split(" "):
        visited_pages += str(pk) + " "
    cache.set(user_id, visited_pages)


    return render(request, 'app/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'app/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'app/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'app/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_list')

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect(post_list)

@login_required
def post_unchecked(request):

    all_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    cached_pages = cached_posts(request)
    posts = []
    unchecked_posts = []

    for post in all_posts:
        if post.pk not in cached_pages:
            unchecked_posts.append(post)
    unchecked_posts = paginated_posts(request, unchecked_posts)
    unchecked = True

    return render(request, 'app/post_unchecked_list.html', {'posts': unchecked_posts, 'pages': cached_pages, 'unchecked': unchecked})