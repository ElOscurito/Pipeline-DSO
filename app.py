import requests

def fetch_data(url):
    # Vulnerabilidad SAST: Uso de credenciales hardcodeadas
    api_key = "12345-SUPER-SECRET-KEY"
    response = requests.get(f"{url}?key={api_key}")
    return response.json()
