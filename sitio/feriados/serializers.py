from rest_framework import serializers
from models import Evento  # Cambia "app" por el nombre de tu app

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = "__all__"