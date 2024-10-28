import streamlit as st
import pandas as pd
import joblib

# Al inicio del archivo, después de los imports
st.set_page_config(layout="wide")

# Agregar CSS personalizado
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, rgba(255, 90, 95, 0.7), rgba(255, 56, 92, 0.7));
        }

        /* Modificar el estilo para los labels de los inputs */
        .stSelectbox label, .stNumberInput label {
            font-size: 3em !important;  /* Tamaño equivalente a h2 */
            font-weight: bold !important;
            color: black !important;
            margin-bottom: 10px !important;
        }
        
        /* Estilo para el resultado de la predicción */
        .prediction-result {
            text-align: center !important;
            padding: 20px !important;
            margin: 20px auto !important;
            font-size: 2em !important;
            background-color: rgba(255, 255, 255, 0.1) !important;
            border-radius: 10px !important;
            width: 80% !important;
        }

        /* Estilo para el texto para mejor contraste */
        .stMarkdown, .stText, h1, h2, h3 {
            color: white !important;
        }

        /* Estilo para los selectbox y number inputs */
        .stSelectbox, .stNumberInput {
            background-color: white;
            border-radius: 5px;
            padding: 10px;
        }

        /* Estilo para el formulario */
        .stForm {
            background-color: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)


# Cargar el modelo
def load_model():
    return joblib.load('model_ingresos_madrid.pkl')


model = load_model()


# Crear una función para hacer predicciones
def predict_ingresos(model, data):
    return model.predict(data)


# diccionario de datos
data_dict = {
    'zona': [
        'zona_Barajas', 'zona_Carabanchel', 'zona_Centro',
        'zona_Chamartín', 'zona_Chamberí', 'zona_Ciudad Lineal',
        'zona_Fuencarral - El Pardo', 'zona_Hortaleza', 'zona_Latina',
        'zona_Moncloa - Aravaca', 'zona_Moratalaz', 'zona_Puente de Vallecas',
        'zona_Retiro', 'zona_Salamanca', 'zona_San Blas - Canillejas',
        'zona_Tetuán', 'zona_Usera', 'zona_Vicálvaro',
        'zona_Villa de Vallecas',
        'zona_Villaverde'
    ],
    'type': ['type_Hotel room', 'type_Private room', 'type_Shared room',
             'type_apt']
}


# Crear la aplicación Streamlit
def main():
    col1, col2 = st.columns([4, 1])  # Proporción 4:1 para el título y logo
    with col1:
        st.title('Predicción de Ingresos Airbnb en Madrid')
    with col2:
        st.image('airbnb_Logo_Bélo.svg.png', width=400)

    # Crear las pestañas
    tab_prediccion, tab_analisis = st.tabs(["Predicción", "Análisis de Datos"])

    with tab_prediccion:
        st.write(
            "Introduce los datos de la propiedad para predecir el ingreso "
            "anual estimado."
        )

        # Crear un formulario para ingresar datos
        with st.form(key='prediction_form'):
            st.write('Ingrese los datos del apartamento:')

            # Selecione la zona y tipo de alojamiento
            area = st.selectbox('Zona', data_dict['zona'])
            type_house = st.selectbox('Tipo de alojamiento', data_dict['type'])

            # Seleccione el precio
            precio_eur = st.number_input('precio noche', min_value=0,
                                         max_value=1000, value=0, step=1)

            # duracion de la estancia
            duracion_minima = st.number_input('Duración mínima de la estancia',
                                              min_value=1, max_value=365,
                                              value=1, step=1)

            # disponibilidad de la propiedad
            disponibilidad_anual = st.number_input('Disponibilidad anual',
                                                   min_value=0, max_value=365,
                                                   value=365, step=1)

            # Botón para hacer la predicción
            submit_button = st.form_submit_button(label='Predecir ingresos')

        if submit_button:
            # Codificación One-Hot de 'zona' y 'type' para el modelo
            zona_encoded = [1 if area == z else 0 for z in data_dict['zona']]
            type_encoded = [1 if type_house == t else 0 for t in data_dict[
                'type']]

            # valores predeterminados
            valores_default = {
                'id': 0,
                'numero_de_opiniones': 31.858803139973492,
                'opiniones_por_mes': 0.8024273626261595,
                'reservas_mensual_estimado': 1.246005221469192,
                'noches_ocupadas_anual_estimado': 93,
                'tasa_ocupacion': 0.35,
                'sector_lujo': 0,
            }
            # Crear DataFrame con todos los campos
            input_data = pd.DataFrame(
                [[valores_default['id'],
                    duracion_minima,
                    valores_default['numero_de_opiniones'],
                    valores_default['opiniones_por_mes'],
                    disponibilidad_anual,
                    precio_eur,
                    valores_default['sector_lujo'],
                    valores_default['reservas_mensual_estimado'],
                    valores_default['noches_ocupadas_anual_estimado'],
                    valores_default['tasa_ocupacion'],
                    *zona_encoded,
                    *type_encoded]],
                columns=['id', 'duracion_minima', 'numero_de_opiniones',
                         'opiniones_por_mes', 'disponibilidad_anual',
                         'precio_eur', 'sector_lujo',
                         'reservas_mensual_estimado',
                         'noches_ocupadas_anual_estimado', 'tasa_ocupacion',
                         *data_dict['zona'], *data_dict['type']]
            )

            # Realizar predicción
            prediction = predict_ingresos(model, input_data)[0]

            # Mostrar el resultado centrado
            st.markdown(
                f"<div class='prediction-result'>"
                f"<h2>Ingreso Anual Estimado:</h2>"
                f"<h1>€{prediction:,.2f}</h1>"
                f"</div>",
                unsafe_allow_html=True
            )
    # Contenido de la pestaña de análisis
    with tab_analisis:
        st.header("Análisis de Datos de Airbnb Madrid")
        st.markdown("[Ver Dashboard Completo en PowerBI](https://app.fabric.microsoft.com/view?r=eyJrIjoiMTc0ZDJjNzItYjM1Zi00NTU1LThlM2UtZmE0YmM3NWY2YzQyIiwidCI6ImJlNDViM2I2LWQzOGMtNDBhMi1hMmVmLTk2MWI4YTRmYmM3YiIsImMiOjl9)")
        # Proporcionar tanto el enlace directo como el dashboard incrustado
        html_code = """
            <iframe
                width="100%"
                height="800"
                length="1600"
                src="https://app.fabric.microsoft.com/view?r=eyJrIjoiMTc0ZDJjNzItYjM1Zi00NTU1LThlM2UtZmE0YmM3NWY2YzQyIiwidCI6ImJlNDViM2I2LWQzOGMtNDBhMi1hMmVmLTk2MWI4YTRmYmM3YiIsImMiOjl9"
                frameborder="0"
                allowFullScreen="true"
                style="aspect-ratio: 16/9; width: 100%;">
            </iframe>
        """
        st.components.v1.html(html_code, height=800)
        # Aquí puedes añadir más elementos de análisis si lo deseas
        st.write("Explora el análisis detallado de los datos de Airbnb en "
                 "Madrid a través de nuestro dashboard interactivo.")


# Ejecutar la aplicación
if __name__ == '__main__':
    main()
