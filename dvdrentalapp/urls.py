from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.customer, name = 'mycustomer'),
    path('customer/detalhes/<int:id>', views.detalhes, name = 'myDetalhes')
]
