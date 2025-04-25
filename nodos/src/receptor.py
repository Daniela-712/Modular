import network
import espnow
import sys

# --- CONFIGURACIÓN DE WIFI Y ESP-NOW ---
sta = network.WLAN(network.STA_IF)
sta.active(True)

e = espnow.ESPNow()
e.active(True)

# Escuchar todos los dispositivos (broadcast)
e.add_peer(b'\xFF\xFF\xFF\xFF\xFF\xFF')

print("Esperando datos por ESP-NOW...")

while True:
    try:
        host, msg = e.recv()
        if msg:
            try:
                # Decodificar mensaje
                msg_decoded = msg.decode().strip()
                print(msg_decoded)  # Enviar datos a la computadora por serial
            except UnicodeDecodeError:
                print("Error: Datos no decodificables.")
    except KeyboardInterrupt:
        print("\nSaliendo...")
        sys.exit(0)
