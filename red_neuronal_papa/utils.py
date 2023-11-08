import os
import csv
import pandas as pd
import numpy as np

def procesar_archivo_csv():
    csv_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'potato-production-districtwise.csv')
    resultados = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Omitir la primera fila
        for row in csv_reader:
            # Procesa cada fila como desees y agrega los resultados a la lista
            resultados.append(row)  # Puedes reemplazar esto con tu lógica de procesamiento real
    return resultados

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def procesar_red_neuronal():
    csv_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'potato-production-districtwise.csv')
    resultados = []

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Omitir la primera fila
        for row in csv_reader:
            processed_row = []
            for value in row:
                try:
                    processed_value = float(value)  # Convertir el valor a un número
                except ValueError:
                    processed_value = 0.0  # Si no se puede convertir, establecer en cero
                processed_row.append(processed_value)
            # Realizar cálculo específico para cada fila, por ejemplo, calcular el porcentaje de cada valor respecto a la suma total de la fila
            fila_suma = sum(processed_row)
            if fila_suma != 0:
                fila_porcentajes = [val / fila_suma for val in processed_row]
            else:
                fila_porcentajes = [0] * len(processed_row)  # Si la fila suma cero, asigna ceros a todos los porcentajes
            resultados.append(fila_porcentajes)

    # Simulación de una red neuronal simple con una capa oculta
    # Supongamos que tenemos 3 entradas y 2 salidas en la capa oculta
    np_resultados = np.array(resultados)
    pesos_capa_oculta = np.random.rand(13, 3)  # Pesos para la capa oculta
    pesos_capa_salida = np.random.rand(3, 2)  # Pesos para la capa de salida

    # Propagación hacia adelante
    capa_oculta = sigmoid(np.dot(np_resultados, pesos_capa_oculta))
    salida = np.dot(capa_oculta, pesos_capa_salida)

    interpretacion = "Los datos indican los porcentajes de cada valor en relación con la suma total de cada fila: {}. \n La salida de la red neuronal es: {}.".format(resultados, salida)

    return {'interpretacion': interpretacion}