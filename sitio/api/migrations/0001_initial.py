# Generated by Django 5.1.1 on 2024-11-25 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('tipo', models.CharField(choices=[('inicio_semestre', 'Inicio de Semestre'), ('fin_semestre', 'Fin de Semestre'), ('inicio_inscripcion', 'Inicio de Inscripción de Asignaturas'), ('fin_inscripcion', 'Fin de Inscripción de Asignaturas'), ('receso', 'Receso Académico'), ('feriado_nacional', 'Feriado Nacional'), ('feriado_regional', 'Feriado Regional'), ('inicio_solicitudes', 'Inicio de Plazos de Solicitudes Administrativas'), ('fin_solicitudes', 'Fin de Plazos de Solicitudes Administrativas'), ('inicio_beneficios', 'Inicio de Plazos para la Gestión de Beneficios'), ('fin_beneficios', 'Fin de Plazos para la Gestión de Beneficios'), ('ceremonia_titulacion', 'Ceremonia de Titulación o Graduación'), ('reunion_consejo', 'Reunión de Consejo Académico'), ('taller_charla', 'Talleres y Charlas'), ('orientacion', 'Día de Orientación para Nuevos Estudiantes'), ('extracurricular', 'Eventos Extracurriculares'), ('inicio_clases', 'Inicio de Clases'), ('ultimo_dia_clases', 'Último Día de Clases'), ('puertas_abiertas', 'Día de Puertas Abiertas'), ('suspension_completa', 'Suspensión de Actividades Completa'), ('suspension_parcial', 'Suspensión de Actividades Parcial')], max_length=30)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('aprobado', 'Aprobado'), ('rechazado', 'Rechazado')], max_length=20)),
            ],
        ),
    ]
