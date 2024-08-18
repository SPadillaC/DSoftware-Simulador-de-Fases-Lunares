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
- **Visualizar la fase lunar actual con una imagen representativa.**

## Requisitos

- Python 3.x
- Biblioteca `ephem`
- Biblioteca `streamlit`
- **Imágenes de las fases lunares**: Las imágenes en formato `.jpg` deben estar ubicadas en `src/imagenes_fases/`.

## Instalación

1. Clona este repositorio en tu máquina local.

    ```sh
    git clone https://github.com/SPadillaC/DSoftware-Simulador-de-Fases-Lunares.git
    ```

2. Navega al directorio donde deseas utilizar el proyecto.
3. Instala las bibliotecas necesarias.

    ```sh
    pip install ephem streamlit
    ```

## Estructura del Proyecto

```plaintext
simulador_fases_lunares/
│
├── src/
│   ├── simulador_fases_lunares/
│   │   ├── __init__.py
│   │   ├── observador.py
│   │   ├── datos_lunares.py
│   │   └── visualizacion_fase_lunar.py
│   └── imagenes_fases/
│       ├── luna_nueva.jpg
│       ├── creciente_iluminante.jpg
│       ├── cuarto_creciente.jpg
│       ├── gibosa_creciente.jpg
│       ├── luna_llena.jpg
│       ├── gibosa_menguante.jpg
│       ├── cuarto_menguante.jpg
│       ├── creciente_menguante.jpg
│       └── fase_desconocida.jpg
│
├── tests/
│   ├── __init__.py
│   └── test.py
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
- **`tests/test.py`**: Pruebas unitarias para las funciones del proyecto.

## Uso

1. Ejecuta el script principal `main.py`.

    ```sh
    streamlit run main.py
    ```

2. Ingresa la fecha y hora usando los controles en la interfaz.
3. El programa calculará y mostrará la constelación, magnitud, distancia en kilómetros, fase lunar en porcentaje, y las fechas de la siguiente luna nueva y llena.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
