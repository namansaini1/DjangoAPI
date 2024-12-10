from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Avg, Sum, F
from django.db.models import Q
from products.models import Product
from django.core.cache import cache

def product_analytics(request):
    # Steps 2.1: Retrieve Query parameters
    category = request.GET.get('category')  # case-insensitive filter
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price')

    print(f"Category: {category}, Min Price: {min_price}, Max Price: {max_price}")
    
    # Step 2.2 Generate a Unique Cache Key
    cache_key = f"analytics_{category or 'all'}_{min_price}_{max_price}"
    cached_data = cache.get(cache_key)

    if cached_data:
        print("Cache hit! Returning cached result.")  # Debugging output
        return JsonResponse(cached_data)
    
    # Fetch all products
    products = Product.objects.all()
    print(f"Total products in database: {products.count()}")  # Debugging output

    if category:
        products = products.filter(category__iexact=category)  # Case-insensitive filter
    if min_price:
        try:
            products = products.filter(price__gte=float(min_price))
        except ValueError:
            return JsonResponse({"error": "Invalid minimum price value"}, status=400)
    if max_price:
        try:
            products = products.filter(price__lte=float(max_price))
        except ValueError:
            return JsonResponse({"error": "Invalid maximum price value"}, status=400)

    # Step 2.2 Perform aggregation
    analytics = products.aggregate(
        total_products=Count('id'),
        average_price=Avg('price'),
        total_stock_value=Sum(F('stock') * F('price'))
    )

    # Check if analytics is empty
    if analytics['total_products'] == 0:
        return JsonResponse({"message": "No products found matching the criteria."}, status=404)
    
    #  Cache the result for 5 minute

    cache.set(cache_key, analytics, timeout=300)

    # Step 3 Return the aggregated data as Json
    return JsonResponse(analytics)