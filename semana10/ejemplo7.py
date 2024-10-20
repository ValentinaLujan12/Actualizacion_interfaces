import tkinter as tk
from tkinter import ttk

# Crear la ventana
ventana = tk.Tk()
ventana.title("Eventos")
ventana.geometry("300x200")

# Definir las funciones de los eventos
def Ok(evento):
    etiqueta.config(text="Click en botón OK")

def Cancelar(evento):
    etiqueta.config(text="Click en botón Cancelar")

button1 = ttk.Button(ventana, text="OK")
button1.pack(side='top', anchor="w", padx=10, pady=10)
button1.bind("<Button-1>", Ok)
button2 = ttk.Button(ventana, text="Cancelar")
button2.pack(side='left', anchor="n", padx=10, pady=10)
button2.bind("<Button-1>", Cancelar)
etiqueta = tk.Label(ventana, text="Presione un botón")
etiqueta.pack()

ventana.mainloop()
