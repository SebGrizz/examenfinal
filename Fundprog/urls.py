"""Fundprog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from grizzly.views import cantpar,sumpar,raizcuadra,sucesion,sucecond,tabla3,ejer5,sem9ejer2,sem9ejer1,sem9ejer3,sem12ejer1,sem12ejer2,sem12ejer3,sem12ejer4,sem12ejer5
from pagina.views import index, consultoria
urlpatterns = [
    path('admin/', admin.site.urls),
    path('semana9ejer1/', sem9ejer1),
    path('semana9ejer2/', sem9ejer2),
    path('semana9ejer3/', sem9ejer3),
    path('semana9ejer4/', cantpar ),
    path('semana9ejer5/', sumpar ),
    path('semana11ejer1/', raizcuadra),
    path('semana11ejer2/', sucesion),
    path('semana11ejer3/', sucecond),
    path('semana11ejer4/', tabla3),
    path('semana11ejer5/', ejer5),
    path('semana12ejer1/', sem12ejer1),
    path('semana12ejer2/', sem12ejer2),
    path('semana12ejer3/', sem12ejer3),
    path('semana12ejer4/', sem12ejer4),
    path('semana12ejer5/', sem12ejer5),
    path('paginaweb/', index),
    path('paginadjango/', consultoria),

]
