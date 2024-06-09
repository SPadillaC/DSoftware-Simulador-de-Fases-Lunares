import sys
import os
import unittest
from datetime import datetime
import ephem

# Ajuste para incluir el directorio src en el PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from simulador_fases_lunares.observador import crear_observador

class TestObservador(unittest.TestCase):
    def test_crear_observador(self):
        fecha_hora = datetime(2024, 6, 1, 20, 0, 0)
        observador = crear_observador(fecha_hora)
        self.assertEqual(observador.date, ephem.Date(fecha_hora))
        self.assertAlmostEqual(float(observador.lat), float(ephem.degrees('-33.59217')))
        self.assertAlmostEqual(float(observador.lon), float(ephem.degrees('-70.6996')))
        self.assertEqual(observador.elevation, 570)

if __name__ == '__main__':
    unittest.main()