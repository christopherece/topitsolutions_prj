from django.shortcuts import render
from  portfolios.models import Portfolio
from blogs.models import BlogPost
# Create your views here.
def index(request):
    portfolios = Portfolio.objects.all()
    latest_blog_posts = BlogPost.objects.all()[:3]  # This will get the first 3 blog posts

    context = {
        'portfolios': portfolios,
        'latest_blog_posts': latest_blog_posts,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

