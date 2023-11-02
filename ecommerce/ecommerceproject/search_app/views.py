from shop.models import Product
from django.shortcuts import render
from django.db.models import Q

def SearchResult(request):
    products = None
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        query_list = query.split()  # Split the query into individual words
        products = Product.objects.filter(Q(name__icontains=query_list[0]) | Q(description__icontains=query_list[0]))
        for term in query_list[1:]:
            products = products | Product.objects.filter(Q(name__icontains=term) | Q(description__icontains=term))

    return render(request, 'search.html', {'query': query, 'products': products})
