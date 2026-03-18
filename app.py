import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Dashboard de Vehículos")

df = pd.read_csv("data/vehicles_us.csv")

st.write("Vista previa de los datos:")
st.dataframe(df.head())

if st.checkbox("Mostrar gráfico de dispersión (Precio vs Odómetro)"):

    fig_scatter = px.scatter(
        df,
        x="odometer",
        y="price",
        title="Precio vs Odómetro"
    )

    st.plotly_chart(fig_scatter)


