import pytest
import ephem
from datetime import datetime
from src.simulador_fases_lunares.observador import crear_observador
from src.simulador_fases_lunares.datos_lunares import calcular_fase_lunar

# python -m pytest tests/test.py

def test_crear_observador():
    fecha_hora = datetime(2024, 6, 1, 20, 0, 0)
    observador = crear_observador(fecha_hora)
    assert observador.date == ephem.Date(fecha_hora)
    assert float(observador.lat) * (180 / 3.14159) == pytest.approx(-33.59217, 0.01)
    assert float(observador.lon) * (180 / 3.14159) == pytest.approx(-70.6996, 0.01)

def test_calcular_fase_lunar():
    fecha_hora = datetime(2024, 6, 1, 20, 0, 0)
    observador = crear_observador(fecha_hora)
    datos = calcular_fase_lunar(observador)
    assert "constelacion" in datos
    assert "magnitud" in datos
    assert "distancia_km" in datos
    assert "fase" in datos
    assert "siguiente_luna_nueva" in datos
    assert "siguiente_luna_llena" in datos
    assert datos["distancia_km"] == pytest.approx(370351, 15000)

def test_fecha_extrema_pasada():
    fecha_hora = datetime(1800, 1, 1, 0, 0, 0)
    observador = crear_observador(fecha_hora)
    datos = calcular_fase_lunar(observador)
    assert datos is not None

def test_fecha_extrema_futura():
    fecha_hora = datetime(3000, 1, 1, 0, 0, 0)
    observador = crear_observador(fecha_hora)
    datos = calcular_fase_lunar(observador)
    assert datos is not None

def test_fecha_incorrecta():
    with pytest.raises(ValueError) as excinfo:
        crear_observador("fecha incorrecta")
    assert "Formato de fecha inválido" in str(excinfo.value)

def test_consistencia():
    fecha_hora = datetime(2024, 6, 1, 20, 0, 0)
    observador1 = crear_observador(fecha_hora)
    observador2 = crear_observador(fecha_hora)
    assert observador1.date == observador2.date

def test_resultados_calculos(capsys: pytest.CaptureFixture[str]):
    fecha_hora = datetime(2024, 6, 1, 20, 0, 0)
    observador = crear_observador(fecha_hora)
    datos = calcular_fase_lunar(observador)
    print(f"Constelación: {datos['constelacion']}")
    print(f"Magnitud: {datos['magnitud']}")
    print(f"Distancia: {datos['distancia_km']:.0f} km")
    print(f"Fase: {datos['fase']:.2f}%")
    captured = capsys.readouterr()
    assert "Constelación" in captured.out
    assert "Magnitud" in captured.out
    assert "Distancia" in captured.out
    assert "Fase" in captured.out

def test_confirmacion_seleccion_fecha(capsys: pytest.CaptureFixture[str]):
    fecha_hora = datetime(2024, 6, 1, 20, 0, 0)
    print(f"Fecha y hora seleccionada: {fecha_hora}")
    captured = capsys.readouterr()
    assert "Fecha y hora seleccionada: 2024-06-01 20:00:00" in captured.out

def test_integracion():
    # Configurar el observador
    fecha_hora = datetime(2024, 6, 1, 20, 0, 0)
    observador = crear_observador(fecha_hora)
    
    # Calcular datos lunares
    datos = calcular_fase_lunar(observador)
    
    # Verificar datos básicos
    assert "constelacion" in datos
    assert "magnitud" in datos
    assert "distancia_km" in datos
    assert "fase" in datos
    assert "siguiente_luna_nueva" in datos
    assert "siguiente_luna_llena" in datos
    
    # Verificar resultados específicos
    assert datos["distancia_km"] > 0
    assert datos["fase"] >= 0
    assert isinstance(datos["siguiente_luna_nueva"], ephem.Date)
    assert isinstance(datos["siguiente_luna_llena"], ephem.Date)
    assert datos["constelacion"] != ""
    assert datos["magnitud"] < 0  # La magnitud aparente debería ser negativa

