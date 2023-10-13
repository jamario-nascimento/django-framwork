from django.shortcuts import render

from .models import Product
# Criando minha primeira view
def index(request):

    products = Product.objects.all()

    context = {
        'curso': 'Programação Web com Django Framework',
        'products': products,
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def product(request, id):
    productItem = Product.objects.get(id)
    context = {
        'product': productItem
    }
    return render(request, 'product.html', context)

