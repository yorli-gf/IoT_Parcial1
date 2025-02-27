import network
import urequests
import machine
import utime
from wifi_config import SSID, PASSWORD  # Importamos credenciales de Wi-Fi

# Configuración del sensor LM35 en GP26 (ADC0)
adc = machine.ADC(26)

# Configuración de ThingSpeak
THINGSPEAK_API_KEY = "1RKQUY2M8BRZ695X"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Conectar a Wi-Fi
def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    print("Conectando a Wi-Fi...")
    while not wlan.isconnected():
        utime.sleep(1)

    print("Conectado! IP:", wlan.ifconfig()[0])

# Leer temperatura del sensor LM35
def leer_temperatura():
    valor_adc = adc.read_u16()
    voltaje = (valor_adc / 65535) * 3.3  # Convertir lectura ADC a voltaje
    temperatura_celsius = voltaje * 100  # Conversión LM35 (10mV/°C)
    return temperatura_celsius

# Enviar datos a ThingSpeak
def enviar_a_thingspeak(temp):
    url = f"{THINGSPEAK_URL}?api_key={THINGSPEAK_API_KEY}&field1={temp}"
    respuesta = urequests.get(url)
    print(f"Enviado a ThingSpeak: {respuesta.text}")
    respuesta.close()

# Iniciar el programa
conectar_wifi()

while True:
    temperatura = leer_temperatura()
    print(f"Temperatura: {temperatura:.2f}°C")
    enviar_a_thingspeak(temperatura)
    print("-----------------------------------------")
    utime.sleep(180)  # Esperar 180 segundos antes de la siguiente lectura
