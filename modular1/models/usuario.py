class Usuario:
    def __init__(self, usuarios):
        self.usuarios = usuarios

    def validar(self, nombre, contraseña):
        user = self.usuarios.get(nombre)
        if user and user["password"] == contraseña:
            return user["rol"]
        return None
