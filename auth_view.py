import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

class LoginView:
    def __init__(self, root, callback_login):
        self.root = root
        self.callback_login = callback_login
        self.crear_interfaz()

    def crear_interfaz(self):
        self.root.title("Sistema de Monitoreo - Login")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")

        estilo = {
            "fuente": ("Helvetica", 12),
            "color_texto": "#333333",
            "bg": "#f0f0f0",
            "boton_bg": "#4a6baf",
            "boton_fg": "white"
        }

        try:
            path_img = os.path.join("img", "logo.png")
            img = Image.open(path_img).resize((200, 150))
            self.logo_img = ImageTk.PhotoImage(img)
            lbl_img = ttk.Label(self.root, image=self.logo_img)
            lbl_img.pack(pady=20)
        except Exception as e:
            print(f"No se pudo cargar la imagen: {e}")
            ttk.Label(self.root, text="LOGO", font=("Arial", 20)).pack(pady=20)

        ttk.Label(self.root, text="Usuario:", font=estilo["fuente"]).pack(pady=5)
        self.entry_usuario = ttk.Entry(self.root)
        self.entry_usuario.pack(pady=5)

        ttk.Label(self.root, text="Contraseña:", font=estilo["fuente"]).pack(pady=5)
        self.entry_password = ttk.Entry(self.root, show="*")
        self.entry_password.pack(pady=5)

        btn = ttk.Button(self.root, text="Ingresar", command=self._login)
        btn.pack(pady=20)

    def _login(self):
        usuario = self.entry_usuario.get()
        contraseña = self.entry_password.get()
        self.callback_login(usuario, contraseña)

    def mostrar_error(self, mensaje):
        messagebox.showerror("Error", mensaje)

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Bienvenido", mensaje)
