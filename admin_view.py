import tkinter as tk
from tkinter import ttk, messagebox

class AdminView:
    def __init__(self, root, usuario, callback_dashboard, callback_nueva_ruta, callback_nueva_alerta, callback_nuevo_insumo, callback_historial):
        self.root = root
        self.usuario = usuario
        self.callback_dashboard = callback_dashboard
        self.callback_nueva_ruta = callback_nueva_ruta
        self.callback_nueva_alerta = callback_nueva_alerta
        self.callback_nuevo_insumo = callback_nuevo_insumo
        self.callback_historial = callback_historial

        self._configurar_ui()

    def _configurar_ui(self):
        self.root.title("Panel de Administrador")
        self.root.geometry("800x600")

        barra = tk.Frame(self.root, bg="#4a6baf")
        barra.pack(side=tk.LEFT, fill=tk.Y)

        opciones = [
            ("Dashboard", self.callback_dashboard),
            ("Nueva Ruta", self._form_ruta),
            ("Nueva Alerta", self._form_alerta),
            ("Nuevo Insumo", self._form_insumo),
            ("Historial", self.callback_historial)
        ]

        for texto, accion in opciones:
            btn = tk.Button(barra, text=texto, command=accion, bg="#4a6baf", fg="white")
            btn.pack(fill=tk.X, pady=2)

        self.contenido = tk.Frame(self.root)
        self.contenido.pack(fill=tk.BOTH, expand=True)

    def limpiar(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def mostrar_dashboard(self, resumen):
        self.limpiar()
        tk.Label(self.contenido, text="Resumen General", font=("Arial", 16)).pack(pady=10)
        for clave, valor in resumen.items():
            tk.Label(self.contenido, text=f"{clave.capitalize()}: {valor}").pack()

    def _form_ruta(self):
        self.limpiar()
        campos = ["Origen", "Destino", "Chofer", "Fecha"]
        entradas = []
        for campo in campos:
            tk.Label(self.contenido, text=campo).pack()
            entry = tk.Entry(self.contenido)
            entry.pack()
            entradas.append(entry)
        tk.Button(self.contenido, text="Guardar", command=lambda: self.callback_nueva_ruta(*[e.get() for e in entradas])).pack(pady=10)

    def _form_alerta(self):
        self.limpiar()
        tk.Label(self.contenido, text="Mensaje").pack()
        entry_msg = tk.Entry(self.contenido)
        entry_msg.pack()
        tk.Label(self.contenido, text="Prioridad").pack()
        combo = ttk.Combobox(self.contenido, values=["Baja", "Media", "Alta"])
        combo.set("Media")
        combo.pack()
        tk.Button(self.contenido, text="Guardar", command=lambda: self.callback_nueva_alerta(entry_msg.get(), combo.get())).pack(pady=10)

    def _form_insumo(self):
        self.limpiar()
        campos = ["Nombre", "Descripción", "Cantidad", "Ubicación", "Estado"]
        entradas = []
        for campo in campos:
            tk.Label(self.contenido, text=campo).pack()
            entrada = tk.Entry(self.contenido)
            entrada.pack()
            entradas.append(entrada)
        tk.Button(self.contenido, text="Guardar", command=lambda: self.callback_nuevo_insumo(*[e.get() for e in entradas])).pack(pady=10)

    def mostrar_historial(self, registros):
        self.limpiar()
        for registro in registros:
            tk.Label(self.contenido, text=f"{registro['fecha']} - {registro['accion']} ({registro['usuario']})").pack()

    def mostrar_mensaje(self, texto):
        messagebox.showinfo("Éxito", texto)
