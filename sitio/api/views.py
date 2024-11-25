from django.shortcuts import render
from django.http import JsonResponse
from .models import Evento, Feriado

def calendario_academico(request):
    
    #Filtrar los eventos excluyendo los que están con estado "pendiente" o "rechazado".
    eventos = Evento.objects.exclude(estado__in=["pendiente", "rechazado"])
    
    feriados = Feriado.objects.all()

    #Creamos la DATA de los eventos.
    eventos_data = [
        {
            "titulo": evento.titulo,
            "descripcion": evento.descripcion,
            "fecha_inicio": evento.fecha_inicio,
            "fecha_fin": evento.fecha_fin,
            "tipo": evento.tipo,
            "estado": evento.estado
        }
        for evento in eventos
    ]
    
    #Creamos la DATA para feriados.
    feriados_data = [
        {
            "nombre": feriado.nombre,
            "fecha": feriado.fecha
        }
        for feriado in feriados
    ]

    #Consolidar ambos en un solo JSON.
    calendario = {
        "eventos": eventos_data,
        "feriados": feriados_data
    }

    #Retornamos lo creado.
    return JsonResponse(calendario)