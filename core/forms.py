from django.forms import ModelForm
from .models import Usuario, Passeio
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['nome_completo', 'cpf', 'email', 'password1', 'password2']

class PasseioForm(ModelForm):
    class Meta():
        model = Passeio
        fields = ["titulo", "descricao","valor"]