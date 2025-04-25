import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os

class SistemaMonitoreoInsumos:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Monitoreo de Insumos")
        self.root.geometry("1000x700")
        
      
        self.usuarios = {
            "admin": {"password": "admin123", "rol": "admin"},
            "chofer1": {"password": "chofer123", "rol": "chofer"}
        }
        
        self.insumos = []
        self.rutas = []
        self.alertas = []
        self.historial = []
        
        self.cargar_datos()
        
     
        self.usuario_actual = None
        self.rol_actual = None
        
        self.crear_interfaz_login()
    
    def cargar_datos(self):
       
        try:
            if os.path.exists("usuarios.json"):
                with open("usuarios.json", "r") as f:
                    self.usuarios = json.load(f)
            
            if os.path.exists("insumos.json"):
                with open("insumos.json", "r") as f:
                    self.insumos = json.load(f)
            
            if os.path.exists("rutas.json"):
                with open("rutas.json", "r") as f:
                    self.rutas = json.load(f)
            
            if os.path.exists("alertas.json"):
                with open("alertas.json", "r") as f:
                    self.alertas = json.load(f)
            
            if os.path.exists("historial.json"):
                with open("historial.json", "r") as f:
                    self.historial = json.load(f)
        except Exception as e:
            print(f"Error al cargar datos: {e}")
    
    def guardar_datos(self):
        
        try:
            with open("usuarios.json", "w") as f:
                json.dump(self.usuarios, f)
            
            with open("insumos.json", "w") as f:
                json.dump(self.insumos, f)
            
            with open("rutas.json", "w") as f:
                json.dump(self.rutas, f)
            
            with open("alertas.json", "w") as f:
                json.dump(self.alertas, f)
            
            with open("historial.json", "w") as f:
                json.dump(self.historial, f)
        except Exception as e:
            print(f"Error al guardar datos: {e}")
    
    def crear_interfaz_login(self):
       
        self.limpiar_interfaz()
        
      
        lbl_logo = ttk.Label(self.root, text="LOGO", font=("Arial", 24))
        lbl_logo.pack(pady=50)
        
       
        lbl_usuario = ttk.Label(self.root, text="NOMBRE DE USUARIO")
        lbl_usuario.pack(pady=5)
        
        self.entry_usuario = ttk.Entry(self.root)
        self.entry_usuario.pack(pady=5)
        
     
        lbl_password = ttk.Label(self.root, text="CONTRASEÑA")
        lbl_password.pack(pady=5)
        
        self.entry_password = ttk.Entry(self.root, show="*")
        self.entry_password.pack(pady=5)
        
     
        btn_login = ttk.Button(self.root, text="Ingresar", command=self.validar_login)
        btn_login.pack(pady=20)
    
    def validar_login(self):
        
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()
        
        if usuario in self.usuarios and self.usuarios[usuario]["password"] == password:
            self.usuario_actual = usuario
            self.rol_actual = self.usuarios[usuario]["rol"]
            self.registrar_historial(f"Inicio de sesión: {usuario}")
            
            if self.rol_actual == "admin":
                self.crear_interfaz_admin()
            elif self.rol_actual == "chofer":
                self.crear_interfaz_chofer()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
    
    def limpiar_interfaz(self):
        
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def crear_interfaz_admin(self):
       
        self.limpiar_interfaz()
        
       
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
       
        sidebar = ttk.Frame(main_frame, width=200, relief=tk.RAISED)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
      
        lbl_logo = ttk.Label(sidebar, text="LOGO", font=("Arial", 16))
        lbl_logo.pack(pady=20)
        
        
        menu_opciones = [
            "GENERAL",
            "RUTAS Y TRANSPORTE",
            "ALERTAS Y NOTIFICACIONES",
            "DATOS",
            "HISTORIAL Y REPORTES",
            "USUARIOS"
        ]
        
        for opcion in menu_opciones:
            btn = ttk.Button(sidebar, text=opcion, command=lambda o=opcion: self.mostrar_modulo_admin(o))
            btn.pack(fill=tk.X, pady=5)
        
        
        btn_salir = ttk.Button(sidebar, text="Salir", command=self.cerrar_sesion)
        btn_salir.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
        
       
        self.content_frame = ttk.Frame(main_frame)
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        
        self.mostrar_modulo_admin("GENERAL")
    
    def crear_interfaz_chofer(self):
        
        self.limpiar_interfaz()
        
 
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
 
        sidebar = ttk.Frame(main_frame, width=200, relief=tk.RAISED)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
   
        lbl_logo = ttk.Label(sidebar, text="LOGO", font=("Arial", 16))
        lbl_logo.pack(pady=20)
        
       
        menu_opciones = [
            "GENERAL",
            "INFORMACIÓN VIAJE",
            "ALERTAS Y NOTIFICACIONES",
            "ENTREGA Y CONFIRMACIÓN",
            "DATOS"
        ]
        
        for opcion in menu_opciones:
            btn = ttk.Button(sidebar, text=opcion, command=lambda o=opcion: self.mostrar_modulo_chofer(o))
            btn.pack(fill=tk.X, pady=5)
        
       
        btn_salir = ttk.Button(sidebar, text="Salir", command=self.cerrar_sesion)
        btn_salir.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
        
       
        self.content_frame = ttk.Frame(main_frame)
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
    
        self.mostrar_modulo_chofer("GENERAL")
    
    def mostrar_modulo_admin(self, modulo):
      
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        lbl_titulo = ttk.Label(self.content_frame, text=modulo, font=("Arial", 16))
        lbl_titulo.pack(pady=10)
        
        if modulo == "GENERAL":
            self.mostrar_dashboard_admin()
        elif modulo == "RUTAS Y TRANSPORTE":
            self.mostrar_rutas_transporte()
        elif modulo == "ALERTAS Y NOTIFICACIONES":
            self.mostrar_alertas_notificaciones()
        elif modulo == "DATOS":
            self.mostrar_gestion_datos()
        elif modulo == "HISTORIAL Y REPORTES":
            self.mostrar_historial_reportes()
        elif modulo == "USUARIOS":
            self.mostrar_gestion_usuarios()
    
    def mostrar_modulo_chofer(self, modulo):
     
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        lbl_titulo = ttk.Label(self.content_frame, text=modulo, font=("Arial", 16))
        lbl_titulo.pack(pady=10)
        
        if modulo == "GENERAL":
            self.mostrar_dashboard_chofer()
        elif modulo == "INFORMACIÓN VIAJE":
            self.mostrar_info_viaje()
        elif modulo == "ALERTAS Y NOTIFICACIONES":
            self.mostrar_alertas_chofer()
        elif modulo == "ENTREGA Y CONFIRMACIÓN":
            self.mostrar_entrega_confirmacion()
        elif modulo == "DATOS":
            self.mostrar_datos_chofer()
    
    def mostrar_dashboard_admin(self):
        
       
        frame_insumos = ttk.LabelFrame(self.content_frame, text="Resumen de Insumos")
        frame_insumos.pack(fill=tk.X, padx=10, pady=5)
        
        lbl_total = ttk.Label(frame_insumos, text=f"Total de insumos registrados: {len(self.insumos)}")
        lbl_total.pack(pady=5)
        
      
        frame_alertas = ttk.LabelFrame(self.content_frame, text="Alertas Recientes")
        frame_alertas.pack(fill=tk.X, padx=10, pady=5)
        
        alertas_recientes = [a for a in self.alertas if a["estado"] == "pendiente"]
        lbl_alertas = ttk.Label(frame_alertas, text=f"Alertas pendientes: {len(alertas_recientes)}")
        lbl_alertas.pack(pady=5)
        
        if alertas_recientes:
            for alerta in alertas_recientes[:3]:  # Mostrar solo las 3 más recientes
                ttk.Label(frame_alertas, text=f"{alerta['fecha']} - {alerta['mensaje']}").pack(anchor=tk.W)
        
       
        frame_rutas = ttk.LabelFrame(self.content_frame, text="Rutas Activas")
        frame_rutas.pack(fill=tk.X, padx=10, pady=5)
        
        rutas_activas = [r for r in self.rutas if r["estado"] == "activa"]
        lbl_rutas = ttk.Label(frame_rutas, text=f"Rutas activas: {len(rutas_activas)}")
        lbl_rutas.pack(pady=5)
    
    def mostrar_rutas_transporte(self):
      
      
        frame_controles = ttk.Frame(self.content_frame)
        frame_controles.pack(fill=tk.X, padx=10, pady=5)
        
        btn_nueva_ruta = ttk.Button(frame_controles, text="Nueva Ruta", command=self.crear_nueva_ruta)
        btn_nueva_ruta.pack(side=tk.LEFT, padx=5)
        
        
        frame_filtros = ttk.Frame(frame_controles)
        frame_filtros.pack(side=tk.RIGHT)
        
        ttk.Label(frame_filtros, text="Filtrar por:").pack(side=tk.LEFT)
        
        self.filtro_tipo_ruta = ttk.Combobox(frame_filtros, values=["Todas", "Activas", "Inactivas", "Completadas"])
        self.filtro_tipo_ruta.set("Todas")
        self.filtro_tipo_ruta.pack(side=tk.LEFT, padx=5)
        self.filtro_tipo_ruta.bind("<<ComboboxSelected>>", self.aplicar_filtro_rutas)
        
    
        frame_tabla = ttk.Frame(self.content_frame)
        frame_tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        columns = ("ID", "Origen", "Destino", "Chofer", "Estado", "Fecha")
        self.tree_rutas = ttk.Treeview(frame_tabla, columns=columns, show="headings")
        
        for col in columns:
            self.tree_rutas.heading(col, text=col)
            self.tree_rutas.column(col, width=100)
        
        self.tree_rutas.pack(fill=tk.BOTH, expand=True)
        
      
        self.actualizar_tabla_rutas()
    
    def actualizar_tabla_rutas(self, filtro=None):
        for item in self.tree_rutas.get_children():
            self.tree_rutas.delete(item)
        
        rutas_mostrar = self.rutas
        
        if filtro == "Activas":
            rutas_mostrar = [r for r in self.rutas if r["estado"] == "activa"]
        elif filtro == "Inactivas":
            rutas_mostrar = [r for r in self.rutas if r["estado"] == "inactiva"]
        elif filtro == "Completadas":
            rutas_mostrar = [r for r in self.rutas if r["estado"] == "completada"]
        
        for ruta in rutas_mostrar:
            self.tree_rutas.insert("", tk.END, values=(
                ruta["id"],
                ruta["origen"],
                ruta["destino"],
                ruta["chofer"],
                ruta["estado"],
                ruta["fecha"]
            ))
    
    def aplicar_filtro_rutas(self, event):
        """Aplicar filtro a la tabla de rutas"""
        filtro = self.filtro_tipo_ruta.get()
        self.actualizar_tabla_rutas(filtro)
    
    def crear_nueva_ruta(self):
       
        dialog = tk.Toplevel(self.root)
        dialog.title("Nueva Ruta")
        dialog.geometry("400x300")
        
        ttk.Label(dialog, text="Origen:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        entry_origen = ttk.Entry(dialog)
        entry_origen.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(dialog, text="Destino:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        entry_destino = ttk.Entry(dialog)
        entry_destino.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(dialog, text="Chofer:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        entry_chofer = ttk.Entry(dialog)
        entry_chofer.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(dialog, text="Fecha:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        entry_fecha = ttk.Entry(dialog)
        entry_fecha.insert(0, datetime.now().strftime("%Y-%m-%d"))
        entry_fecha.grid(row=3, column=1, padx=5, pady=5, sticky=tk.EW)
        
        btn_guardar = ttk.Button(dialog, text="Guardar", command=lambda: self.guardar_nueva_ruta(
            entry_origen.get(),
            entry_destino.get(),
            entry_chofer.get(),
            entry_fecha.get(),
            dialog
        ))
        btn_guardar.grid(row=4, column=1, padx=5, pady=10, sticky=tk.E)
    
    def guardar_nueva_ruta(self, origen, destino, chofer, fecha, dialog):
    
        if not origen or not destino or not chofer:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        nueva_ruta = {
            "id": len(self.rutas) + 1,
            "origen": origen,
            "destino": destino,
            "chofer": chofer,
            "fecha": fecha,
            "estado": "activa",
            "insumos": []
        }
        
        self.rutas.append(nueva_ruta)
        self.guardar_datos()
        self.actualizar_tabla_rutas()
        self.registrar_historial(f"Nueva ruta creada: {origen} -> {destino}")
        
        dialog.destroy()
        messagebox.showinfo("Éxito", "Ruta creada correctamente")
    
    def mostrar_alertas_notificaciones(self):
        
      
        frame_controles = ttk.Frame(self.content_frame)
        frame_controles.pack(fill=tk.X, padx=10, pady=5)
        
        btn_nueva_alerta = ttk.Button(frame_controles, text="Nueva Alerta", command=self.crear_nueva_alerta)
        btn_nueva_alerta.pack(side=tk.LEFT, padx=5)
        
  
        frame_filtros = ttk.Frame(frame_controles)
        frame_filtros.pack(side=tk.RIGHT)
        
        ttk.Label(frame_filtros, text="Filtrar por:").pack(side=tk.LEFT)
        
        self.filtro_tipo_alerta = ttk.Combobox(frame_filtros, values=["Todas", "Pendientes", "Resueltas"])
        self.filtro_tipo_alerta.set("Todas")
        self.filtro_tipo_alerta.pack(side=tk.LEFT, padx=5)
        self.filtro_tipo_alerta.bind("<<ComboboxSelected>>", self.aplicar_filtro_alertas)
        
      
        frame_tabla = ttk.Frame(self.content_frame)
        frame_tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        columns = ("ID", "Fecha", "Mensaje", "Prioridad", "Estado")
        self.tree_alertas = ttk.Treeview(frame_tabla, columns=columns, show="headings")
        
        for col in columns:
            self.tree_alertas.heading(col, text=col)
            self.tree_alertas.column(col, width=100)
        
        self.tree_alertas.pack(fill=tk.BOTH, expand=True)
        
        btn_resolver = ttk.Button(frame_tabla, text="Marcar como Resuelta", command=self.marcar_alerta_resuelta)
        btn_resolver.pack(pady=5)
     
        self.actualizar_tabla_alertas()
    
    def actualizar_tabla_alertas(self, filtro=None):
        
        for item in self.tree_alertas.get_children():
            self.tree_alertas.delete(item)
        
        alertas_mostrar = self.alertas
        
        if filtro == "Pendientes":
            alertas_mostrar = [a for a in self.alertas if a["estado"] == "pendiente"]
        elif filtro == "Resueltas":
            alertas_mostrar = [a for a in self.alertas if a["estado"] == "resuelta"]
        
        for alerta in alertas_mostrar:
            self.tree_alertas.insert("", tk.END, values=(
                alerta["id"],
                alerta["fecha"],
                alerta["mensaje"],
                alerta["prioridad"],
                alerta["estado"]
            ))
    
    def aplicar_filtro_alertas(self, event):
       
        filtro = self.filtro_tipo_alerta.get()
        self.actualizar_tabla_alertas(filtro)
    
    def crear_nueva_alerta(self):
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Nueva Alerta")
        dialog.geometry("400x300")
        
        ttk.Label(dialog, text="Mensaje:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        entry_mensaje = ttk.Entry(dialog)
        entry_mensaje.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(dialog, text="Prioridad:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        entry_prioridad = ttk.Combobox(dialog, values=["Baja", "Media", "Alta", "Crítica"])
        entry_prioridad.set("Media")
        entry_prioridad.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
        
        btn_guardar = ttk.Button(dialog, text="Guardar", command=lambda: self.guardar_nueva_alerta(
            entry_mensaje.get(),
            entry_prioridad.get(),
            dialog
        ))
        btn_guardar.grid(row=2, column=1, padx=5, pady=10, sticky=tk.E)
    
    def guardar_nueva_alerta(self, mensaje, prioridad, dialog):
       
        if not mensaje:
            messagebox.showerror("Error", "El mensaje es obligatorio")
            return
        
        nueva_alerta = {
            "id": len(self.alertas) + 1,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "mensaje": mensaje,
            "prioridad": prioridad,
            "estado": "pendiente"
        }
        
        self.alertas.append(nueva_alerta)
        self.guardar_datos()
        self.actualizar_tabla_alertas()
        self.registrar_historial(f"Nueva alerta creada: {mensaje}")
        
        dialog.destroy()
        messagebox.showinfo("Éxito", "Alerta creada correctamente")
    
    def marcar_alerta_resuelta(self):
        
        seleccion = self.tree_alertas.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una alerta")
            return
        
        item = self.tree_alertas.item(seleccion[0])
        alerta_id = item["values"][0]
        
        for alerta in self.alertas:
            if alerta["id"] == alerta_id:
                alerta["estado"] = "resuelta"
                break
        
        self.guardar_datos()
        self.actualizar_tabla_alertas()
        self.registrar_historial(f"Alerta {alerta_id} marcada como resuelta")
        messagebox.showinfo("Éxito", "Alerta marcada como resuelta")
    
    def mostrar_gestion_datos(self):
        
    
        notebook = ttk.Notebook(self.content_frame)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
     
        tab_insumos = ttk.Frame(notebook)
        notebook.add(tab_insumos, text="Insumos")
        
      
        frame_controles = ttk.Frame(tab_insumos)
        frame_controles.pack(fill=tk.X, padx=10, pady=5)
        
        btn_nuevo_insumo = ttk.Button(frame_controles, text="Nuevo Insumo", command=self.crear_nuevo_insumo)
        btn_nuevo_insumo.pack(side=tk.LEFT, padx=5)
        

        frame_tabla = ttk.Frame(tab_insumos)
        frame_tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        columns = ("ID", "Nombre", "Cantidad", "Ubicación", "Estado")
        self.tree_insumos = ttk.Treeview(frame_tabla, columns=columns, show="headings")
        
        for col in columns:
            self.tree_insumos.heading(col, text=col)
            self.tree_insumos.column(col, width=100)
        
        self.tree_insumos.pack(fill=tk.BOTH, expand=True)
        
        
        self.actualizar_tabla_insumos()
    
    def actualizar_tabla_insumos(self):
       
        for item in self.tree_insumos.get_children():
            self.tree_insumos.delete(item)
        
        for insumo in self.insumos:
            self.tree_insumos.insert("", tk.END, values=(
                insumo["id"],
                insumo["nombre"],
                insumo["cantidad"],
                insumo["ubicacion"],
                insumo["estado"]
            ))
    
    def crear_nuevo_insumo(self):

        dialog = tk.Toplevel(self.root)
        dialog.title("Nuevo Insumo")
        dialog.geometry("400x400")
        
        ttk.Label(dialog, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        entry_nombre = ttk.Entry(dialog)
        entry_nombre.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(dialog, text="Descripción:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        entry_descripcion = ttk.Entry(dialog)
        entry_descripcion.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(dialog, text="Cantidad:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        entry_cantidad = ttk.Entry(dialog)
        entry_cantidad.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(dialog, text="Ubicación:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        entry_ubicacion = ttk.Entry(dialog)
        entry_ubicacion.grid(row=3, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(dialog, text="Estado:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        entry_estado = ttk.Combobox(dialog, values=["Disponible", "Reservado", "En uso", "Agotado"])
        entry_estado.set("Disponible")
        entry_estado.grid(row=4, column=1, padx=5, pady=5, sticky=tk.EW)
        
        btn_guardar = ttk.Button(dialog, text="Guardar", command=lambda: self.guardar_nuevo_insumo(
            entry_nombre.get(),
            entry_descripcion.get(),
            entry_cantidad.get(),
            entry_ubicacion.get(),
            entry_estado.get(),
            dialog
        ))
        btn_guardar.grid(row=5, column=1, padx=5, pady=10, sticky=tk.E)
    
    def guardar_nuevo_insumo(self, nombre, descripcion, cantidad, ubicacion, estado, dialog):
        
        if not nombre or not cantidad or not ubicacion:
            messagebox.showerror("Error", "Nombre, cantidad y ubicación son obligatorios")
            return
        
        try:
            cantidad = int(cantidad)
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número")
            return
        
        nuevo_insumo = {
            "id": len(self.insumos) + 1,
            "nombre": nombre,
            "descripcion": descripcion if descripcion else "Sin descripción",
            "cantidad": cantidad,
            "ubicacion": ubicacion,
            "estado": estado
        }
        
        self.insumos.append(nuevo_insumo)
        self.guardar_datos()
        self.actualizar_tabla_insumos()
        self.registrar_historial(f"Nuevo insumo creado: {nombre}")
        
        dialog.destroy()
        messagebox.showinfo("Éxito", "Insumo creado correctamente")
    
    def mostrar_historial_reportes(self):
        
        frame_controles = ttk.Frame(self.content_frame)
        frame_controles.pack(fill=tk.X, padx=10, pady=5)
        
        btn_generar_reporte = ttk.Button(frame_controles, text="Generar Reporte", command=self.generar_reporte)
        btn_generar_reporte.pack(side=tk.LEFT, padx=5)
        
       
        frame_filtros = ttk.Frame(frame_controles)
        frame_filtros.pack(side=tk.RIGHT)
        
        ttk.Label(frame_filtros, text="Filtrar por:").pack(side=tk.LEFT)
        
        self.filtro_tipo_historial = ttk.Combobox(frame_filtros, values=["Todos", "Usuarios", "Insumos", "Rutas", "Alertas"])
        self.filtro_tipo_historial.set("Todos")
        self.filtro_tipo_historial.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(frame_filtros, text="Fecha:").pack(side=tk.LEFT, padx=5)
        self.filtro_fecha_historial = ttk.Entry(frame_filtros)
        self.filtro_fecha_historial.pack(side=tk.LEFT, padx=5)
        
        btn_aplicar_filtro = ttk.Button(frame_filtros, text="Aplicar", command=self.aplicar_filtro_historial)
        btn_aplicar_filtro.pack(side=tk.LEFT, padx=5)
        
        
        frame_tabla = ttk.Frame(self.content_frame)
        frame_tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        columns = ("Fecha", "Acción", "Usuario", "Detalles")
        self.tree_historial = ttk.Treeview(frame_tabla, columns=columns, show="headings")
        
        for col in columns:
            self.tree_historial.heading(col, text=col)
            self.tree_historial.column(col, width=150)
        
        self.tree_historial.pack(fill=tk.BOTH, expand=True)
        
      
        self.actualizar_tabla_historial()
    
    def actualizar_tabla_historial(self, filtro_tipo=None, filtro_fecha=None):
        
        for item in self.tree_historial.get_children():
            self.tree_historial.delete(item)
        
        historial_mostrar = self.historial
        
        if filtro_tipo and filtro_tipo != "Todos":
            historial_mostrar = [h for h in self.historial if filtro_tipo.lower() in h["tipo"]]
        
        if filtro_fecha:
            historial_mostrar = [h for h in historial_mostrar if filtro_fecha in h["fecha"]]
        
        for registro in historial_mostrar:
            self.tree_historial.insert("", tk.END, values=(
                registro["fecha"],
                registro["accion"],
                registro["usuario"],
                registro["detalles"]
            ))
    
    def aplicar_filtro_historial(self):
        
        filtro_tipo = self.filtro_tipo_historial.get()
        filtro_fecha = self.filtro_fecha_historial.get()
        
        self.actualizar_tabla_historial(filtro_tipo, filtro_fecha)
    
    def generar_reporte(self):
        
        seleccion = self.filtro_tipo_historial.get()
        fecha = self.filtro_fecha_historial.get()
        
        if seleccion == "Todos" and not fecha:
            messagebox.showinfo("Reporte", "Generando reporte completo del historial")
        else:
            messagebox.showinfo("Reporte", f"Generando reporte de {seleccion} para fecha {fecha if fecha else 'todas'}")
    
    def mostrar_gestion_usuarios(self):
        
      
        frame_controles = ttk.Frame(self.content_frame)
        frame_controles.pack(fill=tk.X, padx=10, pady=5)
        
        btn_nuevo_usuario = ttk.Button(frame_controles, text="Nuevo Usuario", command=self.crear_nuevo_usuario)
        btn_nuevo_usuario.pack(side=tk.LEFT, padx=5)
        
      
        frame_tabla = ttk.Frame(self.content_frame)
        frame_tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        columns = ("Usuario", "Rol", "Último Acceso")
        self.tree_usuarios = ttk.Treeview(frame_tabla, columns=columns, show="headings")
        
        for col in columns:
            self.tree_usuarios.heading(col, text=col)
            self.tree_usuarios.column(col, width=150)
        
        self.tree_usuarios.pack(fill=tk.BOTH, expand=True)
        
       
        frame_botones = ttk.Frame(frame_tabla)
        frame_botones.pack(fill=tk.X, pady=5)
        
        btn_editar = ttk.Button(frame_botones, text="Editar", command=self.editar_usuario)
        btn_editar.pack(side=tk.LEFT, padx=5)
        
        btn_eliminar = ttk.Button(frame_botones, text="Eliminar", command=self.eliminar_usuario)
        btn_eliminar.pack(side=tk.LEFT, padx=5)
        
        
        self.actualizar_tabla_usuarios()
    
    def actualizar_tabla_usuarios(self):
        
        for item in self.tree_usuarios.get_children():
            self.tree_usuarios.delete(item)
        
        for usuario, datos in self.usuarios.items():
            self.tree_usuarios.insert("", tk.END, values=(
                usuario,
                datos["rol"],
                datos.get("ultimo_acceso", "Nunca")
            ))
    
    def crear_nuevo_usuario(self):
     
        dialog = tk.Toplevel(self.root)
        dialog.title("Nuevo Usuario")
        dialog.geometry("400x300")
        
        ttk.Label(dialog, text="Nombre de usuario:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        entry_usuario = ttk.Entry(dialog)
        entry_usuario.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(dialog, text="Contraseña:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        entry_password = ttk.Entry(dialog, show="*")
        entry_password.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(dialog, text="Confirmar contraseña:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        entry_confirm = ttk.Entry(dialog, show="*")
        entry_confirm.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(dialog, text="Rol:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        entry_rol = ttk.Combobox(dialog, values=["admin", "chofer"])
        entry_rol.set("chofer")
        entry_rol.grid(row=3, column=1, padx=5, pady=5, sticky=tk.EW)
        
        btn_guardar = ttk.Button(dialog, text="Guardar", command=lambda: self.guardar_nuevo_usuario(
            entry_usuario.get(),
            entry_password.get(),
            entry_confirm.get(),
            entry_rol.get(),
            dialog
        ))
        btn_guardar.grid(row=4, column=1, padx=5, pady=10, sticky=tk.E)
    
    def guardar_nuevo_usuario(self, usuario, password, confirm, rol, dialog):
      
        if not usuario or not password:
            messagebox.showerror("Error", "Usuario y contraseña son obligatorios")
            return
        
        if password != confirm:
            messagebox.showerror("Error", "Las contraseñas no coinciden")
            return
        
        if usuario in self.usuarios:
            messagebox.showerror("Error", "El usuario ya existe")
            return
        
        self.usuarios[usuario] = {
            "password": password,
            "rol": rol
        }
        
        self.guardar_datos()
        self.actualizar_tabla_usuarios()
        self.registrar_historial(f"Nuevo usuario creado: {usuario} ({rol})")
        
        dialog.destroy()
        messagebox.showinfo("Éxito", "Usuario creado correctamente")
    
    def editar_usuario(self):
      
        seleccion = self.tree_usuarios.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un usuario")
            return
        
        item = self.tree_usuarios.item(seleccion[0])
        usuario = item["values"][0]
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Editar Usuario")
        dialog.geometry("400x300")
        
        ttk.Label(dialog, text="Nombre de usuario:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        lbl_usuario = ttk.Label(dialog, text=usuario)
        lbl_usuario.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        
        ttk.Label(dialog, text="Nueva contraseña:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        entry_password = ttk.Entry(dialog, show="*")
        entry_password.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(dialog, text="Confirmar contraseña:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        entry_confirm = ttk.Entry(dialog, show="*")
        entry_confirm.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(dialog, text="Rol:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        entry_rol = ttk.Combobox(dialog, values=["admin", "chofer"])
        entry_rol.set(self.usuarios[usuario]["rol"])
        entry_rol.grid(row=3, column=1, padx=5, pady=5, sticky=tk.EW)
        
        btn_guardar = ttk.Button(dialog, text="Guardar", command=lambda: self.actualizar_usuario(
            usuario,
            entry_password.get(),
            entry_confirm.get(),
            entry_rol.get(),
            dialog
        ))
        btn_guardar.grid(row=4, column=1, padx=5, pady=10, sticky=tk.E)
    
    def actualizar_usuario(self, usuario, password, confirm, rol, dialog):
    
        if password and password != confirm:
            messagebox.showerror("Error", "Las contraseñas no coinciden")
            return
        
        if password:
            self.usuarios[usuario]["password"] = password
        
        self.usuarios[usuario]["rol"] = rol
        
        self.guardar_datos()
        self.actualizar_tabla_usuarios()
        self.registrar_historial(f"Usuario actualizado: {usuario}")
        
        dialog.destroy()
        messagebox.showinfo("Éxito", "Usuario actualizado correctamente")
    
    def eliminar_usuario(self):
      
        seleccion = self.tree_usuarios.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un usuario")
            return
        
        item = self.tree_usuarios.item(seleccion[0])
        usuario = item["values"][0]
        
        if usuario == self.usuario_actual:
            messagebox.showerror("Error", "No puede eliminarse a sí mismo")
            return
        
        if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar al usuario {usuario}?"):
            del self.usuarios[usuario]
            self.guardar_datos()
            self.actualizar_tabla_usuarios()
            self.registrar_historial(f"Usuario eliminado: {usuario}")
            messagebox.showinfo("Éxito", "Usuario eliminado correctamente")
    
    def mostrar_dashboard_chofer(self):
        
    
        frame_info = ttk.LabelFrame(self.content_frame, text="Información del Chofer")
        frame_info.pack(fill=tk.X, padx=10, pady=5)
        
        lbl_nombre = ttk.Label(frame_info, text=f"Nombre: {self.usuario_actual}")
        lbl_nombre.pack(anchor=tk.W, pady=2)
        
       
        frame_rutas = ttk.LabelFrame(self.content_frame, text="Rutas Asignadas")
        frame_rutas.pack(fill=tk.X, padx=10, pady=5)
        
        rutas_chofer = [r for r in self.rutas if r["chofer"] == self.usuario_actual and r["estado"] == "activa"]
        lbl_rutas = ttk.Label(frame_rutas, text=f"Rutas activas: {len(rutas_chofer)}")
        lbl_rutas.pack(anchor=tk.W, pady=2)
        
        if rutas_chofer:
            for ruta in rutas_chofer[:3]:  # Mostrar solo las 3 más recientes
                ttk.Label(frame_rutas, text=f"{ruta['origen']} -> {ruta['destino']} - {ruta['fecha']}").pack(anchor=tk.W)
        
       
        frame_alertas = ttk.LabelFrame(self.content_frame, text="Alertas Recientes")
        frame_alertas.pack(fill=tk.X, padx=10, pady=5)
        
        alertas_recientes = [a for a in self.alertas if a["estado"] == "pendiente"]
        lbl_alertas = ttk.Label(frame_alertas, text=f"Alertas pendientes: {len(alertas_recientes)}")
        lbl_alertas.pack(anchor=tk.W, pady=2)
        
        if alertas_recientes:
            for alerta in alertas_recientes[:3]:  # Mostrar solo las 3 más recientes
                ttk.Label(frame_alertas, text=f"{alerta['fecha']} - {alerta['mensaje']}").pack(anchor=tk.W)
    
    def mostrar_info_viaje(self):
       
        frame_rutas = ttk.LabelFrame(self.content_frame, text="Mis Rutas")
        frame_rutas.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        rutas_chofer = [r for r in self.rutas if r["chofer"] == self.usuario_actual]
        
        if not rutas_chofer:
            ttk.Label(frame_rutas, text="No tiene rutas asignadas").pack(pady=20)
            return
        
     
        columns = ("ID", "Origen", "Destino", "Estado", "Fecha")
        tree_rutas = ttk.Treeview(frame_rutas, columns=columns, show="headings")
        
        for col in columns:
            tree_rutas.heading(col, text=col)
            tree_rutas.column(col, width=100)
        
        tree_rutas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        for ruta in rutas_chofer:
            tree_rutas.insert("", tk.END, values=(
                ruta["id"],
                ruta["origen"],
                ruta["destino"],
                ruta["estado"],
                ruta["fecha"]
            ))
        
  
        btn_detalles = ttk.Button(frame_rutas, text="Ver Detalles", command=lambda: self.mostrar_detalles_ruta(tree_rutas))
        btn_detalles.pack(pady=5)
    
    def mostrar_detalles_ruta(self, tree):
        seleccion = tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una ruta")
            return
        
        item = tree.item(seleccion[0])
        ruta_id = item["values"][0]
        
        ruta = next((r for r in self.rutas if r["id"] == ruta_id), None)
        if not ruta:
            messagebox.showerror("Error", "Ruta no encontrada")
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Detalles de Ruta {ruta_id}")
        dialog.geometry("500x400")
        
        frame_info = ttk.LabelFrame(dialog, text="Información de la Ruta")
        frame_info.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(frame_info, text=f"Origen: {ruta['origen']}").pack(anchor=tk.W)
        ttk.Label(frame_info, text=f"Destino: {ruta['destino']}").pack(anchor=tk.W)
        ttk.Label(frame_info, text=f"Fecha: {ruta['fecha']}").pack(anchor=tk.W)
        ttk.Label(frame_info, text=f"Estado: {ruta['estado']}").pack(anchor=tk.W)
        
       
        frame_insumos = ttk.LabelFrame(dialog, text="Insumos")
        frame_insumos.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        if not ruta["insumos"]:
            ttk.Label(frame_insumos, text="No hay insumos asignados").pack(pady=10)
        else:
            columns = ("ID", "Nombre", "Cantidad")
            tree_insumos = ttk.Treeview(frame_insumos, columns=columns, show="headings")
            
            for col in columns:
                tree_insumos.heading(col, text=col)
                tree_insumos.column(col, width=100)
            
            tree_insumos.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
            
            for insumo_id in ruta["insumos"]:
                insumo = next((i for i in self.insumos if i["id"] == insumo_id), None)
                if insumo:
                    tree_insumos.insert("", tk.END, values=(
                        insumo["id"],
                        insumo["nombre"],
                        insumo["cantidad"]
                    ))
        
      
        frame_botones = ttk.Frame(dialog)
        frame_botones.pack(fill=tk.X, padx=10, pady=5)
        
        if ruta["estado"] == "activa":
            btn_completar = ttk.Button(frame_botones, text="Marcar como Completada", 
                                     command=lambda: self.marcar_ruta_completada(ruta_id, dialog))
            btn_completar.pack(side=tk.LEFT, padx=5)
    
    def marcar_ruta_completada(self, ruta_id, dialog):
      
        for ruta in self.rutas:
            if ruta["id"] == ruta_id:
                ruta["estado"] = "completada"
                break
        
        self.guardar_datos()
        self.registrar_historial(f"Ruta {ruta_id} marcada como completada por {self.usuario_actual}")
        
        dialog.destroy()
        messagebox.showinfo("Éxito", "Ruta marcada como completada")
        self.mostrar_info_viaje()  # Actualizar la vista
    
    def mostrar_alertas_chofer(self):
      
        frame_controles = ttk.Frame(self.content_frame)
        frame_controles.pack(fill=tk.X, padx=10, pady=5)
        
        btn_nueva_alerta = ttk.Button(frame_controles, text="Nueva Alerta", command=self.crear_nueva_alerta_chofer)
        btn_nueva_alerta.pack(side=tk.LEFT, padx=5)
        
       
        frame_tabla = ttk.Frame(self.content_frame)
        frame_tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        columns = ("ID", "Fecha", "Mensaje", "Prioridad", "Estado")
        tree_alertas = ttk.Treeview(frame_tabla, columns=columns, show="headings")
        
        for col in columns:
            tree_alertas.heading(col, text=col)
            tree_alertas.column(col, width=100)
        
        tree_alertas.pack(fill=tk.BOTH, expand=True)
        
        
        alertas_chofer = [a for a in self.alertas if a.get("usuario") == self.usuario_actual or 
                         ("ruta" in a and any(r["chofer"] == self.usuario_actual for r in self.rutas if r["id"] == a["ruta"]))]
        
        for alerta in alertas_chofer:
            tree_alertas.insert("", tk.END, values=(
                alerta["id"],
                alerta["fecha"],
                alerta["mensaje"],
                alerta["prioridad"],
                alerta["estado"]
            ))
    
    def crear_nueva_alerta_chofer(self):
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Nueva Alerta")
        dialog.geometry("400x300")
        
        ttk.Label(dialog, text="Mensaje:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        entry_mensaje = ttk.Entry(dialog)
        entry_mensaje.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(dialog, text="Prioridad:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        entry_prioridad = ttk.Combobox(dialog, values=["Baja", "Media", "Alta"])
        entry_prioridad.set("Media")
        entry_prioridad.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
        
      
        rutas_activas = [r for r in self.rutas if r["chofer"] == self.usuario_actual and r["estado"] == "activa"]
        
        ttk.Label(dialog, text="Relacionada con ruta:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        entry_ruta = ttk.Combobox(dialog, values=["Ninguna"] + [f"{r['id']}: {r['origen']}->{r['destino']}" for r in rutas_activas])
        entry_ruta.set("Ninguna")
        entry_ruta.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)
        
        btn_guardar = ttk.Button(dialog, text="Enviar Alerta", command=lambda: self.guardar_nueva_alerta_chofer(
            entry_mensaje.get(),
            entry_prioridad.get(),
            entry_ruta.get(),
            dialog
        ))
        btn_guardar.grid(row=3, column=1, padx=5, pady=10, sticky=tk.E)
    
    def guardar_nueva_alerta_chofer(self, mensaje, prioridad, ruta, dialog):
        if not mensaje:
            messagebox.showerror("Error", "El mensaje es obligatorio")
            return
        
        nueva_alerta = {
            "id": len(self.alertas) + 1,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "mensaje": mensaje,
            "prioridad": prioridad,
            "estado": "pendiente",
            "usuario": self.usuario_actual
        }
        
        if ruta != "Ninguna":
            ruta_id = int(ruta.split(":")[0])
            nueva_alerta["ruta"] = ruta_id
        
        self.alertas.append(nueva_alerta)
        self.guardar_datos()
        self.registrar_historial(f"Nueva alerta creada por chofer: {mensaje}")
        
        dialog.destroy()
        messagebox.showinfo("Éxito", "Alerta enviada correctamente")
    
    def mostrar_entrega_confirmacion(self):
      
        frame_principal = ttk.Frame(self.content_frame)
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        ttk.Label(frame_principal, text="Confirmación de Entrega", font=("Arial", 14)).pack(pady=10)
        
        
        frame_ruta = ttk.Frame(frame_principal)
        frame_ruta.pack(fill=tk.X, pady=5)
        
        ttk.Label(frame_ruta, text="Seleccione ruta:").pack(side=tk.LEFT)
        
        rutas_activas = [r for r in self.rutas if r["chofer"] == self.usuario_actual and r["estado"] == "activa"]
        self.combo_rutas = ttk.Combobox(frame_ruta, values=[f"{r['id']}: {r['origen']}->{r['destino']}" for r in rutas_activas])
        self.combo_rutas.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
       
        frame_firma = ttk.LabelFrame(frame_principal, text="Firma del Receptor")
        frame_firma.pack(fill=tk.BOTH, expand=True, pady=10)
        
        ttk.Label(frame_firma, text="Área de firma (simulada)").pack(pady=50)
        
       
        frame_info = ttk.Frame(frame_principal)
        frame_info.pack(fill=tk.X, pady=5)
        
        ttk.Label(frame_info, text="Nombre receptor:").pack(side=tk.LEFT)
        self.entry_receptor = ttk.Entry(frame_info)
        self.entry_receptor.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        ttk.Label(frame_info, text="Comentarios:").pack(side=tk.LEFT)
        self.entry_comentarios = ttk.Entry(frame_info)
        self.entry_comentarios.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
 
        btn_confirmar = ttk.Button(frame_principal, text="Confirmar Entrega", command=self.confirmar_entrega)
        btn_confirmar.pack(pady=10)
    
    def confirmar_entrega(self):
      
        ruta_seleccionada = self.combo_rutas.get()
        receptor = self.entry_receptor.get()
        
        if not ruta_seleccionada or not receptor:
            messagebox.showerror("Error", "Seleccione una ruta e ingrese el nombre del receptor")
            return
        
        ruta_id = int(ruta_seleccionada.split(":")[0])
        comentarios = self.entry_comentarios.get()
        
    
        ruta = next((r for r in self.rutas if r["id"] == ruta_id), None)
        if ruta:
            for insumo_id in ruta["insumos"]:
                insumo = next((i for i in self.insumos if i["id"] == insumo_id), None)
                if insumo:
                    insumo["estado"] = "Entregado"
        
        self.historial.append({
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "accion": "Confirmación de entrega",
            "usuario": self.usuario_actual,
            "detalles": f"Ruta {ruta_id} - Receptor: {receptor}",
            "tipo": "entrega"
        })
        
        self.guardar_datos()
        messagebox.showinfo("Éxito", "Entrega confirmada correctamente")
        
     
        self.combo_rutas.set("")
        self.entry_receptor.delete(0, tk.END)
        self.entry_comentarios.delete(0, tk.END)
    
    def mostrar_datos_chofer(self):
       
        frame_principal = ttk.Frame(self.content_frame)
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        ttk.Label(frame_principal, text="Datos del Chofer", font=("Arial", 14)).pack(pady=10)
        
       
        frame_info = ttk.LabelFrame(frame_principal, text="Información Personal")
        frame_info.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(frame_info, text=f"Nombre: {self.usuario_actual}").pack(anchor=tk.W, pady=2)
        ttk.Label(frame_info, text="Rol: Chofer").pack(anchor=tk.W, pady=2)
        
      
        frame_stats = ttk.LabelFrame(frame_principal, text="Estadísticas")
        frame_stats.pack(fill=tk.X, padx=10, pady=5)
        
        rutas_completadas = len([r for r in self.rutas if r["chofer"] == self.usuario_actual and r["estado"] == "completada"])
        ttk.Label(frame_stats, text=f"Rutas completadas: {rutas_completadas}").pack(anchor=tk.W, pady=2)
        
        insumos_entregados = len([i for i in self.insumos if i["estado"] == "Entregado" and 
                                any(r["chofer"] == self.usuario_actual for r in self.rutas if i["id"] in r["insumos"])])
        ttk.Label(frame_stats, text=f"Insumos entregados: {insumos_entregados}").pack(anchor=tk.W, pady=2)
    
    def registrar_historial(self, accion, detalles="", tipo="sistema"):
        
        registro = {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "accion": accion,
            "usuario": self.usuario_actual,
            "detalles": detalles,
            "tipo": tipo
        }
        
        self.historial.append(registro)
        self.guardar_datos()
    
    def cerrar_sesion(self):
        
        self.registrar_historial(f"Cierre de sesión: {self.usuario_actual}")
        self.usuario_actual = None
        self.rol_actual = None
        self.crear_interfaz_login()

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaMonitoreoInsumos(root)
    root.mainloop()
