from django.contrib import admin
from .models import  Evento

# Register your models here.
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'fecha_inicio', 'fecha_fin')
    list_filter = ('tipo',)
    search_fields = ('titulo', 'descripcion')