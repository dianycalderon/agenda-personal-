import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime

# Función para agregar evento
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha and hora and descripcion:
        # Agregar evento a la lista
        tree.insert("", "end", values=(fecha, hora, descripcion))
        entry_fecha.delete(0, "end")
        entry_hora.delete(0, "end")
        entry_descripcion.delete(0, "end")
    else:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

# Función para eliminar evento seleccionado
def eliminar_evento():
    selected_item = tree.selection()
    if selected_item:
        confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar este evento?")
        if confirmacion:
            tree.delete(selected_item)
    else:
        messagebox.showwarning("Advertencia", "Por favor, selecciona un evento para eliminar.")

# Ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x400")

# Frame para la lista de eventos
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

# Treeview para mostrar eventos
columns = ("Fecha", "Hora", "Descripción")
tree = ttk.Treeview(frame_lista, columns=columns, show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Frame para agregar eventos
frame_agregar = tk.Frame(root)
frame_agregar.pack(pady=10)

# Campos de entrada
label_fecha = tk.Label(frame_agregar, text="Fecha (DD/MM/AAAA):")
label_fecha.grid(row=0, column=0)
entry_fecha = tk.Entry(frame_agregar)
entry_fecha.grid(row=0, column=1)

label_hora = tk.Label(frame_agregar, text="Hora (HH:MM):")
label_hora.grid(row=1, column=0)
entry_hora = tk.Entry(frame_agregar)
entry_hora.grid(row=1, column=1)

label_descripcion = tk.Label(frame_agregar, text="Descripción:")
label_descripcion.grid(row=2, column=0)
entry_descripcion = tk.Entry(frame_agregar)
entry_descripcion.grid(row=2, column=1)

# Botones
boton_agregar = tk.Button(frame_agregar, text="Agregar Evento", command=agregar_evento)
boton_agregar.grid(row=3, columnspan=2, pady=10)

boton_eliminar = tk.Button(root, text="Eliminar Evento Seleccionado", command=eliminar_evento)
boton_eliminar.pack(pady=10)

boton_salir = tk.Button(root, text="Salir", command=root.quit)
boton_salir.pack(pady=10)

# Iniciar la aplicación
root.mainloop()
