import time
import network
import espnow
import json
import math
from machine import Pin, I2C
import dht
import onewire
import ds18x20
from MPU6050 import MPU6050

# FALTA CONFIGURACIÓN DE SENSOR DE LUZ  
# FALTA CONFIGURACIÓN DE SENSOR DE BATERÍA

# --- CONFIGURACIONES ---
ID = "1"   # Identificador del nodo
LZ = 0        # Luz (configurable)
BAT = 0       # Batería (configurable)

# --- INICIALIZACIÓN DEL WIFI Y ESP-NOW ---
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.config(txpower=78)  # Máxima potencia de transmisión
sta.config(protocol=network.MODE_11B)  # Modo de largo alcance (802.11b)

e = espnow.ESPNow()
e.active(True)
broadcast_mac = b'\xFF\xFF\xFF\xFF\xFF\xFF'
e.add_peer(broadcast_mac)

# --- INICIALIZACIÓN DE SENSORES ---
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
mpu = MPU6050(i2c)

dht22 = None
ds18b20 = None

def roc(t, h):
    """Calcula el punto de rocío usando Magnus-Tetens."""
    a, b = (17.27, 237.7) if t >= 0 else (22.452, 272.55)
    g = math.log(h / 100.0) + (a * t) / (b + t)
    return (b * g) / (a - g)

while True:
    time.sleep(2)

    # --- DATOS POR DEFECTO (-255 = ERROR) ---
    data = {"id": ID, "ta": -255, "ts": -255, "h": -255, "lz": LZ, "roc": -255, "bat": BAT, "a": -255}

    # --- LECTURA DE DHT22 ---
    if dht22 is None:
        try:
            dht22 = dht.DHT22(Pin(5))
        except Exception:
            dht22 = None

    if dht22:
        try:
            dht22.measure()
            t, h = dht22.temperature(), dht22.humidity()
            data["ta"], data["h"], data["roc"] = t, h, roc(t, h)
        except OSError:
            pass

    # --- LECTURA DE DS18B20 ---
    if ds18b20 is None:
        try:
            ds18b20 = ds18x20.DS18X20(onewire.OneWire(Pin(4)))
        except Exception:
            ds18b20 = None

    if ds18b20:
        try:
            roms = ds18b20.scan()
            if roms:
                ds18b20.convert_temp()
                time.sleep(0.75)
                data["ts"] = ds18b20.read_temp(roms[0])
        except OSError:
            pass

    # --- LECTURA DE ACELERACIÓN ---
    try:
        acc = mpu.read_accel_data()
        data["a"] = math.sqrt(acc["x"]**2 + acc["y"]**2 + acc["z"]**2)
    except Exception:
        pass

    # --- ENVIAR DATOS POR SERIAL Y ESP-NOW ---
    json_data = json.dumps(data)
    
    print(json_data)  # Enviar por serial
    e.send(broadcast_mac, json_data)  # Enviar por ESP-NOW

    time.sleep(0.5)
