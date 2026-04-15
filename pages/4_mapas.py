import streamlit as st
import plotly.express as px
import pandas as pd
from utils.data_loader import load_parquet, load_geo_dptos

st.title("🗺️ Disparidades geográficas")

gdf = load_geo_dptos()
df = load_parquet("agg_dpto_anio")

anio_sel = st.selectbox("Año", sorted(df["anio"].unique(), reverse=True))
df_yr = df[df["anio"] == anio_sel]
gdf_yr = gdf.merge(df_yr, on="cod_dpto", how="left")

fig = px.choropleth(
    gdf_yr,
    geojson=gdf_yr.__geo_interface__,
    locations=gdf_yr.index,
    color="n_tutelas",
    color_continuous_scale="Purples",
    hover_name="departamento_geo",
    hover_data={"n_tutelas": True, "tasa_concesion": ":.1%"},
    title=f"Tutelas de salud por departamento — {anio_sel}",
)
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r": 0, "t": 40, "l": 0, "b": 0})
st.plotly_chart(fig, use_container_width=True)
