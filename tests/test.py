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

# Test para la función obtener_fase_lunar agrupando casos similares
@pytest.mark.parametrize("fase,creciente,resultado_esperado", [
    (1.1, True, "Fase Desconocida"),
    (-0.1, True, "Fase Desconocida"),
    (0.95, True, "Luna Llena"),
    (1.01, True, "Fase Desconocida"),
    (1.0, True, "Luna Llena"),
    (0.50, True, "Cuarto Creciente"),
    (0.50, False, "Cuarto Menguante"),
])
def test_obtener_fase_lunar(fase, creciente, resultado_esperado):
    assert obtener_fase_lunar(fase, creciente) == resultado_esperado

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

# Test para verificar la función obtener_imagen_fase
@pytest.mark.parametrize("nombre_fase, imagen_esperada", [
    ("Luna Nueva", "luna_nueva.jpg"),
    ("Luna Llena", "luna_llena.jpg"),
    ("Gibosa Menguante", "gibosa_menguante.jpg"),
    ("Fase Desconocida", "fase_desconocida.jpg"),
    ("Fase No Existente", "fase_desconocida.jpg")
])
def test_obtener_imagen_fase(nombre_fase, imagen_esperada):
    assert obtener_imagen_fase(nombre_fase).endswith(imagen_esperada)

# Test para mostrar_imagen_fase, manejando el caso donde la imagen no se encuentra
@patch("src.simulador_fases_lunares.visualizacion_fase_lunar.st.image")
@patch("src.simulador_fases_lunares.visualizacion_fase_lunar.st.error")
@patch("src.simulador_fases_lunares.visualizacion_fase_lunar.os.path.exists", side_effect=lambda path: not path.endswith("luna_nueva.jpg"))
def test_mostrar_imagen_fase_no_existente(mock_os_path_exists, mock_st_error, mock_st_image):
    mostrar_imagen_fase("Luna Nueva", width=150)
    mock_st_error.assert_called_once_with("Error: La imagen para la fase 'Luna Nueva' no se encontró.")
    mock_st_image.assert_called_once_with(os.path.join("src", "imagenes_fases", "fase_desconocida.jpg"), caption="Fase Lunar: Luna Nueva", width=150)
