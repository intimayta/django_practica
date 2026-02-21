from django.shortcuts import render

from django.http import HttpResponse

from django.utils import timezone

# def indice(request):
 #   return HttpResponse("Hola mundo 👌") #win+.

def indice(request):
    variable = "Python + DJANGO"
    contexto = {
        "ahora": timezone.localtime(),
        "lenguajes": ["Angular", "React", "PHP", "Vue"],
        "estado": "completado",
        "variable": variable,
    }
    return render(request, "inicio/inicio.html", contexto)


def pato(request):
    return HttpResponse("Pato 🦆")

def vaca(request):
    return HttpResponse("Vaca 🐮")

def perro(request):
    return HttpResponse("perro 🐶")

def suma(request):
    return HttpResponse("Perro 🐶")

def acerca(request):
    return render(request, "inicio/acerca.html")

def temario(request):
    return render(request, "inicio/temario.html")