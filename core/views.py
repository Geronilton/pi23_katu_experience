from django.shortcuts import render, redirect
from .forms import UsuarioForm,PasseioForm, AgendamentoForm
from .models import Usuario, Agendamento, Passeio
from django.contrib.auth import authenticate, login,logout
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


def autenticar(request):
    if request.POST:
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(request, username=usuario,password= senha)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            # contexto usado para mensagens de error.
            contexto = {
             'erro':'Por favor, entre com um CPF e senha corretos. Note que ambos os campos diferenciam maiúsculas e minúsculas.'
            }
            return render(request, 'registration\login.html',contexto)
    else:
        return render(request, 'registration\login.html')



def desconectar(request):
    logout(request)
    return redirect('index')


@login_required
def dados(request, cpf):
    user = Usuario.objects.get(cpf=cpf)
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

@login_required
def cadastrarPasseio(request):
    if request.user.is_superuser:
        form = PasseioForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(passeios)

    contexto = {
            "form": form
        }

    return render(request, "cadastrarPasseio.html",contexto)

@login_required
def editarPasseio(request,id):
    if request.user.is_superuser:
        passeio = Passeio.objects.get(pk=id)
        form = PasseioForm(request.POST or None,request.FILES or None, instance=passeio)
        if form.is_valid():
            form.save()
            return redirect('passeios')
        
        contexto = {
            "form": form
        }

    return render(request, "cadastrarPasseio.html",contexto)

@login_required
def deletarPasseio(request, id):

    passeio = Passeio.objects.get(pk=id)
    passeio.delete()
    return redirect('gerencia_passeio')


@login_required
def perfil(request):
    agenda= Agendamento.objects.all()  
    if request.user.is_superuser:
        contexto = {
        'agendamento':agenda
        }
        return render(request, 'admAgendamento.html',contexto)
       
    return render(request, 'perfil.html')

@login_required
def agendamento(request,id):
    form = AgendamentoForm(request.POST or None)
    passeio = Passeio.objects.get(pk=id)
    if form.is_valid():
        agendamento = form.save(commit=False)
        agendamento.usuario = request.user     
        agendamento.save()
        msg_sucesso="Agendamento realizado com sucesso!"
        contexto = {
            "form": form,
            "passeio": passeio,
            "mensagem": msg_sucesso
        }
        return render(request, 'agendamento.html', contexto)
    contexto = {
        "form": form,
        "passeio": passeio
    }

    return render(request, 'agendamento.html', contexto)

@login_required
def admAgendamentos(request):
    if request.user.is_superuser:
        data =''
        if request.POST:
            data = request.POST['data_proposta']
            agenda= Agendamento.objects.filter(data_proposta=data)
        else:
            agenda= Agendamento.objects.all()

    contexto = {
            'agendamento':agenda
        }
    return render(request , "admAgendamento.html", contexto)


@login_required
def user_passeios(request):
    agendamentos = Agendamento.objects.filter(usuario=request.user)
    contexto = {
        'agendamentos':agendamentos,

    }
    return render(request,'user_passeios.html',contexto)

@login_required
def gerencia_passeio(request):
    if request.user.is_superuser:
        passeios = Passeio.objects.all()
        contexto = {
            "lista_passeios" : passeios
        }

    return render(request, "gerencia_passeio.html", contexto)

def cancelar_agendamento(request,id):
    agendamento = Agendamento.objects.get(pk=id)
    agendamento.delete()

    return redirect('user_passeios')