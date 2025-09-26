from typing import Any
from django.forms import ModelForm
from .models import Customer, Category, CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        
class CateogryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('endereco', 'cidade', 'estado', 'cep')
        labels = {
            'username': "Nome de Usuário",
            'password1': 'Senha',
            'password2': 'Confirme a senha',
            'endereco': 'Endereço',
            'cidade': 'Cidade',
            'estado': 'Estado',
            'cep': 'CEP'
        }
        
    def __init__(self, *args: Any, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'django-form'