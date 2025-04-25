from datetime import datetime

class AlertaModel:
    def __init__(self, alertas):
        self.alertas = alertas
    def contar_pendientes(self):
        """Cuenta las alertas pendientes (puedes definir el criterio)."""
        return len([alerta for alerta in self.alertas if alerta.get("estado", "pendiente") == "pendiente"])
    
    def obtener_para_chofer(self, chofer, rutas):
        """Obtiene alertas relacionadas con las rutas asignadas a un chofer."""
        return [
            alerta for alerta in self.alertas
            if any(ruta["id"] == alerta.get("ruta_id") and ruta["chofer"] == chofer for ruta in rutas)
        ]

    def crear_chofer(self, mensaje, prioridad, chofer, ruta_relacionada=None):
        """Crea una nueva alerta generada por un chofer."""
        nueva_alerta = {
            "id": len(self.alertas) + 1,
            "mensaje": mensaje,
            "prioridad": prioridad,
            "chofer": chofer,
            "ruta_id": ruta_relacionada,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.alertas.append(nueva_alerta)