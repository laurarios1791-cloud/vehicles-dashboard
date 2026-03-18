import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Vehicles Dashboard", layout="wide")

# Título
st.title("Dashboard de Vehículos en USA")

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv("data/vehicles_us.csv")

df = load_data()

# Mostrar datos
st.subheader("Vista previa de los datos")
st.dataframe(df.head())

# Histograma
st.subheader("Distribución de precios")
fig_hist = px.histogram(df, x="price", title="Distribución de precios")
st.plotly_chart(fig_hist)

# Checkbox para scatter
st.subheader("🔍 Relación entre variables")

if st.checkbox("Mostrar gráfico Precio vs Odómetro"):
    fig_scatter = px.scatter(
        df,
        x="odometer",
        y="price",
        title="Precio vs Odómetro",
        opacity=0.5
    )
    st.plotly_chart(fig_scatter)


