from django.db import models

class Evento(models.Model):
    TIPO_EVENTO = [
        ('feriado', 'Feriado'),
        ('examen', 'Examen'),
        ('plazo', 'Plazo administrativo'),
        ('actividad', 'Actividad general'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    tipo = models.CharField(max_length=20, choices=TIPO_EVENTO)
