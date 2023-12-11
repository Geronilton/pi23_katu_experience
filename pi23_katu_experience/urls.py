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
from core.views import index,passeios,cadastrarPasseio,editarPasseio,deletarPasseio
from core.views import cadastro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name= 'index'),
    path('cadastro/',cadastro , name= 'cadastro'),

    path('passeios/', passeios, name= 'passeios'),
    path('cadastrarPasseio/', cadastrarPasseio, name= 'cadastrarPasseio'),
    path('editarPasseio/<int:id>/',editarPasseio, name= 'editarPasseio'),
    path('deletarPasseio/<int:id>/',deletarPasseio, name= 'deletarPasseio'),
]
