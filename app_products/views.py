from django.shortcuts import render, redirect
from .models import Product

def home(request):
    _products = Product.objects.all()
    return render(request, 'index.html',{'products': _products})

def add(request):
    _name = request.POST.get('name')
    _price = request.POST.get('price')
    Product.objects.create(name=_name)

    _products = Product.objects.all()
    return render(request, 'index.html',{'products': _products})

def edit(request, id):
    _product = Product.objects.get(id=id)
    return render(request, 'update.html',{'product': _product})

def update(request, id):
    _name = request.POST.get("name")
    _price = request.POST.get("price")
    _product = Product.objects.get(id=id)
    _product.name = _name
    _product.price = _price
  
    _product.save()
    return redirect(home)

def delete(request, id):
    _product = Product.objects.get(id=id)
    _product.delete()
    return redirect(home)