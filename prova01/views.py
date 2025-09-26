from django import template
from django.shortcuts import render
from .models import Country, City, Address

def get_all_country(request):
    countries = Country.objects.all()
    return render(request, 'country.html', {'countries': countries})

def get_all_city_from_country(request, id):
    citites = City.objects.filter(country = id)
    
    return render(request, 'cities.html', {'cities': citites})

def get_all_address_from_city(request, id):
    addres = Address.objects.filter(city = id)
    
    return render(request, 'address.html', {'address': addres})
