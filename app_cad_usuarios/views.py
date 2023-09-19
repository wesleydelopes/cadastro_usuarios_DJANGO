from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    # Salvar os dados para o BD
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    # Exibir todos os cadastros em outra pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retorna os dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)
    