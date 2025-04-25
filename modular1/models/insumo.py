class InsumoModel:
    def __init__(self, insumos):
        self.insumos = insumos

    def crear(self, nombre, descripcion, cantidad, ubicacion, estado):
        nuevo = {
            "id": len(self.insumos) + 1,
            "nombre": nombre,
            "descripcion": descripcion,
            "cantidad": int(cantidad),
            "ubicacion": ubicacion,
            "estado": estado
        }
        self.insumos.append(nuevo)
