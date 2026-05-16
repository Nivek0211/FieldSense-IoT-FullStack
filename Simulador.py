import requests
import time
import random

# La URL de tu servidor local
url = "http://127.0.0.1:5000/api/lecturas"

print("Iniciando ESP32 Virtual... Presiona Ctrl+C para detener.")

while True:
    # Generamos datos falsos simulando variaciones de clima
    temp_simulada = round(random.uniform(22.0, 28.0), 1)
    hum_simulada = round(random.uniform(50.0, 65.0), 1)
    
    paquete_datos = {
        "sensor_id": "ESP32_VIRTUAL_01",
        "temperatura": temp_simulada,
        "humedad": hum_simulada,
        "latitud": 19.0414,
        "longitud": -98.2063
    }
    
    try:
        # Enviamos los datos (POST)
        respuesta = requests.post(url, json=paquete_datos)
        print(f"📦 Dato enviado -> Temp: {temp_simulada}°C | Hum: {hum_simulada}% | Servidor respondió: {respuesta.status_code}")
    except Exception as e:
        print("Error de conexión con el servidor.")
        
    # Esperamos 5 segundos antes del siguiente envío
    time.sleep(5)