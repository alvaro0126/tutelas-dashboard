"""Carga parquets desde data/ local (incluidos en el repo)."""
from __future__ import annotations
from pathlib import Path

import pandas as pd
import geopandas as gpd
import streamlit as st

DATA_DIR = Path(__file__).parent.parent / "data"


@st.cache_data(show_spinner="Cargando datos...")
def load_parquet(name: str) -> pd.DataFrame:
    return pd.read_parquet(DATA_DIR / f"{name}.parquet")


@st.cache_data(show_spinner="Cargando geodatos...")
def load_geo_dptos() -> gpd.GeoDataFrame:
    return gpd.read_parquet(DATA_DIR / "geo_dptos.parquet")
