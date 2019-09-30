from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
from math import ceil

# Create your views here.


def index(request):
    allprods = []
    categoriesList = Product.objects.values('category', 'id')
    print(categoriesList)

    categoryLt = {item['category'] for item in categoriesList}
    for category in categoryLt:
        prods = Product.objects.filter(category=category)
        print(prods)
        n = len(prods)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allprods.append([prods, range(1, nSlides), nSlides])

    params = {
        'allprods': allprods
    }
    return render(request, "shop/index.html", params)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    if request.method == 'POST':

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        desc = request.POST.get('desc', '')
        phone = request.POST.get('phone', '')

        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "shop/contact.html")


def tracker(request):
    return render(request, "shop/tracker.html")


def search(request):
    return render(request, "shop/search.html")


def productView(request,myid):
    #fetch the producct from db

    product=Product.objects.filter(id=myid)
    print(product)

    return render(request, "shop/prodView.html", {'product': product[0]})


def checkout(request):
    return render(request, "shop/checkout.html")
