from django.utils import timezone
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.core.serializers.json import DjangoJSONEncoder
from .models import Customer, Rental, Category, Address, City
from .forms import CustomerForm, CateogryForm

import json

# Create your views here.

def customer(request):
    nameFilter = typeFilter =""
    if request.method == "POST":
        nameFilter = request.POST.get("first_name")
        typeFilter = request.POST.get("type")
        filtro = {typeFilter: nameFilter}
        print(filtro)
        customers = Customer.objects.filter(**filtro)
    else:
        customers = Customer.objects.all().values()
    template = loader.get_template('all_customers.html')
    context = {
        'mycustomer': customers,
        'nameFilter': nameFilter,
        'typeFilter': typeFilter
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
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("/customer")
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'edit_customer.html', {'customer': customer, "form": form})

def all_categories(request):
    nameFilter = typeFilter =""
    if request.method == "POST":
        nameFilter = request.POST.get("first_name")
        typeFilter = request.POST.get("type")
        filtro = {typeFilter: nameFilter}
        categories = Category.objects.filter(**filtro)
    else:
         categories = Category.objects.all().values()
    return render(request, 'all_categories.html', {'categories': categories, 'nameFilter':nameFilter})

def add_category(request):
    if request.method == 'POST':
        form = CateogryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.last_update = timezone.now()
            form.save()
            return redirect("/categories")
    else:
        form = CateogryForm() 
    return render(request, 'add_category.html', {'form': form})
    
def edit_category(request, id):
    category = get_object_or_404(Category, pk = id)
    if(request.method == 'POST'):
        form = CateogryForm(request.POST, instance= category)
        if form.is_valid():
            form.save()
            return redirect("/categories")
    else:
        form = CateogryForm(instance= category)
    return render(request, 'edit_category.html', {'category': category, 'form': form})
        
        
    
def add_customer_form_view(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/customer")
    else:
        form = CustomerForm() 
    return render(request, 'add_customer_form_template.html', {'form': form})

def custumersJson(request):
        customers_list = list(Customer.objects.filter(customer_id__lte=10).values())
        jsonCustumers = json.dumps(customers_list,  default=str)
        
        #return JsonResponse(customers_list)
        return render(request, 'json.json', {'json': jsonCustumers})
    
def get_rental_details(request, id):
    myDetalhes = Rental.objects.filter(customer_id=id)
    customer = get_object_or_404(Customer, pk = id)
    template = loader.get_template('modal/rental_modal_content.html')
    
    context = {
        "myDetalhe": myDetalhes,
        "customer_name": f"{customer.first_name} {customer.last_name}"
    }
    
    rendered_content = template.render(context, request)
    return JsonResponse({'html': rendered_content })