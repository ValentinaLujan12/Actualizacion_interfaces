import tkinter as tk
from tkinter import ttk

def eliminar():
    entrada2.delete(0, last=tk.END)

ventana = tk.Tk()
ventana.title("Ejemplo de Entry")
ventana.geometry("400x100")

# Crear StringVar para almacenar el texto
texto1 = tk.StringVar(value="Saludos")
texto2 = tk.StringVar(value="Saludos")

entrada1 = ttk.Entry(ventana, state="disabled", textvariable=texto1)
entrada1.grid(row=0, column=0, padx=10, pady=10, sticky="n")

entrada2 = ttk.Entry(ventana, textvariable=texto2)
entrada2.grid(row=0, column=1, padx=10, pady=10, sticky="n")

boton = ttk.Button(ventana, text="Clear", command=eliminar)
boton.grid(row=1, column=0, padx=10, pady=10, sticky="w")

ventana.mainloop()




