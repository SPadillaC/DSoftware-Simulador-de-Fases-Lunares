import sys
import os

# Ajuste para Jupyter Notebook
if '__file__' not in globals():
    # Si estamos en un entorno interactivo (Jupyter Notebook)
    current_dir = os.getcwd()
else:
    # Si estamos en un script normal
    current_dir = os.path.dirname(__file__)

sys.path.insert(0, os.path.abspath(os.path.join(current_dir, 'src')))

from datetime import datetime
from simulador_fases_lunares.observador import crear_observador # type: ignore
from simulador_fases_lunares.datos_lunares import calcular_fase_lunar # type: ignore

def solicitar_fecha_hora():
    while True:
        fecha_hora_entrada = input("Ingrese la fecha y hora (AAAA-MM-DD HH:MM:SS): ")
        try:
            dt = datetime.strptime(fecha_hora_entrada, "%Y-%m-%d %H:%M:%S")
            return dt
        except ValueError:
            print("Formato de fecha y hora incorrecto. Por favor, intente nuevamente.")

def main():
    # Solicitar fecha y hora al usuario
    dt = solicitar_fecha_hora()
    
    # Crear el observador
    observador = crear_observador(dt)
    
    # Calcular las fases lunares y obtener los datos
    datos_lunares = calcular_fase_lunar(observador)
    
    # Imprimir los resultados en el orden solicitado
    print(f"Constelación: {datos_lunares['constelacion']}")
    print(f"Magnitud: {datos_lunares['magnitud']}")
    print(f"Distancia: {datos_lunares['distancia_km']:.0f} km")
    print(f"Fase: {datos_lunares['fase']:.2f}%")
    print(f"Siguiente Luna Nueva: {datos_lunares['siguiente_luna_nueva']}")
    print(f"Siguiente Luna Llena: {datos_lunares['siguiente_luna_llena']}")

if __name__ == "__main__":
    main()