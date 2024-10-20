import tkinter as tk
from tkinter import ttk

def botonTexto():
    print("Click en botón BotonTexto")

def botonIcono():
    print("Click en botón Icono")

def botonTextoIcono():
    print("Click en botón TextoIcono")

ventana = tk.Tk()
ventana.title("Ejemplo de Botones")
ventana.geometry("500x200")

boton1 = ttk.Button(ventana, text="BotonTexto1", command=botonTexto)
boton1.grid(row=0, column=0, padx=20, pady=10, sticky="n")

imagen1 = tk.PhotoImage(file="semana11/imagenes/carta.png")
boton2 = ttk.Button(ventana, command=botonIcono, image=imagen1)
boton2.grid(row=0, column=1, padx=10, pady=10)

boton3 = ttk.Button(ventana, text="BotonTexto2", compound="left", command=botonTextoIcono)
imagen2 = tk.PhotoImage(file="semana11/imagenes/perrito.png")
boton3.config(image=imagen2)
boton3.grid(row=0, column=2, padx=10, pady=10)

ventana.mainloop()
