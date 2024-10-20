import tkinter as tk
from tkinter import ttk

def opcion1():
    ventana.config(bg="blue")
    texto.config(text="Click en Menu Opción 1", background="blue")

def opcion2():
    ventana.config(bg="red")
    texto.config(text="Click en Menu Opción 2", background="red")

ventana = tk.Tk()
ventana.title("Ejemplo de Menú")
ventana.geometry("400x200")

menuBar = tk.Menu(ventana)
ventana.config(menu=menuBar)

menu1 = tk.Menu(menuBar, activebackground="blue", activeforeground="white")
menuBar.add_cascade(label="Archivo", menu=menu1)
menu1.add_command(label="Abrir")

menu2 = tk.Menu(menu1, activebackground="blue", activeforeground="white")
menu2.add_command(label="Opción 1", command=opcion1)
menu2.add_command(label="Opción 2", command=opcion2)

menu1.add_cascade(label="Salir", menu=menu2)

texto = ttk.Label(ventana, text="Presione un Menu", font=("Arial", 10))
texto.pack(anchor="w")

ventana.mainloop()
