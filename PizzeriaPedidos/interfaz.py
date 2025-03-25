# interfaz.py

import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from orden import Orden
from cola import Cola
from graficador import graficar_cola
from PIL import ImageTk, Image
import os

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Pedidos - Pizzería")
        self.cola = Cola()
        self._crear_menu()

    def _crear_menu(self):
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack()

        tk.Label(frame, text="Menú Principal", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Button(frame, text="Nueva Orden", width=25, command=self.nueva_orden).pack(pady=5)
        tk.Button(frame, text="Entregar Orden", width=25, command=self.entregar_orden).pack(pady=5)
        tk.Button(frame, text="Ver Cola de Pedidos", width=25, command=self.ver_cola).pack(pady=5)
        tk.Button(frame, text="Salir", width=25, command=self.root.quit).pack(pady=5)

    def nueva_orden(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Nueva Orden")

        cliente = simpledialog.askstring("Cliente", "Nombre del cliente:", parent=ventana)
        if not cliente:
            ventana.destroy()
            return

        orden = Orden(cliente)

        def agregar_pizza():
            esp = especialidad_var.get()
            try:
                cant = int(cantidad_var.get())
                orden.agregar_pizza(esp, cant)
                lista.insert(tk.END, f"{cant}x {esp}")
                cantidad_var.set("1")
            except ValueError:
                messagebox.showerror("Error", "Cantidad inválida")

        def eliminar_pizza():
            sel = lista.curselection()
            if sel:
                texto = lista.get(sel[0])
                esp = texto.split("x")[1].strip()
                orden.eliminar_pizza(esp)
                lista.delete(sel[0])

        def guardar_orden():
            if orden.total_pizzas() == 0:
                messagebox.showerror("Error", "Debes agregar al menos una pizza.")
                return
            self.cola.encolar(orden)
            graficar_cola(self.cola)
            messagebox.showinfo("Orden Guardada", f"Orden agregada para {cliente}")
            ventana.destroy()

        especialidad_var = tk.StringVar(value="Pepperoni")
        cantidad_var = tk.StringVar(value="1")

        ttk.Label(ventana, text="Especialidad:").pack()
        ttk.Combobox(ventana, textvariable=especialidad_var, values=[
            "Pepperoni", "Hawaiana", "Vegetariana", "Cuatro Quesos"
        ]).pack()

        ttk.Label(ventana, text="Cantidad:").pack()
        ttk.Entry(ventana, textvariable=cantidad_var).pack()

        tk.Button(ventana, text="Agregar Pizza", command=agregar_pizza).pack(pady=5)
        lista = tk.Listbox(ventana, width=40)
        lista.pack(pady=5)

        tk.Button(ventana, text="Eliminar Seleccionada", command=eliminar_pizza).pack()
        tk.Button(ventana, text="Guardar Orden", command=guardar_orden).pack(pady=10)

    def entregar_orden(self):
        if self.cola.esta_vacia():
            messagebox.showinfo("Cola Vacía", "No hay pedidos pendientes.")
            return

        orden = self.cola.desencolar()
        graficar_cola(self.cola)

        detalle = str(orden)
        espera = sum(o.tiempo_total_orden() for o in self.cola)
        detalle += f"Tiempo de espera en cola: {espera} minutos"

        messagebox.showinfo("Orden Entregada", detalle)

    def ver_cola(self):
        if not os.path.exists("recursos/cola.png"):
            messagebox.showinfo("Sin imagen", "No hay cola generada aún.")
            return

        ventana = tk.Toplevel(self.root)
        ventana.title("Cola de Pedidos")

        img = Image.open("recursos/cola.png")
        img = img.resize((800, 200), Image.Resampling.LANCZOS)
        foto = ImageTk.PhotoImage(img)

        lbl = tk.Label(ventana, image=foto)
        lbl.image = foto
        lbl.pack()

# Punto de entrada
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
