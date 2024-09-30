# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Home Principal')


def sobre(request):
    return HttpResponse('Sobre')


def contato(request):
    return HttpResponse('Contato')
