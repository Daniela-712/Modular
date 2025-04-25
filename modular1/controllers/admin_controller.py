from views.admin_view import AdminView
from models.ruta import RutaModel
from models.alerta import AlertaModel
from models.historial import HistorialModel
from models.insumo import InsumoModel

class AdminController:
    def __init__(self, root, datos, usuario):
        self.root = root
        self.datos = datos
        self.usuario = usuario

        self.model_ruta = RutaModel(datos["rutas"])
        self.model_alerta = AlertaModel(datos["alertas"])
        self.model_historial = HistorialModel(datos["historial"])
        self.model_insumo = InsumoModel(datos["insumos"])

        self.view = AdminView(
            root,
            self.usuario,
            self.mostrar_dashboard,
            self.crear_ruta,
            self.crear_alerta,
            self.crear_insumo,
            self.mostrar_historial
        )
        self.mostrar_dashboard()

    def mostrar_dashboard(self):
        resumen = {
            "insumos": len(self.model_insumo.insumos),
            "alertas": self.model_alerta.contar_pendientes(),
            "rutas": self.model_ruta.contar_activas()
        }
        self.view.mostrar_dashboard(resumen)

    def crear_ruta(self, origen, destino, chofer, fecha):
        self.model_ruta.crear(origen, destino, chofer, fecha)
        self.model_historial.registrar("Nueva ruta creada", self.usuario)
        self.view.mostrar_mensaje("Ruta creada exitosamente")

    def crear_alerta(self, mensaje, prioridad):
        self.model_alerta.crear(mensaje, prioridad)
        self.model_historial.registrar("Nueva alerta creada", self.usuario)
        self.view.mostrar_mensaje("Alerta creada exitosamente")

    def crear_insumo(self, nombre, descripcion, cantidad, ubicacion, estado):
        self.model_insumo.crear(nombre, descripcion, cantidad, ubicacion, estado)
        self.model_historial.registrar("Nuevo insumo creado", self.usuario)
        self.view.mostrar_mensaje("Insumo registrado correctamente")

    def mostrar_historial(self):
        registros = self.model_historial.obtener()
        self.view.mostrar_historial(registros)
