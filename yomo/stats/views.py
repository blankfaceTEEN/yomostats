from django.shortcuts import render

from .models import Stats

def index(request):
    stats = Stats.objects.order_by('-score')
    context = {
        'stats': stats, 
        }
    return render(request, 'stats/index.html', context)  
