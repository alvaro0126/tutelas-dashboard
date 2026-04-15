"""Descarga parquets privados desde Google Drive usando Service Account."""
from __future__ import annotations
import io
import json
import tempfile
from pathlib import Path

import pandas as pd
import geopandas as gpd
import streamlit as st
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

# IDs de archivos en Drive (completar después de subir los parquets)
FILE_IDS: dict[str, str] = {
    "agg_mensual": "19fFyrCKPRr7IuRu7fvWGPPk8AW8MGCF7",
    "agg_dpto_anio": "1qKkAtOWk9y0zTvXvoSuKFNxWhqHmXvdB",
    "agg_eps_anio": "1-V5VItJRuQH8W-w0bwbRINyrOTnKfeut",
    "agg_pretensiones_anio": "1hkjgGMGn8NNp_AusOlQw5UMRypYU_Q7E",
    "geo_dptos": "1eoJ1bACAnW8lY8CDTbu7RKcDhh2ZU68H",
}


def _get_credentials() -> Credentials:
    """Obtiene credenciales desde Streamlit secrets."""
    sa_info = json.loads(st.secrets["google"]["service_account_json"])
    return Credentials.from_service_account_info(sa_info, scopes=SCOPES)


def _download_file(service, file_id: str) -> bytes:
    """Descarga un archivo de Drive y retorna su contenido en bytes."""
    request = service.files().get_media(fileId=file_id)
    buf = io.BytesIO()
    downloader = MediaIoBaseDownload(buf, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    return buf.getvalue()


@st.cache_data(ttl=3600, show_spinner="Cargando datos...")
def load_parquet(name: str) -> pd.DataFrame:
    """Carga un parquet desde Drive. Cachea por 1 hora."""
    creds = _get_credentials()
    service = build("drive", "v3", credentials=creds)
    file_id = FILE_IDS[name]
    if not file_id:
        raise ValueError(f"FILE_IDS['{name}'] no configurado. Ver utils/drive_loader.py.")
    data = _download_file(service, file_id)
    return pd.read_parquet(io.BytesIO(data))


@st.cache_data(ttl=3600, show_spinner="Cargando geodatos...")
def load_geo_dptos() -> gpd.GeoDataFrame:
    """Carga GeoDataFrame de departamentos desde Drive."""
    creds = _get_credentials()
    service = build("drive", "v3", credentials=creds)
    file_id = FILE_IDS["geo_dptos"]
    if not file_id:
        raise ValueError("FILE_IDS['geo_dptos'] no configurado.")
    data = _download_file(service, file_id)
    with tempfile.NamedTemporaryFile(suffix=".parquet", delete=False) as tmp:
        tmp.write(data)
        tmp_path = tmp.name
    gdf = gpd.read_parquet(tmp_path)
    Path(tmp_path).unlink()
    return gdf
