from django.shortcuts import render
from django.http import JsonResponse
import requests

def inicio (request):
    try:
        response = requests.get("http://127.0.0.1:8000/api/calendario/")
        calendario = response.json()
        
    except requests.exceptions.RequestException:
        calendario = {"eventos": [], "feriados": []}

    return render(request, "index.html", {"calendario": calendario})