from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    nome_completo = models.CharField("Nome", max_length=100)
    telefone = models.IntegerField("Telefone")
    cpf = models.CharField("CPF", max_length=11, primary_key=True)

class Passeio(models.Model):
    titulo = models.CharField("Titulo", max_length= 100)
    descricao = models.TextField("Descrição")
    valor = models.DecimalField(max_digits=5, decimal_places= 2)

class Agendamento(models.Model):
    data_registro = models.DateTimeField('Data Registro',auto_now_add= True)
    data_proposta =  models.DateTimeField('Data de Agendamento')
    data_confirmacao = models.DateTimeField('Data de confirmação')
    qtd_pessoas = models.IntegerField("Quantidade de Pessaos")
    usuario = models.ForeignKey(Usuario,on_delete=models.PROTECT )
    passeio = models.ForeignKey(Passeio,on_delete=models.PROTECT )
