from django.shortcuts import render, redirect
from  portfolios.models import Portfolio
from blogs.models import BlogPost
from .models import ContactMessage
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

def contact_view(request):
    if request.method == 'POST':
        website_url = request.POST.get('website_url')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            website_url=website_url,
            name=name,
            email=email,
            phone_number=phone_number,
            message=message
        )
        return redirect('index')

    return render(request, 'contact/index.html')

