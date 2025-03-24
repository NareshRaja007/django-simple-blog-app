from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BlogPost
from .forms import BlogPostForm

def list_blog_posts(request):
    """View to list all blog posts."""
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def create_blog_post(request):
    """View to create a new blog post."""
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_blog_posts')  
    else:
        form = BlogPostForm()
    return render(request, 'blog/post_create.html', {'form': form})
