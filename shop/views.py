from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


# Create your views here.

def index(request):


    # params = {
    #     'product': products,
    #     'no_of_slides': nSlides,
    #     'range': range(1, nSlides)
    # }
    # list of list
    allprods = []
    categoriesList = Product.objects.values('category', 'id')
    print(categoriesList)
    categoryLt = {item['category'] for item in categoriesList}
    for category in categoryLt:
        prods = Product.objects.filter(category=category)
        print(prods)
        n = len(prods)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allprods.append([prods, range(1,nSlides), nSlides])



    params = {
        'allprods': allprods
    }
    return render(request, "shop/index.html", params)


def about(request):
    return render(request, "shop/about.html")


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
