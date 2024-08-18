import os
import pytest
import ephem
from datetime import datetime
from src.simulador_fases_lunares.observador import crear_observador
from src.simulador_fases_lunares.datos_lunares import calcular_fase_lunar
from src.simulador_fases_lunares.datos_lunares import obtener_fase_lunar
from src.simulador_fases_lunares.visualizacion_fase_lunar import obtener_imagen_fase, mostrar_imagen_fase
from unittest.mock import patch

# python -m pytest tests/test.py

# Test para la creación del observador
def test_crear_observador():
    fecha_hora = datetime(2024, 6, 1, 20, 0, 0)
    observador = crear_observador(fecha_hora)
    assert observador.date == ephem.Date(fecha_hora)
    assert float(observador.lat) * (180 / 3.14159) == pytest.approx(-33.59217, 0.01)
    assert float(observador.lon) * (180 / 3.14159) == pytest.approx(-70.6996, 0.01)

# Test para el cálculo de la fase lunar con mocking
@patch('src.simulador_fases_lunares.datos_lunares.ephem.Moon')
def test_calcular_fase_lunar(mock_moon):
    mock_moon.return_value.phase = 50.0
    mock_moon.return_value.mag = -12.74
    mock_moon.return_value.earth_distance = 0.00257
    
    # Simula el retorno de la función `constellation`
    with patch('src.simulador_fases_lunares.datos_lunares.ephem.constellation', return_value=('Gemini', 'GEM')):
        observador = crear_observador(datetime(2024, 6, 1, 20, 0, 0))
        datos = calcular_fase_lunar(observador)

        # Verificaciones básicas de contenido
        assert datos["fase"] == 50.0
        assert datos["magnitud"] == -12.74
        assert datos["distancia_km"] == pytest.approx(384400, 1000)  # Aproximadamente la distancia media a la Luna
        assert datos["constelacion"] == 'GEM'
        assert isinstance(datos["siguiente_luna_nueva"], ephem.Date)
        assert isinstance(datos["siguiente_luna_llena"], ephem.Date)

@patch('src.simulador_fases_lunares.datos_lunares.ephem.Moon', side_effect=Exception("Error simulado"))
def test_calcular_fase_lunar_error(mock_moon):
    observador = crear_observador(datetime(2024, 6, 1, 20, 0, 0))
    
    # Verifica que se lanza un ValueError con el mensaje esperado
    with pytest.raises(ValueError, match="Error al calcular la fase lunar"):
        calcular_fase_lunar(observador)

# Test para fechas extremas pasadas
def test_fecha_extrema_pasada():
    fecha_hora = datetime(1800, 1, 1, 0, 0, 0)
    observador = crear_observador(fecha_hora)
    datos = calcular_fase_lunar(observador)
    
    # Verificación de consistencia
    assert 0 <= datos["fase"] <= 100

# Test para fechas extremas futuras
def test_fecha_extrema_futura():
    fecha_hora = datetime(3000, 1, 1, 0, 0, 0)
    observador = crear_observador(fecha_hora)
    datos = calcular_fase_lunar(observador)
    
    # Verificación de consistencia
    assert 0 <= datos["fase"] <= 100

# Test para manejo de fecha incorrecta
def test_fecha_incorrecta():
    with pytest.raises(ValueError) as excinfo:
        crear_observador("fecha incorrecta")
    assert "Formato de fecha inválido" in str(excinfo.value)

# Test de consistencia entre observadores creados con la misma fecha
def test_consistencia():
    fecha_hora = datetime(2024, 6, 1, 20, 0, 0)
    observador1 = crear_observador(fecha_hora)
    observador2 = crear_observador(fecha_hora)
    assert observador1.date == observador2.date

# Test para verificar la salida impresa (usando capsys)
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

# Test para confirmar la selección de la fecha y hora
def test_confirmacion_seleccion_fecha(capsys: pytest.CaptureFixture[str]):
    fecha_hora = datetime(2024, 6, 1, 20, 0, 0)
    print(f"Fecha y hora seleccionada: {fecha_hora}")
    captured = capsys.readouterr()
    assert "Fecha y hora seleccionada: 2024-06-01 20:00:00" in captured.out

# Test para fechas extremas pasadas
def test_fecha_extrema_pasada():
    fecha_hora = datetime(1800, 1, 1, 0, 0, 0)
    observador = crear_observador(fecha_hora)
    datos = calcular_fase_lunar(observador)
    assert datos is not None
    assert datos["nombre_fase_lunar"] == "Luna Nueva" or "Creciente Iluminante"

# Test para fechas extremas recientes
def test_fecha_extrema_reciente():
    fecha_hora = datetime(2024, 1, 1, 0, 0, 0)
    observador = crear_observador(fecha_hora)
    datos = calcular_fase_lunar(observador)
    assert datos is not None
    assert datos["nombre_fase_lunar"] in ["Luna Nueva", "Creciente Iluminante", "Cuarto Creciente", "Gibosa Creciente", "Luna Llena"]

def test_fase_desconocida():
    # Test para fase fuera del rango esperado (> 1)
    assert obtener_fase_lunar(1.1, True) == "Fase Desconocida"
    assert obtener_fase_lunar(-0.1, True) == "Fase Desconocida"

def test_fase_exacta_095():
    assert obtener_fase_lunar(0.95, True) == "Luna Llena"

def test_fase_fuera_de_rango_superior():
    assert obtener_fase_lunar(1.01, True) == "Fase Desconocida"

def test_fase_maxima():
    assert obtener_fase_lunar(1.0, True) == "Fase Desconocida"

# Test de integración que verifica el flujo completo
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
    assert 0 <= datos["fase"] <= 100
    assert isinstance(datos["siguiente_luna_nueva"], ephem.Date)
    assert isinstance(datos["siguiente_luna_llena"], ephem.Date)
    assert datos["constelacion"] != ""
    assert datos["magnitud"] < 0  # La magnitud aparente debería ser negativa

def test_obtener_imagen_fase():
    # Test para verificar que se obtienen las rutas correctas de las imágenes
    assert obtener_imagen_fase("Luna Nueva").endswith("luna_nueva.jpg")
    assert obtener_imagen_fase("Luna Llena").endswith("luna_llena.jpg")
    assert obtener_imagen_fase("Gibosa Menguante").endswith("gibosa_menguante.jpg")
    assert obtener_imagen_fase("Fase Desconocida").endswith("fase_desconocida.jpg")

@patch("src.simulador_fases_lunares.visualizacion_fase_lunar.st.image")
def test_mostrar_imagen_fase(mock_st_image):
    # Normalizar la ruta esperada según el sistema operativo
    expected_path = os.path.normpath("src/imagenes_fases/luna_nueva.jpg")
    mostrar_imagen_fase("Luna Nueva", width=150)
    mock_st_image.assert_called_once_with(expected_path, caption="Fase Lunar: Luna Nueva", width=150)