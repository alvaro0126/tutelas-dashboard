import streamlit as st
import plotly.express as px
from utils.drive_loader import load_parquet

st.title("📈 Tendencias temporales — 2019–2025")

df = load_parquet("agg_mensual")

anios = sorted(df["anio"].unique())
rango = st.slider("Rango de años", min_value=int(anios[0]),
                  max_value=int(anios[-1]), value=(int(anios[0]), int(anios[-1])))
mask = df["anio"].between(rango[0], rango[1])
df_f = df[mask]

col1, col2, col3 = st.columns(3)
col1.metric("Total tutelas", f"{df_f['n_tutelas'].sum():,.0f}")
col2.metric("Tasa de concesión promedio", f"{df_f['tasa_concesion'].mean():.1%}")
col3.metric("Años analizados", f"{rango[1] - rango[0] + 1}")

HITOS = [
    {"x": "2020-03-01", "label": "COVID-19", "color": "red"},
    {"x": "2022-08-07", "label": "Inicio Petro", "color": "purple"},
]

fig = px.line(df_f, x="fecha", y="n_tutelas",
              title="Volumen mensual de tutelas de salud",
              labels={"fecha": "Mes", "n_tutelas": "Tutelas / mes"},
              template="plotly_white")
for h in HITOS:
    fig.add_vline(x=h["x"], line_dash="dash", line_color=h["color"],
                  annotation_text=h["label"])
st.plotly_chart(fig, use_container_width=True)
