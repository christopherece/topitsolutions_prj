from django.shortcuts import render
from . models import Portfolio

def portfolio(request):
    portfolios = Portfolio.objects.all().order_by('-created_at')

    context = {
        'portfolios': portfolios,
  
    }
    return render(request, 'portfolio/index.html', context)
