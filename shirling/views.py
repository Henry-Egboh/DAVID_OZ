from django.shortcuts import render

# Create your views here.

def home (request):
    return render (request, 'shirling/index.html')

def cart (request):
    return render (request,'shirling/cart.html')

def checkout (request):
    return render(request,'shirling/checkout.html')

def product (request):
    return render(request,'shirling/product.html')

def blog (request):
    return render(request,'shirling/blog.html')

def contact (request):
    return render(request,'shirling/contact.html')

def about (request):
    return render(request,'shirling/about.html')