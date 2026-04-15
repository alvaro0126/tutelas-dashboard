import streamlit as st
import plotly.express as px
from utils.data_loader import load_parquet

st.title("🛡️ Poblaciones vulnerables")

st.info(
    "Este análisis requiere acceso a microdatos. "
    "Los agregados disponibles muestran tasa de concesión por año y SEP."
)

df = load_parquet("agg_dpto_anio")

fig = px.line(df, x="anio", y="pct_sep",
              color="departamento",
              title="Proporción de casos SEP por departamento y año",
              labels={"anio": "Año", "pct_sep": "% casos SEP", "departamento": "Depto"},
              template="plotly_white")
st.plotly_chart(fig, use_container_width=True)
