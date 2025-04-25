import tkinter as tk
from controllers.auth_controller import AuthController
from utils.file_manager import cargar_datos, guardar_datos

if __name__ == "__main__":
    root = tk.Tk()
    datos = cargar_datos()
    app = AuthController(root, datos)
    root.mainloop()
    guardar_datos(datos)
