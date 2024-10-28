
#Airbnb Data Analyst Project

## Descripción del proyecto
Este proyecto, desarrollado por la División de Tracks, permite realizar un análisis exhaustivo de datos de Airbnb. Incluye un análisis exploratorio global de los datos de Airbnb y un modelo predictivo enfocado en estimar los ingresos anuales de propiedades ubicadas en Madrid. La aplicación ofrece un análisis estadístico detallado a través de herramientas de Exploratory Data Analysis (EDA) y visualizaciones interactivas en Power BI, brindando una visión completa y fácilmente interpretable de las tendencias y características del mercado de alquileres vacacionales con Airbnb.

## Integrantes
- [@Dolcevitta95](https://github.com/Dolcevitta95)
- [@jvazquez28](https://github.com/jvazquez28)
- [@EstherTapias](https://github.com/EstherTapias)

## Tecnologías utilizadas
- Python
- Streamlit
- Pandas
- Numpy
- Scikit-learn
- Seaborn
- Matplotlib
- XGBoost
- Power BI

## Funcionalidades Principales
1. Análisis exploratorio de datos global y en Madrid.
   - Exploración detallada de datos a nivel global, utilizando gráficos descriptivos y técnicas de EDA para identificar patrones, correlaciones y variaciones en los datos.
   - Examina distribuciones de precios, tasas de ocupación y características clave en diferentes áreas geográficas.
   - [Ver EDA Usado para el análisis]()
2. Modelo predictivo para estimar ingresos anuales en propiedades de Airbnb en Madrid.
   - Implementación de un modelo de aprendizaje automático para predecir los ingresos anuales de propiedades de Airbnb en Madrid.
   - El modelo considera factores como ubicación, tipo de propiedad, precio por noche, opiniones, disponibilidad anual, etc.
   - [Ver Modelo predictivo desplegado en Streamlit](https://airbnbdataanalys.streamlit.app/)
3. Visualizaciones interactivas en Power BI.
   - Creación de paneles interactivos en Power BI para visualizar datos y resultados de manera intuitiva.
   - Incorpora gráficos dinámicos y filtros para explorar datos de manera interactiva.
   - [Ver Dashboard Completo en PowerBI](https://app.fabric.microsoft.com/view?r=eyJrIjoiMTc0ZDJjNzItYjM1Zi00NTU1LThlM2UtZmE0YmM3NWY2YzQyIiwidCI6ImJlNDViM2I2LWQzOGMtNDBhMi1hMmVmLTk2MWI4YTRmYmM3YiIsImMiOjl9)

## Requisitos
- Python 3.8 o superior
- Pandas 1.3.5 o superior
- Numpy 1.21.2 o superior
- Scikit-learn 0.24.2 o superior
- XGBoost 1.5.1 o superior

## Instrucciones de uso
1. Clona el repositorio en tu máquina local.
2. Instala las dependencias utilizando pip:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación con Streamlit:
   ```bash
   streamlit run app.py
   ```

