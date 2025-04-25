from datetime import datetime

class EntregaModel:
    def __init__(self, datos):
        self.rutas = datos["rutas"]
        self.insumos = datos["insumos"]
        self.historial = datos["historial"]

    def confirmar(self, ruta_id, receptor, comentarios, chofer):
        ruta = next((r for r in self.rutas if r["id"] == ruta_id), None)
        if not ruta:
            raise Exception("Ruta no encontrada")

        for insumo_id in ruta["insumos"]:
            insumo = next((i for i in self.insumos if i["id"] == insumo_id), None)
            if insumo:
                insumo["estado"] = "Entregado"

        ruta["estado"] = "completada"

        self.historial.append({
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "accion": "Entrega confirmada",
            "usuario": chofer,
            "detalles": f"Receptor: {receptor} / Ruta: {ruta_id}",
            "tipo": "entrega"
        })
