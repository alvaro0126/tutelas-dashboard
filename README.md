# Tutelas de Salud en Colombia — Dashboard

Dashboard público para explorar ~1.6 millones de tutelas de salud (2019–2025).

**Deploy:** Streamlit Community Cloud

## Ejes de análisis

1. Tendencias temporales
2. Barreras de acceso (pretensiones)
3. Responsabilidad EPS e intervenciones
4. Disparidades geográficas
5. Poblaciones vulnerables
6. Género y edad
7. Efectividad judicial

## Configuración (deploy)

Los datos viven en Google Drive privado. Para hacer deploy en Streamlit Cloud:

1. Crear Service Account en Google Cloud Console
2. Compartir la carpeta `Tutelas-Dashboard-Data/` con el email del Service Account
3. Subir parquets de agregados a esa carpeta
4. Completar `FILE_IDS` en `utils/drive_loader.py` con los IDs de cada archivo
5. Configurar en Streamlit Secrets:

```toml
[google]
service_account_json = "{ ... }"  # JSON completo del Service Account
```

6. Hacer deploy desde GitHub en Streamlit Community Cloud
