"""
URL configuration for projeto_womakers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# Incluir da pasta base(aplicativo) criada:
from base.views import inicio_teste
from base.views import inicioHtml
from base.views import inicioHtmlArq
# Rodando Valendo:
from base.views import inicio, cadastro

#Lista de Urls
urlpatterns = [
    #http://127.0.0.1:8000/admin/login/?next=/admin/
    path('admin/', admin.site.urls),
    #http://127.0.0.1:8000/
    path('inicio_teste', inicio_teste),
    path('inicioHtml', inicioHtml),
    path('inicioHtmlArq', inicioHtmlArq),
    # path ('inicio', inicio),

    # RODANDO OK
    path('', inicio),
    path('cadastro/', cadastro),
]

'''
Anotação:
    path('', inicio), #O vazio renderiza imediatamente a pagina virando um index sem url específica
    #poderia ser:  #http://127.0.0.1:8000/Inicio
    #path('Inicio', inicio),
'''