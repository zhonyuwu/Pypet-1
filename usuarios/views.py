from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def login(request):
    pass


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
    if request.method == 'POST':
        username = request.POST.get('nome')
        email = request.POST.get('email')
        senha1 = request.POST.get('senha')
        senha2 = request.POST.get('confirmar_senha')

        # verificar se os campos foram preenchidos
        for campo in [username, email, senha1]:
            if len(campo.strip()) == 0 or len(campo.strip()) == None:
                messages.add_message(request, constants.ERROR, 'Preencha corretamente todos os campos')
                return render(request, 'cadastro.html')
            
        # verificar se senhas são iguais
        if senha1 != senha2:
            messages.add_message(request, constants.ERROR, 'As senhas devem ser iguais')
            return render(request, 'cadastro.html')
        
        # verifica se senha é maior de 4 caracteres
        if len(senha1) < 4:
            messages.add_message(request, constants.WARNING, 'As senhas devem ter 4 caracteres no mínimo')
            return render(request, 'cadastro.html')
        
        # verifica se o usuário já existe no sistema
        usuario_existe = User.objects.filter(username=username)

        if usuario_existe:
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse nome')
            return render(request, 'cadastro.html')

        # Cadastra o usuário ou retorna erro
        try:
            usuario = User.objects.create_user(username=username, email=email, password=senha1)
            messages.add_message(request, constants.SUCCESS, 'Usuário adicionado com sucesso!')
            return render(request, 'cadastro.html')
        except:
            messages.add_message(request, constants.ERROR, 'Não foi possivel criar o usuário')
            return render(request, 'cadastro.html')



        
