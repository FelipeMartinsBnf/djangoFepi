from django.utils import timezone
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Customer, Rental, Category, Address, City

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

def edit_customer(request, id):
    customer = get_object_or_404(Customer, pk = id)
    
    if request.method == "POST":
        customer.first_name = request.POST.get("first_name")
        customer.last_name = request.POST.get("last_name")
        customer.email = request.POST.get("email")
        customer.save()
        return redirect('/customer')
    return render(request, 'edit_customer.html', {'customer': customer})

def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'all_categories.html', {'categories': categories})

def add_category(request):
    if request.method == "POST":
        category = Category(name=request.POST.get("name"), last_update=timezone.now())
        category.save()
        
        return redirect('/categories')
    return render(request, 'add_category.html', {})

def add_customer(request):    
    if request.method == "POST":
        address = Address(
            address = request.POST.get("address"),
            district = request.POST.get("district"),
            city = City.objects.get(city_id = request.POST.get("city")),
            phone = request.POST.get("phone"),
            last_update=timezone.now())
        
        address.save()
        
        customer = Customer(
            store_id = 1,
            first_name =  request.POST.get("first_name"),
            last_name =  request.POST.get("last_name"),
            email =  request.POST.get("email"),
            address =  address,
            activebool = True,
            create_date = timezone.now(),
            last_update=timezone.now(),
            active = 1)
        
        customer.save()
        
        return redirect('/customer')
    else:
        cities = City.objects.all()
        return render(request, 'add_customer.html', {'cities': cities})