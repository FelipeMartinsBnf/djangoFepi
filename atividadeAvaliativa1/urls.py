from django.urls import path
from . import views

urlpatterns = [
    path('atividade/home', views.home, name = 'home'),
    path('atividade/rental/<int:id>', views.rental, name = 'rental'),
    path('atividade/rental/payment/<int:id>', views.payment, name = 'payment')
]