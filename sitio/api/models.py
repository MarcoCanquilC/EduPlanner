from django.db import models

# Create your models here.

class Evento(models.Model):
    
    TIPOS_EVENTOS = [

        ('inicio_semestre', 'Inicio de Semestre'),
        ('fin_semestre', 'Fin de Semestre'),
        ('inicio_inscripcion', 'Inicio de Inscripción de Asignaturas'),
        ('fin_inscripcion', 'Fin de Inscripción de Asignaturas'),
        ('receso', 'Receso Académico'),
        ('feriado_nacional', 'Feriado Nacional'),
        ('feriado_regional', 'Feriado Regional'),
        ('inicio_solicitudes', 'Inicio de Plazos de Solicitudes Administrativas'),
        ('fin_solicitudes', 'Fin de Plazos de Solicitudes Administrativas'),
        ('inicio_beneficios', 'Inicio de Plazos para la Gestión de Beneficios'),
        ('fin_beneficios', 'Fin de Plazos para la Gestión de Beneficios'),
        ('ceremonia_titulacion', 'Ceremonia de Titulación o Graduación'),
        ('reunion_consejo', 'Reunión de Consejo Académico'),
        ('taller_charla', 'Talleres y Charlas'),
        ('orientacion', 'Día de Orientación para Nuevos Estudiantes'),
        ('extracurricular', 'Eventos Extracurriculares'),
        ('inicio_clases', 'Inicio de Clases'),
        ('ultimo_dia_clases', 'Último Día de Clases'),
        ('puertas_abiertas', 'Día de Puertas Abiertas'),
        ('suspension_completa', 'Suspensión de Actividades Completa'),
        ('suspension_parcial', 'Suspensión de Actividades Parcial'),
    ]
    
    Estados =[
        
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    tipo = models.CharField(max_length=30, choices=TIPOS_EVENTOS)
    estado = models.CharField(max_length=20, choices=Estados, default='pendiente')

    def __str__(self):
        return self.titulo



class Feriado(models.Model):
   
    nombre = models.CharField(max_length=255)
    fecha = models.DateField()
    region = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha}"
