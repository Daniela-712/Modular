from datetime import datetime

class AlertaModel:
    def __init__(self, alertas):
        self.alertas = alertas

    def crear(self, mensaje, prioridad):
        alerta = {
            "id": len(self.alertas) + 1,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "mensaje": mensaje,
            "prioridad": prioridad,
            "estado": "pendiente"
        }
        self.alertas.append(alerta)

    def contar_pendientes(self):
        return len([a for a in self.alertas if a["estado"] == "pendiente"])
