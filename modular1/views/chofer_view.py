import tkinter as tk
from tkinter import ttk, messagebox

class ChoferView:
    def __init__(self, root, usuario, rutas, alertas, callback_entrega, callback_alerta):
        self.root = root
        self.usuario = usuario
        self.rutas = rutas
        self.alertas = alertas
        self.callback_entrega = callback_entrega
        self.callback_alerta = callback_alerta

        self._configurar_ui()

    def _configurar_ui(self):
        self.root.title("Panel de Chofer")
        self.root.geometry("800x600")

        barra = tk.Frame(self.root, bg="#4a6baf")
        barra.pack(side=tk.LEFT, fill=tk.Y)

        opciones = [
            ("Mis Rutas", self._ver_rutas),
            ("Confirmar Entrega", self._form_entrega),
            ("Enviar Alerta", self._form_alerta),
            ("Mis Alertas", self._ver_alertas),
        ]

        for texto, accion in opciones:
            btn = tk.Button(barra, text=texto, command=accion, bg="#4a6baf", fg="white")
            btn.pack(fill=tk.X, pady=2)

        self.contenido = tk.Frame(self.root)
        self.contenido.pack(fill=tk.BOTH, expand=True)

        self._ver_rutas()

    def limpiar(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def _ver_rutas(self):
        self.limpiar()
        tk.Label(self.contenido, text="Rutas Asignadas", font=("Arial", 16)).pack(pady=10)
        for ruta in self.rutas:
            texto = f"{ruta['id']}: {ruta['origen']} -> {ruta['destino']} - {ruta['estado']}"
            tk.Label(self.contenido, text=texto).pack()

    def _form_entrega(self):
        self.limpiar()
        tk.Label(self.contenido, text="Confirmar Entrega", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.contenido, text="Ruta ID").pack()
        self.entry_ruta = ttk.Combobox(self.contenido, values=[r["id"] for r in self.rutas if r["estado"] == "activa"])
        self.entry_ruta.pack()

        tk.Label(self.contenido, text="Nombre del receptor").pack()
        self.entry_receptor = tk.Entry(self.contenido)
        self.entry_receptor.pack()

        tk.Label(self.contenido, text="Comentarios").pack()
        self.entry_comentarios = tk.Entry(self.contenido)
        self.entry_comentarios.pack()

        tk.Button(self.contenido, text="Confirmar", command=self._confirmar).pack(pady=10)

    def _confirmar(self):
        ruta = int(self.entry_ruta.get())
        receptor = self.entry_receptor.get()
        comentarios = self.entry_comentarios.get()
        self.callback_entrega(ruta, receptor, comentarios)

    def _form_alerta(self):
        self.limpiar()
        tk.Label(self.contenido, text="Enviar Alerta", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.contenido, text="Mensaje").pack()
        entry_msg = tk.Entry(self.contenido)
        entry_msg.pack()

        tk.Label(self.contenido, text="Prioridad").pack()
        combo_prioridad = ttk.Combobox(self.contenido, values=["Baja", "Media", "Alta"])
        combo_prioridad.set("Media")
        combo_prioridad.pack()

        tk.Label(self.contenido, text="Ruta relacionada (opcional)").pack()
        combo_ruta = ttk.Combobox(self.contenido, values=["Ninguna"] + [str(r["id"]) for r in self.rutas])
        combo_ruta.set("Ninguna")
        combo_ruta.pack()

        tk.Button(self.contenido, text="Enviar", command=lambda: self.callback_alerta(
            entry_msg.get(), combo_prioridad.get(),
            int(combo_ruta.get()) if combo_ruta.get() != "Ninguna" else None
        )).pack(pady=10)

    def _ver_alertas(self):
        self.limpiar()
        tk.Label(self.contenido, text="Mis Alertas", font=("Arial", 16)).pack(pady=10)
        for alerta in self.alertas:
            texto = f"{alerta['fecha']} - {alerta['mensaje']} ({alerta['prioridad']})"
            tk.Label(self.contenido, text=texto).pack()

    def mostrar_mensaje(self, texto):
        messagebox.showinfo("Éxito", texto)
