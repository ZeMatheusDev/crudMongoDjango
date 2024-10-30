from django.shortcuts import render, get_object_or_404
from .models import Usuario
import secrets
from django.http import JsonResponse
import logging

logger = logging.getLogger('myapp')

def criarConta(request):
    logger.info("Esse é um log de teste enviado para o Graylog")
    usuarios = Usuario.objects.all()
    return render(request, 'index.html', {"usuarios": usuarios})

def salvar(request): 
    email = request.POST.get("email")
    login = request.POST.get("login")
    senha = request.POST.get("senha")
    token = secrets.token_hex(16)  
    Usuario.objects.create(email=email, login=login, senha=senha, token=token)
    usuarios = Usuario.objects.all()
    return render(request, 'home.html', {'usuarios': usuarios})

def home(request):
    usuarios = Usuario.objects.all()
    return render(request, 'home.html', {'usuarios': usuarios})

def editar(request, token):
    usuarioSelecionado = Usuario.objects.get(token=token) 
    return render(request, 'editar.html', {'usuarioSelecionado': usuarioSelecionado})

def update(request):
    email = request.POST.get("email")
    login = request.POST.get("login")
    senha = request.POST.get("senha")
    token = request.POST.get("token")

    Usuario.objects.filter(token=token).update(
        email=email,
        login=login,
        senha=senha
    )
    usuarios = Usuario.objects.all()
    return render(request, 'home.html', {'usuarios': usuarios})

def apagar(request, token):
    Usuario.objects.filter(token=token).delete()
    usuarios = Usuario.objects.all()
    return render(request, 'home.html', {'usuarios': usuarios})

def getUsers(request):
    print("achou")
    usuarios = Usuario.objects.all().values() 
    return JsonResponse(list(usuarios), safe=False) 

