from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from models import Evento  # Cambia "app" por el nombre de tu app
from .serializers import EventoSerializer
from .services import obtener_feriados

class EventoListCreateView(APIView):
    def get(self, request):
        eventos = Evento.objects.all()
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CalendarioConsolidadoView(APIView):
    def get(self, request):
        eventos = Evento.objects.all()
        serializer = EventoSerializer(eventos, many=True)
        feriados = obtener_feriados()
        calendario = {
            "eventos": serializer.data,
            "feriados": feriados,
        }
        return Response(calendario, status=status.HTTP_200_OK)