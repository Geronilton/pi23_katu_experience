"""
URL configuration for pi23_katu_experience project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import index,passeios,cadastrarPasseio,editarPasseio,deletarPasseio,agendamento,admAgendamentos
from core.views import cadastro, perfil, cadastro_admin,dados, user_passeios,gerencia_passeio,autenticar,cancelar_agendamento
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',autenticar, name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("perfil/", perfil, name="perfil"),

    path('admin/', admin.site.urls),
    path('', index, name= 'index'),
    path('cadastro/',cadastro , name= 'cadastro'),
    path('dados/<str:cpf>/', dados, name='dados'),
    path('cadastro_admin/',cadastro_admin , name= 'cadastro_admin'),
    path('user_passeios/',user_passeios , name= 'user_passeios'),


    path('passeios/', passeios, name= 'passeios'),
    path('cadastrarPasseio/', cadastrarPasseio, name= 'cadastrarPasseio'),
    path('editarPasseio/<int:id>/',editarPasseio, name= 'editarPasseio'),
    path('deletarPasseio/<int:id>/',deletarPasseio, name= 'deletarPasseio'),
    path("agendamento/<int:id>/", agendamento, name="agendamento"),
    path("admAgendamentos/", admAgendamentos, name="admAgendamentos"),
    path('gerencia_passeio/', gerencia_passeio, name= 'gerencia_passeio'),
    path("cancelar_agendamento/<int:id>/", cancelar_agendamento, name="cancelar_agendamento"),



]
