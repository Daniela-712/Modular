import serial
import json
import sys
from prettytable import PrettyTable

# Configurar el puerto serial (ajusta el nombre del puerto según corresponda)
PORT = "/dev/ttyUSB0"  # Cambia esto según el puerto del ESP32
BAUDRATE = 115200

try:
    ser = serial.Serial(PORT, BAUDRATE, timeout=1)
except serial.SerialException:
    print(f"Error: No se puede abrir el puerto {PORT}")
    sys.exit(1)

# Crear tabla
tabla = PrettyTable()
tabla.field_names = ["ID", "T_Amb", "T_Sonda", "Hum", "Luz", "Rocío", "Bat", "Acc"]

# Bucle de lectura de datos
while True:
    try:
        linea = ser.readline().decode().strip()  # Leer línea desde serial
        if not linea:
            continue
        
        datos = json.loads(linea)  # Decodificar JSON
        
        # Extraer datos con manejo de valores faltantes
        fila = [
            datos.get("id", "N/A"),
            datos.get("ta", "N/A"),
            datos.get("ts", "N/A"),
            datos.get("h", "N/A"),
            datos.get("lz", "N/A"),
            datos.get("roc", "N/A"),
            datos.get("bat", "N/A"),
            datos.get("a", "N/A"),
        ]
        
        # Agregar nueva fila sin repetir encabezados
        tabla.add_row(fila)
        print("\033c", end="")  # Limpiar pantalla para mostrar solo la tabla actualizada
        print(tabla)
        
    except (json.JSONDecodeError, KeyError):
        print("Error al decodificar JSON, ignorando línea.")
    except KeyboardInterrupt:
        print("\nSaliendo...")
        ser.close()
        sys.exit(0)
