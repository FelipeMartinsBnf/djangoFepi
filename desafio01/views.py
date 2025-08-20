from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Country
from .models import City

# Create your views here.
def contry(request):
    cities = City.objects.all().values()
    countries = Country.objects.all().values()
    template = loader.get_template('desafio01.html')
        
    context = {
        'countries': countries
    }
    return HttpResponse(template.render(context, request))