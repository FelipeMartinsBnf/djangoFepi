
from . import views
from django.urls import path


urlpatterns = [
    path('countries/', views.contry, name = 'countries')
]