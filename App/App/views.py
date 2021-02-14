from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

def principal(request):    
    return render(request,"inicio.html")

def registro(request):
    return render(request,"registro.html")

def login(request):
    return render(request,"login.html")
