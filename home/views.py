from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    # return HttpResponse('Home Principal')
    return render(request, 'home/index.html')


def sobre(request):
    # return HttpResponse('Sobre')
    return render(request, 'home/sobre.html')


def contato(request):
    # return HttpResponse('Contato')
    return render(request, 'home/contato.html')
