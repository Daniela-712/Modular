from views.chofer_view import ChoferView
from models.entrega import EntregaModel
from models.historial import HistorialModel
from models.ruta import RutaModel
from models.alerta import AlertaModel
from models.insumo import InsumoModel

class ChoferController:
    def __init__(self, root, datos, usuario):
        self.root = root
        self.datos = datos
        self.usuario = usuario

        self.model_entrega = EntregaModel(datos)
        self.model_historial = HistorialModel(datos["historial"])
        self.model_ruta = RutaModel(datos["rutas"])
        self.model_alerta = AlertaModel(datos["alertas"])
        self.model_insumo = InsumoModel(datos["insumos"])

        self.view = ChoferView(
            root,
            usuario,
            self.model_ruta.obtener_por_chofer(usuario),
            self.model_alerta.obtener_para_chofer(usuario, datos["rutas"]),
            self.confirmar_entrega,
            self.enviar_alerta
        )

    def confirmar_entrega(self, ruta_id, receptor, comentarios):
        self.model_entrega.confirmar(ruta_id, receptor, comentarios, self.usuario)
        self.model_historial.registrar("Confirmación de entrega", self.usuario, f"Ruta {ruta_id}")
        self.view.mostrar_mensaje("Entrega confirmada correctamente")

    def enviar_alerta(self, mensaje, prioridad, ruta_relacionada=None):
        self.model_alerta.crear_chofer(mensaje, prioridad, self.usuario, ruta_relacionada)
        self.model_historial.registrar("Alerta enviada por chofer", self.usuario)
        self.view.mostrar_mensaje("Alerta enviada correctamente")
