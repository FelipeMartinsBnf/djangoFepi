from django.contrib import admin
from .models import Customer, Address

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "last_update")

admin.site.register(Customer, CustomerAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ("address", "city", "postal_code")

admin.site.register(Address, AddressAdmin)