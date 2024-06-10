# Simulador de Fases Lunares

## Descripción del Proyecto

El "Simulador de Fases Lunares" es una aplicación diseñada para calcular y visualizar la fase de la luna en cualquier fecha y hora. Proporciona detalles adicionales como la constelación en la que se encuentra la luna, su magnitud aparente, la distancia a la Tierra, y las fechas de las próximas lunas nueva y llena.

## Integrantes del Equipo

- **Ariel Rodríguez F.** - Developer
- **Tomás Cortés B.** - Developer
- **Cristóbal Castro L.** - Tester/QA
- **Sebastián Padilla C.** - Scrum Master

## Funcionalidades

- Mostrar la constelación en la que se encuentra la luna.
- Mostrar la magnitud aparente de la luna.
- Mostrar la distancia de la luna a la Tierra en kilómetros.
- Mostrar las fechas de las próximas lunas nueva y llena.

## Requisitos

- Python 3.x
- Biblioteca `ephem`

## Instalación

1. Clona este repositorio en tu máquina local.

    ```sh
    git clone https://github.com/SPadillaC/DSoftware-Simulador-de-Fases-Lunares.git
    ```

2. Navega al directorio donde deseas utilizar el proyecto.
3. Instala la biblioteca `ephem`.

    ```sh
    pip install ephem
    ```

## Estructura del Proyecto

```css
simulador_fases_lunares/
│
├── src/
│ └── simulador_fases_lunares/
│ ├── init.py
│ ├── observador.py
│ ├── datos_lunares.py
│
├── tests/
│ ├── init.py
│ ├── test_datos_lunares.py
│ ├── test_observador.py
│
├── LICENSE
├── README.md
├── pyproject.toml
├── setup.cfg
└── main.py
```

- **`src/simulador_fases_lunares/__init__.py`**: Archivo de inicialización del paquete que permite importar las funciones del módulo.
- **`src/simulador_fases_lunares/observador.py`**: Contiene la función `crear_observador` que configura el observador con la fecha y ubicación especificadas.
- **`src/simulador_fases_lunares/datos_lunares.py`**: Contiene la función `calcular_fase_lunar` que calcula la fase lunar y otros datos relevantes.
- **`tests/test_observador.py`**: Pruebas unitarias para `crear_observador`.
- **`tests/test_datos_lunares.py`**: Pruebas unitarias para `calcular_fase_lunar`.

## Uso

1. Ejecuta el script principal `main.py`.

    ```sh
    python main.py
    ```

2. Ingresa la fecha y hora en el formato solicitado (AAAA-MM-DD HH:MM:SS).
3. El programa calculará y mostrará la constelación, magnitud, distancia en kilómetros, fase lunar en porcentaje, y las fechas de la siguiente luna nueva y llena.

## Ejemplo de Uso

```sh
$ python main.py
Ingrese la fecha y hora (AAAA-MM-DD HH:MM:SS): 2024-06-01 20:00:00
Constelación: Pisces
Magnitud: -11.29
Distancia: 370351 km
Fase: 26.62%
Siguiente Luna Nueva: 2024/6/6 12:37:41
Siguiente Luna Llena: 2024/6/22 01:07:49
```

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
