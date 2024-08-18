# Simulador de Fases Lunares

## Descripción del Proyecto

El "Simulador de Fases Lunares" es una aplicación interactiva desarrollada en Python que permite calcular y visualizar la fase de la luna en cualquier fecha y hora. Además, proporciona información detallada como la constelación en la que se encuentra la luna, su magnitud aparente, la distancia a la Tierra, y las fechas de las próximas lunas nueva y llena. También ofrece una visualización gráfica de la fase lunar actual mediante imágenes representativas.

## Integrantes del Equipo

- **Ariel Rodríguez F.** - Developer
- **Tomás Cortés B.** - Developer
- **Cristóbal Castro L.** - Tester/QA
- **Sebastián Padilla C.** - Scrum Master

## Funcionalidades

- **Cálculo de la fase lunar:** Determina la fase lunar para una fecha y hora específicas.
- **Visualización de la constelación:** Muestra la constelación en la que se encuentra la luna.
- **Magnitud aparente:** Proporciona la magnitud aparente de la luna.
- **Distancia a la Tierra:** Muestra la distancia de la luna a la Tierra en kilómetros.
- **Próximas lunas:** Calcula y muestra las fechas de las próximas lunas nueva y llena.
- **Visualización gráfica:** Muestra una imagen representativa de la fase lunar actual.

## Requisitos

- **Python 3.x**
- **Bibliotecas:**
  - `ephem`: Para cálculos astronómicos.
  - `streamlit`: Para la creación de la interfaz de usuario.
- **Imágenes de las fases lunares:** Las imágenes en formato `.jpg` deben estar ubicadas en `src/imagenes_fases/`.

## Instalación

1. **Clonar el repositorio:**  
   Clona este repositorio en tu máquina local usando el siguiente comando:

    ```sh
    git clone https://github.com/SPadillaC/DSoftware-Simulador-de-Fases-Lunares.git
    ```

2. **Navegar al directorio del proyecto:**  
   Cambia al directorio del proyecto para instalar las dependencias y ejecutar el código.

3. **Instalar las dependencias:**  
   Instala las bibliotecas necesarias ejecutando el siguiente comando:

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

### Descripción de Archivos y Directorios

- **`src/simulador_fases_lunares/__init__.py`**: Inicializa el paquete para permitir la importación de módulos.
- **`src/simulador_fases_lunares/observador.py`**: Contiene la función `crear_observador` que configura un observador astronómico con una fecha y ubicación específica.
- **`src/simulador_fases_lunares/datos_lunares.py`**: Contiene la función `calcular_fase_lunar`, que calcula la fase lunar y otros datos astronómicos relevantes.
- **`src/simulador_fases_lunares/visualizacion_fase_lunar.py`**: Muestra una imagen de la fase lunar actual en la interfaz.
- **`src/imagenes_fases/`**: Contiene las imágenes de las fases lunares utilizadas para la visualización.
- **`tests/test.py`**: Contiene las pruebas unitarias para verificar el correcto funcionamiento de las funciones.

## Uso

1. **Ejecutar la aplicación:**  
   Para iniciar la aplicación, ejecuta el script principal utilizando el siguiente comando:

    ```sh
    streamlit run main.py
    ```

2. **Interacción con la interfaz:**  
   - Selecciona la fecha y hora utilizando los controles deslizantes.
   - Haz clic en "Calcular Fase Lunar" para obtener la fase lunar y demás información.
   - La interfaz mostrará la constelación, magnitud, distancia a la Tierra, fase lunar en porcentaje, y las fechas de la siguiente luna nueva y llena, junto con una imagen representativa de la fase lunar.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
