import streamlit as st
import plotly.express as px
from utils.data_loader import load_parquet

st.title("⚖️ Efectividad judicial")

st.info(
    "El análisis completo de impugnaciones (Sankey) requiere acceso a microdatos. "
    "Esta página muestra variación regional en tasa de concesión."
)

df = load_parquet("agg_dpto_anio")
var = (
    df.groupby("departamento")["tasa_concesion"]
    .mean().reset_index()
    .sort_values("tasa_concesion")
)
fig = px.bar(var, x="tasa_concesion", y="departamento", orientation="h",
             title="Tasa de concesión promedio por departamento (2019–2025)",
             labels={"tasa_concesion": "Tasa concesión", "departamento": ""},
             template="plotly_white", color_discrete_sequence=["#5c3d7a"])
fig.update_xaxes(tickformat=".1%")
st.plotly_chart(fig, use_container_width=True)
