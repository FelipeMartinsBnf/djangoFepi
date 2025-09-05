from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.customer, name = 'mycustomer'),
    path('customer/detalhes/<int:id>', views.detalhes, name = 'myDetalhes'),
    path('customer/edit/<int:id>', views.edit_customer, name = 'edit_customer'),
    path('customer/add/form', views.add_customer_form_view, name = 'add_customer_form'),
    path('categories', views.all_categories, name = 'all_categories'),
    path('categories/add', views.add_category, name = 'add_category'),
    path('categories/edit/<int:id>', views.edit_category, name = 'edit_category'),
    
    
    path('api/customers', views.custumersJson, name = 'custumersJson'),
    
    
]
