from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Customer, Rental

# Create your views here.

def customer(request):
    customers = Customer.objects.all().values()
    template = loader.get_template('all_customers.html')
    context = {
        'mycustomer': customers
    }
    return HttpResponse(template.render(context, request))

def detalhes(request, id):
    myDetalhes = Rental.objects.filter(customer_id = id)
    customer = get_object_or_404(Customer, pk = id)
    
    template = loader.get_template('details.html')
    context = {
        'myDetalhes': myDetalhes,
        'customer_name': f'{customer.first_name}  {customer.last_name}'
    }
    
    return HttpResponse(template.render(context, request))