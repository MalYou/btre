from django.shortcuts import render

from listings.models import Listing

def index(request):
    latest_listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'latest_listings': latest_listings
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
