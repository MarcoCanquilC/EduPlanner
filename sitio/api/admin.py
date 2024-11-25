from django.contrib import admin
from django.utils.html import format_html
from .models import Evento, Feriado

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'fecha_inicio', 'fecha_fin', 'estado')
    search_fields = ('titulo', 'tipo')
    list_filter = ('tipo', 'estado')

    
    def save_model(self, request, obj, form, change):
        
        feriados = Feriado.objects.filter(fecha__range=[obj.fecha_inicio, obj.fecha_fin])

        if feriados.exists():
           
            conflicto = "El evento tiene un conflicto con los siguientes feriados: " + ", ".join([f"{feriado.nombre} ({feriado.fecha})" for feriado in feriados])
            self.message_user(request, conflicto, level='WARNING')  

        obj.save()

        super().save_model(request, obj, form, change)

admin.site.register(Evento, EventoAdmin)
