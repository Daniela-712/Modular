from datetime import datetime

class RutaModel:
    def __init__(self, rutas):
        self.rutas = rutas

    def crear(self, origen, destino, chofer, fecha):
        nueva = {
            "id": len(self.rutas) + 1,
            "origen": origen,
            "destino": destino,
            "chofer": chofer,
            "fecha": fecha,
            "estado": "activa",
            "insumos": []
        }
        self.rutas.append(nueva)

    def contar_activas(self):
        return len([r for r in self.rutas if r["estado"] == "activa"])
