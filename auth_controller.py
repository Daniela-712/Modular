from models.usuario import Usuario
from views.auth_view import LoginView
from controllers.admin_controller import AdminController
from controllers.chofer_controller import ChoferController

class AuthController:
    def __init__(self, root, datos):
        self.root = root
        self.datos = datos
        self.usuario_actual = None
        self.rol_actual = None
        self.login_view = LoginView(root, self.login)

    def login(self, usuario, contraseña):
        modelo = Usuario(self.datos["usuarios"])
        rol = modelo.validar(usuario, contraseña)

        if rol:
            self.usuario_actual = usuario
            self.rol_actual = rol
            self._redirigir_por_rol()
        else:
            self.login_view.mostrar_error("Usuario o contraseña incorrectos")

    def _redirigir_por_rol(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        if self.rol_actual == "admin":
            AdminController(self.root, self.datos, self.usuario_actual)
        elif self.rol_actual == "chofer":
            ChoferController(self.root, self.datos, self.usuario_actual)
