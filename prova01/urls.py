from django.urls import path
from .views import get_all_country, get_all_city_from_country, get_all_address_from_city

urlpatterns = [
    path('prova/countries', get_all_country, name = 'all_countries'),
    path('prova/countries/<int:id>/cities', get_all_city_from_country, name = 'all_cities_country'),
    path('prova/city/address/<int:id>', get_all_address_from_city, name = 'all_address_city')
]