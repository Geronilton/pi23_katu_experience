from django.shortcuts import render, redirect
from .forms import CadastroForm,PasseioForm
from .models import Usuario, Agendamento, Passeio

# Create your views here.

def index(request):
    return render(request, "index.html")

def cadastro(request):
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        form.save()

    contexto={
        "form":form
    }

    return render(request, "cadastro.html", contexto)


def passeios(request):
    passeios = Passeio.objects.all()
    contexto = {
        "lista_passeios" : passeios
    }

    return render(request, "passeios.html", contexto)


def cadastrarPasseio(request):
    form = PasseioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(passeios)
    contexto = {
        "form": form
    }

    return render(request, "cadastrarPasseio.html",contexto)

def editarPasseio(request,id):
    passeio = Passeio.objects.get(pk=id)
    form = PasseioForm(request.POST or None,instance=passeio)

    if form.is_valid():
        form.save()
        return redirect('passeios')
    
    contexto = {
        "form": form
    }

    return render(request, "cadastrarPasseio.html",contexto)

def deletarPasseio(request, id):
    passeio = Passeio.objects.get(pk=id)
    passeio.delete()

    return redirect('passeios')