from django.shortcuts import render
from  portfolios.models import Portfolio
# Create your views here.
def index(request):
    portfolios = Portfolio.objects.all()
    context = {
        'portfolios': portfolios
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')