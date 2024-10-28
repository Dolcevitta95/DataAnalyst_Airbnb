import streamlit as st
import pandas as pd
import joblib


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
        'zona_Tetuán', 'zona_Usera', 'zona_Vicálvaro', 'zona_Villa de Vallecas',
        'zona_Villaverde'
    ],
    'type': ['type_Hotel room', 'type_Private room', 'type_Shared room', 'type_apt']
}


# Crear la aplicación Streamlit
def main():
    st.title('Predicción de Ingresos Airbnb en Madrid')
    st.write("Introduce los datos de la propiedad para predecir el ingreso anual estimado.")

    # Crear un formulario para ingresar datos
    with st.form(key='prediction_form'):
        st.write('Ingrese los datos del apartamento:')

        # Selecione la zona y tipo de alojamiento
        area = st.selectbox('Zona', data_dict['zona'])
        type_house = st.selectbox('Tipo de alojamiento', data_dict['type'])

        # duracion de la estancia
        min_stay = st.number_input('Duración mínima de la estancia', min_value=1, max_value=365, value=1, step=1)

        # disponibilidad de la propiedad
        availability_365 = st.number_input('Disponibilidad anual', min_value=0, max_value=365, value=365, step=1)

        # Botón para hacer la predicción
        submit_button = st.form_submit_button(label='Predecir ingresos')

    if submit_button:
        # Codificación One-Hot de 'zona' y 'type' para el modelo
        zona_encoded = [1 if area == z else 0 for z in data_dict['zona']]
        type_encoded = [1 if type_house == t else 0 for t in data_dict['type']]
        # Crear DataFrame con los datos necesarios
        input_data = pd.DataFrame(
            [[*zona_encoded, *type_encoded, min_stay, availability_365]],
            columns=[*data_dict['zona'], *data_dict['type'], 'duracion_minima', 'disponibilidad_anual']
        )

        # Realizar predicción
        prediction = predict_ingresos(model, input_data)[0]

        # Mostrar el resultado
        st.subheader(f"Ingreso Anual Estimado: ${prediction:,.2f}")


# Ejecutar la aplicación
if __name__ == '__main__':
    main()