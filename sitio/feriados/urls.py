from django.urls import path
from .views import EventoListCreateView, CalendarioConsolidadoView

urlpatterns = [
    path("eventos/", EventoListCreateView.as_view(), name="eventos"),
    path("calendario/", CalendarioConsolidadoView.as_view(), name="calendario")
]