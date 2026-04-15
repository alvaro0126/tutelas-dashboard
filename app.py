"""Dashboard: Tutelas de Salud en Colombia 2019–2025."""
import streamlit as st

st.set_page_config(
    page_title="Tutelas de Salud — Colombia",
    page_icon="⚖️",
    layout="wide",
)

st.title("⚖️ Tutelas de Salud en Colombia")
st.subheader("Análisis 2019–2025 · Defensoría del Pueblo")

st.markdown("""
Este dashboard presenta el análisis de **~1.6 millones de tutelas de salud**
radicadas en Colombia entre 2019 y 2025.

Usa el menú lateral para navegar por los 7 ejes de análisis:

| # | Eje | Pregunta clave |
|---|-----|----------------|
| 1 | Tendencias temporales | ¿Está empeorando el sistema? |
| 2 | Barreras de acceso | ¿Qué le niegan a la gente? |
| 3 | Responsabilidad EPS | ¿Quién falla más? |
| 4 | Disparidades geográficas | ¿Dónde están las peores brechas? |
| 5 | Poblaciones vulnerables | ¿El sistema protege a los más vulnerables? |
| 6 | Género y edad | ¿Hay brechas de género y edad? |
| 7 | Efectividad judicial | ¿La justicia es consistente? |

---
*Datos: Defensoría del Pueblo · Análisis: Equipo de Análisis*
""")
