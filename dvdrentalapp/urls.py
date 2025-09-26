from django.urls import path
from . import views

urlpatterns = [
    path('auth/create-user', views.create_user, name = 'userForm'),
    path('auth/login', views.login_form, name = 'login'),
    path('home', views.home, name = 'home'),
    path('auth/password', views.alterar_senha, name = 'alterar_senha'),
    path('auth/logout', views.logout_user, name = 'logout'),
    path('auth/msg/<str:msg>', views.msg, name = 'msg'),
    
    path('customer/', views.customer, name = 'mycustomer'),
    path('customer/detalhes/<int:id>', views.detalhes, name = 'myDetalhes'),
    path('api/customer/detalhes/<int:id>', views.get_rental_details, name = 'myRental'),
    path('customer/edit/<int:id>', views.edit_customer, name = 'edit_customer'),
    path('customer/add/form', views.add_customer_form_view, name = 'add_customer_form'),
    path('categories', views.all_categories, name = 'all_categories'),
    path('categories/add', views.add_category, name = 'add_category'),
    path('categories/edit/<int:id>', views.edit_category, name = 'edit_category'),
    
    
    path('api/customers', views.custumersJson, name = 'custumersJson'),
    
    
]
