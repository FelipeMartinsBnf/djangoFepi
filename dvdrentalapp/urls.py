from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.customer, name = 'mycustomer'),
    path('customer/detalhes/<int:id>', views.detalhes, name = 'myDetalhes'),
    path('customer/edit/<int:id>', views.edit_customer, name = 'edit_customer'),
    path('customer/add', views.add_customer, name = 'add_customer'),
    path('categories', views.all_categories, name = 'all_categories'),
    path('categories/add', views.add_category, name = 'add_category'),
    
]
