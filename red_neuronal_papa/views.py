from django.shortcuts import render

from django.http import HttpResponse
from .utils import *

def procesar_csv_view(request):
    procesar_archivo_csv()
    return HttpResponse("Archivo CSV procesado con éxito.")
def ver_resultados_view(request):
    resultados = procesar_archivo_csv()
    resultados_red_neuronal = procesar_red_neuronal()
    return render(request, 'resultados.html', {'resultados': resultados, 'resultados_red_neuronal': resultados_red_neuronal})