from django.utils import timezone
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import Customer, Rental, Category, Address, City
from .forms import CustomerForm, CateogryForm, CustomUserCreationForm
import json

def home(request):
    return render(request, 'home.html', {})

# Auth
def create_user(request):
    if request.method == "POST":
        formUsuario = CustomUserCreationForm(request.POST)
        if formUsuario.is_valid():
            formUsuario.save()
            return redirect("msg/Craiado%20com%20sucesso")
    else:
        formUsuario = CustomUserCreationForm()
    return render(request, 'user_form.html', {'form': formUsuario})

def login_form(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)
        
        if(usuario is not None):
            login(request, usuario)
            return render(request, 'logado.html', {})
        formLogin = AuthenticationForm()
    else:
        formLogin = AuthenticationForm()
    return render(request, 'login.html', {'login': formLogin})
@login_required(login_url="login")
def logout_user(requst):
    logout(requst)
    return redirect("home")

@login_required(login_url="login")
def alterar_senha(request):
    if request.method == 'POST':
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect("home")
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'alterar_senha.html', {'form': form_senha})

def msg(request, msg):
    return render(request, 'containers/msg.html', {'msg': msg})

# Create your views here.

@login_required(login_url="login")
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

@login_required(login_url="login")
def detalhes(request, id):
    myDetalhes = Rental.objects.filter(customer_id = id)
    customer = get_object_or_404(Customer, pk = id)
    
    template = loader.get_template('details.html')
    context = {
        'myDetalhes': myDetalhes,
        'customer_name': f'{customer.first_name}  {customer.last_name}'
    }
    
    return HttpResponse(template.render(context, request))

@login_required(login_url="login")
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

@login_required(login_url="login")
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

@login_required(login_url="login")
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

@login_required(login_url="login")
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
        
@login_required(login_url="login")
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

@login_required(login_url="login")
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