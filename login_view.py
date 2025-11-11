
import tkinter as tk
from tkinter import ttk, messagebox
from auth_controller import validar_credenciales

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x500")
        self.root.title("Sistema de Login")
        self.root.resizable(False, False)
        self.crear_pantalla_login()

    def crear_pantalla_login(self):
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        # ---- Pantalla de LOGIN ----
        tk.Label(self.root, text="Bienvenido al Sistema", font=("Arial", 18, "bold")).pack(pady=20)

        tk.Label(self.root, text="Usuario o correo:").pack()
        self.username_entry = tk.Entry(self.root, width=30)
        self.username_entry.pack(pady=5)
        self.username_entry.insert(1, "Medina")

        tk.Label(self.root, text="Contraseña:").pack()
        self.password_entry = tk.Entry(self.root, show="*", width=30)
        self.password_entry.pack(pady=5)
        self.password_entry.insert(0, "1234")

        tk.Button(self.root, text="Iniciar sesión", command=self.Login, width=20).pack(pady=20)

    def Login(self):
        usuario = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not usuario or not password:
            messagebox.showwarning("Faltan datos", "Por favor ingresa usuario y contraseña")
            return

        if validar_credenciales(usuario, password):
            messagebox.showinfo("Acceso concedido", f"Bienvenido {usuario}")
            # Muestra el panel directamente en la misma ventana
            self.mostrar_panel(usuario)
        else:
            messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos")

    def mostrar_panel(self, usuario):
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        # ---- Pantalla del PANEL ----
        tk.Label(self.root, text=f"¡Hola {usuario}!", font=("Arial", 20, "bold")).pack(pady=15)

        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar usuario", width=18).pack(pady=5)
        tk.Button(frame_botones, text="Actualizar usuario", width=18).pack(pady=5)
        tk.Button(frame_botones, text="Eliminar usuario", width=18).pack(pady=5)
        tk.Button(frame_botones, text="Cerrar sesión", width=18, command=self.crear_pantalla_login).pack(pady=10)

        # Tabla de usuarios (de ejemplo)
        tk.Label(self.root, text="Lista de Usuarios", font=("Arial", 16, "bold")).pack(pady=10)

        tree = ttk.Treeview(self.root, columns=("ID", "Usuario", "Correo"), show="headings", height=6)
        tree.heading("ID", text="ID")
        tree.heading("Usuario", text="Usuario")
        tree.heading("Correo", text="Correo")
        tree.pack(padx=20, pady=10, fill="x")

        # Ejemplo de datos
        tree.insert("", "end", values=(1, "luxy", "luxy@example.com"))
        tree.insert("", "end", values=(0, "Admin", "admin@example.com"))