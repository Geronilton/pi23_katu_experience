from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField("Nome", max_length=100)
    telefone = models.IntegerField("Telefone", max_length=11)
    email = models.EmailField("Email", max_length=100)
    cpf = models.IntegerField("CPF", max_length=11)

class Passeio(models.Model):
    titulo = models.CharField("Titulo", max_length=50)
    decricao = models.CharField("Descrição", max_length=50)
    valor = models.IntegerField("Valor")

class Serviços(models.Model):
    nome = models.CharField("Titulo", max_length=50)

class Participantes(models.Model):
    nome = models.CharField("Titulo", max_length=50)
