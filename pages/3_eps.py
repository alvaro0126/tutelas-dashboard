import streamlit as st
import plotly.express as px
import pandas as pd
from utils.data_loader import load_parquet

st.title("🏥 Responsabilidad EPS")

df = load_parquet("agg_eps_anio")

rank = df.groupby("eps_norm")["n_tutelas"].sum().nlargest(20).reset_index()
fig = px.bar(rank, x="n_tutelas", y="eps_norm", orientation="h",
             title="Top 20 EPS por volumen total de tutelas 2019–2025",
             labels={"n_tutelas": "Total tutelas", "eps_norm": ""},
             template="plotly_white", color_discrete_sequence=["#5c3d7a"])
fig.update_layout(yaxis={"categoryorder": "total ascending"})
st.plotly_chart(fig, use_container_width=True)

st.subheader("Evolución anual por EPS")
top10 = rank["eps_norm"].head(10).tolist()
eps_sel = st.multiselect("Selecciona EPS", top10, default=top10[:5])
df_sel = df[df["eps_norm"].isin(eps_sel)]
fig2 = px.line(df_sel, x="anio", y="n_tutelas", color="eps_norm",
               title="Tutelas por año y EPS",
               labels={"anio": "Año", "n_tutelas": "Tutelas", "eps_norm": "EPS"},
               template="plotly_white")
st.plotly_chart(fig2, use_container_width=True)
