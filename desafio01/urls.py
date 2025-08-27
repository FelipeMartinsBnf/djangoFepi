
from . import views
from django.urls import path


urlpatterns = [
    path('countries/', views.contry, name = 'countries'),
    path('countries/edit/<int:id>', views.edit_country, name = 'edit_countries')
]