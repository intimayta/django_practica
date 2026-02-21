from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.utils import timezone

def indice(request):
    return HttpResponse("Estas en RUTAS") #win+.

def ayuda(request):
    return HttpResponse(
        "Rutas disponibles: /rutas/hola/, /rutas/hola//, "
        "/rutas/suma///, /rutas/buscar/?q=..., /rutas/api/estado/"
    )

def hora_actual(request):
    ahora = timezone.localtime()
    return HttpResponse(f"🕒 Hora local: {ahora:%d-%m-%Y %H:%M:%S}")

def hola_mundo(request):
    return HttpResponse("Hola mundo, Roberto")

def ejer(request):
    return HttpResponse("Ejercicios")

def hola(request):
    return HttpResponse("Hola 👋 (sin nombre)")

def hola_nombre(request, nombre):
    return HttpResponse(f"Hola {nombre.upper()}")

def suma(request, a, b):
    return HttpResponse(f"La suma es: {a} + {b}")

def buscar(request):
    q = request.GET.get("q", "").strip()
    if not q:
        return HttpResponse("😡 Envía un query: /rutas/buscar/?q=django")
    return HttpResponse(f"🔎 Buscando: {q}")

def metodo(request):
    if request.method == "GET":
        return HttpResponse("Estás usando GET ✅")
    if request.method == "POST":
        return HttpResponse("Estás usando POST ✅")
    return HttpResponse(f"Método no manejado: {request.method}", status=405)

def api_estado(request):
    data = {
        "estado": "ok",
        "app": "rutas",
        "ruta": request.path,
        "metodo": request.method,
    }
    return JsonResponse(data)

def edad(request, edad):
    if edad < 0 or edad > 120:
        return HttpResponse("Edad inválida", status=400)
    return HttpResponse(f"<h1>EDAD VALIDA: {edad}</h1>")