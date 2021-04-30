from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    
    # Show x item par page
    paginator = Paginator(listings, 6)
    page_number = request.GET.get('page')
    paginated_list = paginator.get_page(page_number)

    context = {
        'listings': paginated_list
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
