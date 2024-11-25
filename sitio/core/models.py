from django.db import models

class Evento(models.Model):
    
    TIPO_EVENTO = [

        ('examen', 'Examen'),
        ('plazo', 'Plazo administrativo'),
        ('actividad', 'Actividad general'),
        
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    tipo = models.CharField(max_length=20, choices=TIPO_EVENTO)


class Feriado(models.Model):

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField()
    tipo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre
