from django.http import *
from polls.models import *
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def index(request):

    return HttpResponse("Index")


@csrf_exempt
def nueva(request):

    data = json.loads(request.body.decode('utf-8'))

    hoja = hojas(titulo=data['titulo'], columnas=data['columnas'], celdas="[]")

    hoja.save()

    return HttpResponse(hoja.id)



@csrf_exempt
def getHojas(request):

    listaHojas = serializers.serialize("json", hojas.objects.all())

    data = {"Resultados": json.loads(listaHojas)}

    return JsonResponse(data)


@csrf_exempt
def getHoja(request):

    data = json.loads(request.body.decode('utf-8'))

    hoja = serializers.serialize("json", hojas.objects.filter(id=data['id']))

    jsonn = {"Hoja": json.loads(hoja)}

    return JsonResponse(jsonn)


@csrf_exempt
def actualizar(request):

    data = json.loads(request.body.decode('utf-8'))

    hoja = hojas.objects.get(id=data['id'])

    hoja.celdas = data['filas']

    hoja.save()

    return HttpResponse("Actualizado")


@csrf_exempt
def borrar(request):

    data = json.loads(request.body.decode('utf-8'))

    hoja = hojas.objects.get(id=data['id'])

    hoja.delete()

    return HttpResponse("Eliminado")
