from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, criarConta, editar, update, apagar, getUsers

urlpatterns = [
    path('', home, name="home"),
    path('criarConta', criarConta),
    path('salvar/', salvar, name='salvar'), 
    path('editar/<str:token>/', editar, name='editar'), 
    path('update/', update, name='update'), 
    path('apagar/<str:token>/', apagar, name='apagar'), 
    path('getUsers', getUsers, name="getUsers"),
]