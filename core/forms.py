from django.forms import ModelForm
from .models import Usuario, Passeio , Agendamento
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['nome_completo', 'cpf','telefone', 'email', 'password1', 'password2']

class PasseioForm(ModelForm):
    class Meta():
        model = Passeio
        fields = ["titulo", "descricao","valor"]

class AgendamentoForm(ModelForm):
    class Meta():
        model = Agendamento
        fields = ["data_proposta","qtd_pessoas","passeio"]