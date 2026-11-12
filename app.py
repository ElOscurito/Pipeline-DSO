import os
import requests

def fetch_data(url):
    # Obtener la clave desde una variable de entorno
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("No se ha configurado la API KEY")

    response = requests.get(
        url,
        params={"key": api_key},
        timeout=10
    )

    response.raise_for_status()
    return response.json()
