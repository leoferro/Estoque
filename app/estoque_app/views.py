from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
    return HttpResponse("Olá, essa é a primeira página")