from django.db import models

class Evento(models.Model):
    TIPOS_EVENTOS = [
        ("EXAMEN", "Examen"),
        ("FERIADO", "Feriado"),
        ("PLAZO", "Plazo Administrativo"),
    ]
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    tipo = models.CharField(max_length=20, choices=TIPOS_EVENTOS)

    def __str__(self):
        return self.titulo
