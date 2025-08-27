from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Country
from .models import City

# Create your views here.
def contry(request):
    countries = Country.objects.all().values()
    template = loader.get_template('desafio01.html')
        
    context = {
        'countries': countries
    }
    return HttpResponse(template.render(context, request))

def edit_country(request, id):
    country = get_object_or_404(Country, pk = id)
    
    if( request.method == "POST"):
        country.country = request.POST.get("country")
        
        country.save()
        return redirect("/countries")
    return render(request, 'edit_country.html', {"country": country})
    