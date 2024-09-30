from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.messages import constants
from django.contrib import messages


def index(request):
    # return HttpResponse('Home Principal')
    messages.add_message(
        request, constants.WARNING, 'Mensagem funcionando !!!')
    return render(request, 'home/index.html')


def sobre(request):
    # return HttpResponse('Sobre')
    return render(request, 'home/sobre.html')


def contato(request):
    # return HttpResponse('Contato')
    return render(request, 'home/contato.html')
