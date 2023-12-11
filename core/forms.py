from django.forms import ModelForm
from .models import Usuario

class CadastroForm(ModelForm):
    class Meta():
        model = Usuario
        fields = ["nome_completo","telefone","email","cpf"]