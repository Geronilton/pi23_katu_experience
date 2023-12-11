from django.forms import ModelForm
from .models import Usuario, Passeio

class CadastroForm(ModelForm):
    class Meta():
        model = Usuario
        fields = ["nome_completo","telefone","email","cpf"]

class PasseioForm(ModelForm):
    class Meta():
        model = Passeio
        fields = ["titulo", "descricao","valor"]