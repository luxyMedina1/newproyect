
import tkinter as tk
from tkinter import messagebox, ttk
from user_controller import *

class UserApp:
    def _init_(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title(f"Bienvenid@ {username}")
        self.root.geometry("400x300")
        self.root.resizable(True, True)
        self.crear_elementos()
        self.ver_usuario()
        self.root.mainloop()


    def crear_elementos(self):

        Frame_botones = tk.Frame(self.root)
        Frame_botones.pack(pady=20)

        tk.Label(Frame_botones, text=f"¡Hola {self.username}!", font=("Arial", "22", "bold")).pack(pady=15)
        tk.Button(Frame_botones, text="Agregar Usuario", command=self.agregar_usuario).pack(pady=10)    
        tk.Button(Frame_botones, text="Actualizar usuario", command=self.actualizar_usuario).pack(pady=10)
        tk.Button(Frame_botones, text="Eliminar usuario", command=self.eliminar_usuario).pack(pady=10)
        tk.Button(Frame_botones, text="Cerrar Sesion", command=self.cerrar_sesion).pack(pady=20)

        tk.Label(self.root, text=f"Lista de Usuarios", font=("Arial", "22", "bold")).pack(pady=15)

        self.tree = ttk.Treeview (self.root, columns=("ID","usuario"), show="headings", height=20)
        self.tree.heading("ID", text="ID")
        self.tree.heading("usuario",text="Usuario")
        self.tree.pack(padx=10,pady=10, fill="both",expand=True)


    def agregar_usuario(self):
        messagebox.showinfo("Agregar Usuario", "Funcionalidad para agregar usuario.")
        
    
    def ver_usuario(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        usuarios = ver_usuarios()
        for u in usuarios:
            self.tree.insert("", tk.END, values=u)

        
    def actualizar_usuario(self):
        messagebox.showinfo("Actualizar Usuario", "Funcionalidad para actualizar usuario.")

    def eliminar_usuario(self):
        messagebox.showinfo("Eliminar Usuario", "Funcionalidad para eliminar usuario.")

    def cerrar_sesion(self):
        self.root.destroy()

if __name__ == "__main__":
    App = UserApp("admin")