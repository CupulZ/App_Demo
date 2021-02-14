from django.http import HttpResponse
from django.template import Template, Context

def principal(request):    
    
    externo=open("C:/Users/Cupul29/Desktop/DGIMOB/App/App/Plantillas/inicio.html")
    plt=Template(externo.read())
    externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)

def registro(request):
    externo=open("C:/Users/Cupul29/Desktop/DGIMOB/App/App/Plantillas/registro.html")
    plt=Template(externo.read())
    externo.close()
    ctx=Context()
    documento2=plt.render(ctx)
    return HttpResponse(documento2)

def login(request):
    externo=open("C:/Users/Cupul29/Desktop/DGIMOB/App/App/Plantillas/login.html")
    plt=Template(externo.read())
    externo.close()
    ctx=Context()
    documento3=plt.render(ctx)
    return HttpResponse(documento3)