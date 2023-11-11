from django.forms import ModelForm
from .models import Cliente

class CadastroForm(ModelForm):
    class meta:
        model = Cliente
        fields = ["nome","telefone","email","cpf"]