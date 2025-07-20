from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    price_history = product.price_history.all().order_by('date')
    return render(request, 'products/product_detail.html', {
        'product': product,
        'price_history': price_history
    })
