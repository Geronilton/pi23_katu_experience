from django.shortcuts import render, redirect
from .forms import CadastroForm,PasseioForm
from .models import Usuario, Agendamento, Passeio
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
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

    return render(request, "registration/cadastro.html", contexto)


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

def autenticacao(request):

    if request.POST:
        username = request.POST['usuario']
        password = request.POST['senha']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('perfil')
        else:
           return render(request, 'registration\login.html')
    else:
        return render(request, 'registration\login.html')
    

@login_required
def perfil(request):
    return render(request, 'perfil.html')