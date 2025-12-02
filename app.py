import pandas as pd 
import streamlit as st 
import plotly.graph_objects as go 

vehiculos = pd.read_csv("vehicles_us.csv")

st.header("Vehiculos")

hist_button = st.button("Hacer histograma")

if hist_button :
    st.write("Creacion del histograma")
    fig = go.Figure(data = [go.Histogram(x = vehiculos["condition"])])
    fig.update_layout(title_text = "Calidad de los vehiculos en venta")
    st.plotly_chart(fig, use_container_width=True)
    
    
    
disp_button = st.button("Hacer grafico  de dispersion")

if disp_button :
    st.write("Creacion de grafico de dispersion ")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = vehiculos["price"], y = vehiculos["condition"], mode = "markers"))   
    fig.update_layout(title_text = "Relacion del precio de los vehiculos con la condicion actual del vehiculo")
    st.plotly_chart(fig)

