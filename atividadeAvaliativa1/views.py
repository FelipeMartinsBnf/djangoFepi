from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Customer, Rental, Payment

def home(request):
    all_customers = Customer.objects.all();
    
    template = loader.get_template('home.html')
    return  HttpResponse(template.render({"customers": all_customers}, request))

def rental(request, id):
    all_rental = Rental.objects.filter(customer_id = id)
    customer = get_object_or_404(Customer, pk = id)

    template = loader.get_template('rental.html')
    return  HttpResponse(template.render({"rental": all_rental, "customer": customer}, request))

def payment(request, id):
    all_payment = Payment.objects.filter(rental_id = 3161)
    rental = get_object_or_404(Rental, pk = id)
    
    template = loader.get_template('payment.html')
    return  HttpResponse(template.render({"rental": rental, "payment": all_payment}, request))

