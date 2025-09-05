from django.forms import ModelForm
from .models import Customer, Category

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        
class CateogryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

