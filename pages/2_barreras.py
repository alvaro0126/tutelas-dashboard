import streamlit as st
import plotly.express as px
from utils.drive_loader import load_parquet

st.title("🚧 Barreras de acceso — Pretensiones")

df = load_parquet("agg_pretensiones_anio")

anio_sel = st.selectbox("Año", sorted(df["anio"].unique(), reverse=True))
df_yr = df[df["anio"] == anio_sel]

top = df_yr.groupby("pretensiones")["n"].sum().nlargest(12).reset_index()
fig = px.bar(top, x="n", y="pretensiones", orientation="h",
             title=f"Top 12 pretensiones — {anio_sel}",
             labels={"n": "Número de tutelas", "pretensiones": ""},
             template="plotly_white", color_discrete_sequence=["#5c3d7a"])
fig.update_layout(yaxis={"categoryorder": "total ascending"})
st.plotly_chart(fig, use_container_width=True)
