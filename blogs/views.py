from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import BlogPost
from pages.models import Testimonial
from django.http import Http404
from django.utils.text import slugify
from django.contrib import messages

# View to list all blog posts
def blog_list(request):
    testimonials = Testimonial.objects.all()

    posts = BlogPost.objects.all().order_by('-created_at')  # Get all blog posts
    paginator = Paginator(posts, 3)  # Paginate the posts
    page = request.GET.get('page')  # Get the current page number from the request
    pages_posts = paginator.get_page(page)  # Get the posts for the current page

    return render(request, 'blogs/blog_list.html', {'posts': pages_posts,'testimonials': testimonials})

# View to display a single blog post
def blog_detail(request, slug):
    testimonials = Testimonial.objects.all()
    blog_post = get_object_or_404(BlogPost, slug=slug)  # Fetch the blog post by its slug
    return render(request, 'blogs/blog_detail.html', {'blog_post': blog_post, 'testimonials': testimonials})

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
