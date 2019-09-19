from django.shortcuts import render
from django.http import HttpResponse
from. models import  Product
from math import ceil

# Create your views here.

def index(request):
    products=Product.objects.all()
    print(products)
    n=len(products)
    nSlides=n//4+ceil((n/4)-(n//4))
    params={
        'product':products,
        'no_of_slides':nSlides,
        'range':range(1,nSlides)
    }
    return  render(request,"shop/index.html",params)

def about(request):
    return  render(request,"shop/about.html")

def contact(request):
    return HttpResponse('we are at contact')

def tracker(request):
    return HttpResponse('we are at tracker')

def search(request):
    return HttpResponse('we are at search')

def productView(request):
    return HttpResponse('we are at productView')

def checkout(request):
    return HttpResponse('we are at checkout')


