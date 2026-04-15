import streamlit as st
import plotly.express as px
from utils.drive_loader import load_parquet

st.title("👥 Género y edad")

st.info(
    "Análisis de género y edad requiere acceso a microdatos. "
    "Esta página se completa cuando los microdatos están disponibles."
)

df = load_parquet("agg_dpto_anio")
fig = px.bar(df.groupby("anio")["tasa_concesion"].mean().reset_index(),
             x="anio", y="tasa_concesion",
             title="Tasa de concesión promedio nacional por año",
             labels={"anio": "Año", "tasa_concesion": "Tasa concesión"},
             template="plotly_white", color_discrete_sequence=["#5c3d7a"])
fig.update_yaxes(tickformat=".1%")
st.plotly_chart(fig, use_container_width=True)
