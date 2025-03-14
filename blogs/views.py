from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.http import Http404
from django.utils.text import slugify
from django.contrib import messages

# View to list all blog posts
def blog_list(request):
    posts = BlogPost.objects.all()  # Get all blog posts
    return render(request, 'blogs/blog_list.html', {'posts': posts})

# View to display a single blog post
def blog_detail(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)  # Fetch the blog post by its slug
    return render(request, 'blogs/blog_detail.html', {'blog_post': blog_post})

# View to create a new blog post (for admins or authenticated users)
def blog_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')
        published_at = request.POST.get('published_at')

        if title and content:
            slug = slugify(title)  # Slugify the title for URL
            new_post = BlogPost(
                title=title,
                slug=slug,
                content=content,
                category=category,
                published_at=published_at
            )
            new_post.save()  # Save the new blog post to the database
            messages.success(request, 'Blog post created successfully!')
            return redirect('blog_list')  # Redirect to the blog list page
        else:
            messages.error(request, 'Title and content are required.')
    
    return render(request, 'blogs/blog_form.html')

# View to edit an existing blog post
def blog_edit(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)  # Get the blog post by its slug
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')
        published_at = request.POST.get('published_at')

        if title and content:
            post.title = title
            post.content = content
            post.category = category
            post.published_at = published_at
            post.slug = slugify(title)  # Ensure the slug is updated if title changes
            post.save()  # Save the updated blog post to the database
            messages.success(request, 'Blog post updated successfully!')
            return redirect('blog_detail', slug=post.slug)  # Redirect to the updated post
        else:
            messages.error(request, 'Title and content are required.')

    return render(request, 'blogs/blog_form.html', {'post': post})
