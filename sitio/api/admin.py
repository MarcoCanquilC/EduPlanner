from django.contrib import admin
from django.utils.html import format_html
from .models import Evento, Feriado

class EventoAdmin(admin.ModelAdmin):

    #Campos que se mostrarán en la lista de eventos en el panel de administración.
    list_display = ("titulo", "tipo", "fecha_inicio", "fecha_fin", "estado")

    search_fields = ("titulo", "tipo")

    list_filter = ("tipo", "estado")


    #Sobrescribimos el método "save_model" para agregar lógica adicional al guardar un evento.
    def save_model(self, request, obj, form, change):

        #Obtiene todos los feriados que coinciden con el rango de fechas del evento.
        feriados = Feriado.objects.filter(fecha__range=[obj.fecha_inicio, obj.fecha_fin])

        #Verifica si hay feriados en conflicto.
        if feriados.exists():

            #Creamos el conflicto.
            conflicto = "El evento tiene un conflicto con los siguientes feriados: " + ", ".join(
                [f"{feriado.nombre} ({feriado.fecha})" for feriado in feriados]
            )

            #Muestra un mensaje de advertencia en la interfaz de administración.
            self.message_user(request, conflicto, level="WARNING")

        #Guarda el objeto del evento.
        obj.save()

        #Llamamos al método "save_model" de la clase padre para asegurar la funcionalidad base.
        super().save_model(request, obj, form, change)

#Registra el modelo Evento con la clase personalizada EventoAdmin.
admin.site.register(Evento, EventoAdmin)