from datetime import datetime

class HistorialModel:
    def __init__(self, historial):
        self.historial = historial

    def registrar(self, accion, usuario, detalles="", tipo="admin"):
        self.historial.append({
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "accion": accion,
            "usuario": usuario,
            "detalles": detalles,
            "tipo": tipo
        })

    def obtener(self):
        return self.historial
