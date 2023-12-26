from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    nome_completo = models.CharField("Nome", max_length=100)
    telefone = models.CharField("Telefone", max_length=14)
    email = models.EmailField('Email',max_length= 100)
    cpf = models.CharField("CPF", max_length=11, primary_key=True)
    username = models.CharField('username', max_length=11, null=True)

    USERNAME_FIELD = 'cpf'


class Passeio(models.Model):
    titulo = models.CharField("Titulo", max_length= 100)
    descricao = models.TextField("Descrição")
    valor = models.DecimalField(max_digits=5, decimal_places= 2)

    
    def __str__(self):
        return self.titulo

class Agendamento(models.Model):
    data_registro = models.DateTimeField('Data Registro',auto_now_add= True)
    data_proposta =  models.DateField('Data de Agendamento')
    data_confirmacao = models.DateTimeField('Data de confirmação', null=True)
    qtd_pessoas = models.IntegerField("Quantidade de Pessoas")
    usuario = models.ForeignKey(Usuario,on_delete=models.PROTECT )
    passeio = models.ForeignKey(Passeio,on_delete=models.PROTECT )
