import network
import time
import urequests  # Necesitamos esta librería para hacer solicitudes HTTP
from machine import Pin, ADC

# Configuración WiFi
SSID = "Quintal"
PASSWORD = "M3ridaYucatan"

# Conectar al Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

# Esperar a que se conecte
while not wlan.isconnected():
    print("Conectando a Wi-Fi...")
    time.sleep(1)

print("Conectado a Wi-Fi:", wlan.ifconfig())

# Configuración del ADC para el sensor de temperatura interno
temp_sensor = ADC(4)  
conversion_factor = 3.3 / (65535)

# Configurar la URL de ThingSpeak
write_api_key = "6RMTVPU9436889TG"
url = f"http://api.thingspeak.com/update?api_key={write_api_key}"

# Función para leer la temperatura y enviarla a ThingSpeak
def enviar_datos():
    
    raw_temp = temp_sensor.read_u16() * conversion_factor  # Convertir el valor crudo a voltaje
    temp_celsius = 27 - (raw_temp - 0.706) / 0.001721  # Fórmula para convertir el voltaje a °C

    print("🌡️ Temperatura:", temp_celsius, "°C")
    
    # Enviar los datos a ThingSpeak
    response = urequests.get(url + f"&field1={temp_celsius}")
    if response.status_code == 200:
        print(" Datos enviados:", temp_celsius)
    else:
        print(" Error al enviar los datos.")
    
    response.close()

# Enviar datos cada 180 segundos
while True:
    enviar_datos()
    time.sleep(180)  
