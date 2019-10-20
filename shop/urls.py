from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="shophome"),
    path('about', views.about, name=' Aboutus'),
    path('contact', views.contact, name=' contactUs'),
    path('tracker', views.tracker, name=' TrackingStatus'),
    path('search', views.search, name='Search'),
    path('products/<int:myid>', views.productView, name='Productview'),
    path('checkout', views.checkout, name='checkout'),
]
