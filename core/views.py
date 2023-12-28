from django.shortcuts import render, redirect
from .forms import UsuarioForm,PasseioForm, AgendamentoForm
from .models import Usuario, Agendamento, Passeio
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, "index.html")

def cadastro(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    contexto={
        "form":form
    }

    return render(request, "registration/cadastro.html", contexto)


@login_required
def dados(request, id):
    user = User.objects.get(pk=id)
    form = UsuarioForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('perfil')
    contexto = {
        'form': form
    }
    return render(request, 'registration/cadastro.html', contexto)

def cadastro_admin(request):
    if request.user.is_superuser:
        form = UsuarioForm(request.POST or None)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.is_superuser = True
            usuario.save()
            return redirect('login')
        contexto={
            "form":form
        }
        return render(request, "registration/cadastro_admin.html", contexto)
    else:
        return redirect('login')


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

# def autenticacao(request):

#     if request.POST:
#         username = request.POST['usuario']
#         password = request.POST['senha']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('perfil')
#         else:
#            return render(request, 'registration\login.html')
#     else:
#         return render(request, 'registration\login.html')
    

@login_required
def perfil(request):
    return render(request, 'perfil.html')


def agendamento(request,id):
    form = AgendamentoForm(request.POST or None)
    passeio = Passeio.objects.get(pk=id)
    #passeio = passeio.titulo
    if form.is_valid():
        agendamento = form.save(commit=False)
        agendamento.usuario = request.user
        #passeio_id = request.POST['passeio']
        
        agendamento.save()
        return redirect(passeios)
    contexto = {
        "form": form,
        "passeio": passeio
    }

    return render(request, 'agendamento.html', contexto)

def admAgendamentos(request):
    agenda= Agendamento.objects.all()
    contexto = {
        'agendamento':agenda
    }
    return render(request , "admAgendamento.html", contexto)