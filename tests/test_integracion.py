import sys
import os
import unittest
from datetime import datetime

# Ajuste para incluir el directorio src en el PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from simulador_fases_lunares.observador import crear_observador
from simulador_fases_lunares.datos_lunares import calcular_fase_lunar

class TestIntegration(unittest.TestCase):
    def test_integration(self):
        # Fecha y hora para la prueba
        fecha_hora = datetime(2024, 6, 1, 20, 0, 0)
        
        # Crear el observador
        observador = crear_observador(fecha_hora)
        
        # Calcular las fases lunares y obtener los datos
        datos = calcular_fase_lunar(observador)
        
        # Verificar que los datos calculados tienen las claves correctas
        self.assertIn("constelacion", datos)
        self.assertIn("magnitud", datos)
        self.assertIn("distancia_km", datos)
        self.assertIn("fase", datos)
        self.assertIn("siguiente_luna_nueva", datos)
        self.assertIn("siguiente_luna_llena", datos)
        
        # Verificar que la constelación sea una de las posibles esperadas
        constelaciones_esperadas = [
            "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
            "Libra", "Scorpio", "Sagittarius", "Capricornus", "Aquarius", "Pisces"
        ]
        self.assertIn(datos["constelacion"], constelaciones_esperadas)
        self.assertAlmostEqual(datos["distancia_km"], 370351, delta=15000)  # Tolerancia de 15000 km

if __name__ == '__main__':
    unittest.main()