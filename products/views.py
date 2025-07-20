from django.shortcuts import render, get_object_or_404
from .models import Product

def homepage(request):
    return render(request, 'products/homepage.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    price_history = product.price_history.all().order_by('date')
    return render(request, 'products/product_detail.html', {
        'product': product,
        'price_history': price_history
    })
